import pickle

with open('a_few_of_my_favorite_things.pkl', 'rb') as fp:
    favorites = pickle.load(fp)
