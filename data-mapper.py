
import pandas as pd

def process (val):
    pos = list (map_file_df ['Aabaco - pishposhbaby']).index (val)
    if val in map_file_df ['Aabaco '].values:
        mapping_val = list (map_file_df ['Aabaco Columns']) [pos]
        map_index = list (map_file_df ['Aabaco ']).index (val)
        if map_file_df ['mappedCol'] [map_index] == '':
            map_file_df ['mappedCol'] [map_index] = mapping_val


if __name__ == '__main__':
    map_file_df = pd.read_csv('datamappingtest.csv').fillna('')
    map_file_df ['Aabaco - pishposhbaby'].apply (process)

    map_file_df.to_csv ('res.csv', index=False)