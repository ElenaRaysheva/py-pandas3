import pandas as pd

def diff(params):
    return params.max() - params.min()

ratings = pd.read_csv('./ratings.csv')
counts = ratings.groupby('userId')['rating'].count().reset_index(name='count')
counts = counts[counts['count'] > 100]
joined = ratings.join(counts.set_index('userId'), on='userId', how='right')
min_max = joined.groupby('userId')['timestamp'].agg(['min', 'max'])

print(
    min_max.apply(diff, 1)
)

"""
Output:
userId
4         203560
8          85187
15     471393496
17          8053
19          5282
         ...
656         3053
659     31609411
664     98180439
665     54131471
671     11283984
Length: 258, dtype: int64
"""
