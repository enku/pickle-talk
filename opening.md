## Opening a Pickle

```python
import pickle

with open('a_few_of_my_favorite_things.pkl', 'rb') as fp:
    data = pickle.load(fp)
```
