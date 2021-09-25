import pandas as pd

# read csv file with old column names and new column names
dict_from_csv = pd.read_csv('data/map_col_names.csv', header=None, index_col=0, squeeze=True).to_dict()

# read in .csv with socioeconomic data
data_df = pd.read_csv('data/..')
# rename columns
data_df = data_df.rename(dict_from_csv, axis = 1)
# save file 
data_df.to_csv('data/socioeconomic_data_new_col_names.csv', index = False)