import pickle 

def translate_rubrics_to_pickle(rubrics: str):
    rubrics_list = rubrics[1: -1].split(', ')
    rubrics_list = list(map(lambda rubric: rubric[1: -1], rubrics_list))

    pickled_rubrics = pickle.dumps(rubrics_list)

    return pickled_rubrics

