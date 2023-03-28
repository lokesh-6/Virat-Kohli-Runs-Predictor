import pickle
import json
import numpy as np

__teams = None
__data_columns = None
__model = None

def get_estimated_runs(Bf,fours,sixes,teams):
    try:
        loc_index = __data_columns.index(teams.lower())
    except:
        loc_index = -1

    a = np.zeros(len(__data_columns))
    a[0] = Bf
    a[1] = fours
    a[2] = sixes
    if loc_index>=0:
        a[loc_index] = 1

    return round(__model.predict([a])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __teams

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __teams = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/virat_kohli_runs_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_team_names():
    return __teams

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_team_names())
    print(get_estimated_runs(95,16,1,'Australia'))
    print(get_estimated_runs(100,2,3,'Australia'))
    print(get_estimated_runs(100,2,3,'Bangladesh')) # other location
    print(get_estimated_runs(100,2,3,'Pakistan')) # other location