import pandas as pd
import glob
import os

# Find path to data (CSVs)
data_path = 'courses_csv'
all_files = glob.glob(os.path.join(data_path, '*.csv'))

# Read all CSVs into one
df_all = pd.concat(
        map(pd.read_csv, all_files), 
        ignore_index=True
)

print(f'Columns: {", ".join(df_all.columns)}')
print('Random Sample: ')
print(df_all.sample(5))