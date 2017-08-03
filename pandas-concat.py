
import pandas as pd

# create fake data
df1 = pd.DataFrame({'id': [6, 7, 8]})
df2 = pd.DataFrame({'id': [9, 10, 11]})

# glue the dataframes together
df = pd.concat([df1, df2], ignore_index=True)
# df