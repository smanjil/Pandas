
import pandas as pd

# create fake data
d = {
    'key': ['A', 'A', 'B'],
    'value': [23, 45, 7]
}

# create dataframe
df = pd.DataFrame(d)
# df

# group by key
group = df.groupby('key')
# group.sum()

