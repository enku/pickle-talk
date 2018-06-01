import datetime
import pickle

data = {
    'color': 'blue',
    'day': datetime.date.today(),
    'function': print,
    int: 7,
}

with open('a_few_of_my_favorite_things.pkl', 'wb') as fp:
    pickle.dump(data, fp)
