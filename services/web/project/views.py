from . import app, db

from .models import Text

from flask import jsonify, request
from operator import itemgetter
import pickle 

@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route('/search-by-text/api/v1.0/texts/', methods=['POST'])
def create_text():
    rubrics = translate_rubrics_to_pickle(request.form['rubrics'])
    text = request.form['text']
    created_date = request.form['created_date']

    try:
        text_model = Text(rubrics=rubrics, text=text, created_date=created_date)
        db.session.add(text_model)
        db.session.commit()
    except:
        return app.make_response(('Not created', 400))
    
    app.elasticsearch.index(index='text_ind', doc_type='text_ind', id=text_model.id, body={'text': text})

    return app.make_response(('Created, id: {0}'.format(text_model.id), 201))

@app.route('/search-by-text/api/v1.0/texts/<int:text_id>', methods=['GET'])
def get_text(text_id):
    text = Text.query.filter(Text.id == text_id).first_or_404()

    return jsonify(id=text.id, rubrics=pickle.loads(text.rubrics), text=text.text, created_date=text.created_date)

@app.route('/search-by-text/api/v1.0/texts/<int:text_id>', methods=['DELETE'])
def delete_text(text_id):
    text = Text.query.filter(Text.id == text_id).first_or_404()

    try:
        db.session.delete(text)
        db.session.commit()
        app.elasticsearch.delete(index='text_ind', doc_type='text_ind', id=text_id)
    except:
        return app.make_response(('Not deleted', 400))

    return app.make_response(('Deleted', 204))
    
@app.route('/search-by-text/api/v1.0/texts', methods=['GET'])
def get_sought_texts():
    query = request.args.get("q")

    try:
        search = app.elasticsearch.search(
            index='text_ind', 
            doc_type='text_ind', 
            body={'query': {'match': {'text': query}}},
            size=20
        )
    except:
        return app.make_response(('No data', 400))

    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    result = []
    
    for ind in ids:
        text = Text.query.filter(Text.id == ind).first_or_404()
        result.append({
            'id': ind, 
            'rubrics': pickle.loads(text.rubrics), 
            'text': text.text, 
            'created_date': text.created_date,
            })

    result = sorted(result, key=itemgetter('created_date'))

    return jsonify(result)

def translate_rubrics_to_pickle(rubrics: str):
    rubrics_list = rubrics[1: -1].split(', ')
    rubrics_list = list(map(lambda rubric: rubric[1: -1], rubrics_list))

    pickled_rubrics = pickle.dumps(rubrics_list)

    return pickled_rubrics