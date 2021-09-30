import pandas as pd
import glob
import os

def df_from_dir(data_path: str, printout: bool = False) -> pd.DataFrame:
    '''
    '''
    all_files = glob.glob(os.path.join(data_path, '*.csv'))

    # Read all CSVs into one
    df_all = pd.concat(
        map(pd.read_csv, all_files), 
        ignore_index=True,
    )
    if printout:
        print(f'Columns: {", ".join(df_all.columns)}')
        print('Random Sample: ')
        print(df_all.sample(5))
    
    return df_all

if __name__ == '__main__':
    # Find path to data (CSVs)
    df = df_from_dir('courses_csv', printout=True)