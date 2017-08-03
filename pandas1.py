
import pandas as pd

# series
years = pd.Series([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999])
# print years

# dataframe
guitars = pd.DataFrame({
    'store1': [584, 601, 403, 480],
    'store2': [1032, 960, 1400, 1355],
    'year': [2012, 2013, 2014, 2015]
})
# print guitars

# selecting columns from dataframes
# print guitars['store1']

# selecting rows from dataframes
# print guitars.loc[0]

# selecting multiple columns from dataframe
# print guitars[['store1', 'year']]

# selecting multiple rows
# print guitars.loc[0:2]

# get all rows where store1 sold over 500 guitars
# print guitars[guitars['store1'] > 500]

# dealing missing values
_2016 = pd.DataFrame([[None, 300, 2016]], columns=guitars.columns)
guitars = guitars.append(_2016, ignore_index=True)
# print guitars

# print guitars.isnull()

# drop if there is even one null value
# print guitars.dropna()

# drop only if all values are null
# print guitars.dropna(how='all')

# fill null values with 0
# print guitars.fillna(0)

# print guitars.fillna(method='ffill')

# print guitars.index

# change index of dataframe
guitars = guitars.set_index('year')
# print guitars.loc[2012]
# print guitars.iloc[0]

# hierarchial index
guitars = guitars.set_index([['old', 'old', 'new', 'new', 'new'], guitars.index])

old = guitars.loc['old']
# old

# guitars.loc['old', 2012]

# transpose
transposed = guitars.T
# transposed

# dropping the hierarchial index and restoring to the original dataframe
guitars.index = guitars.index.droplevel()
# guitars

# plotting
guitars.index = pd.to_datetime(guitars.index, format='%Y')
# guitars.plot(ylim=0)
guitars.plot(kind='bar')











