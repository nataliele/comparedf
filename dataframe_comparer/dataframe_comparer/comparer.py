import pandas as pd

def compare_dataframes(df1, df2):
    if not df1.equals(df2):
        diff_locations = (df1 != df2).stack()
        changed = diff_locations[diff_locations]
        changed.index.names = ['id', 'col']
        difference_locations = changed.index
        return difference_locations
    else:
        return 'Dataframes are identical.'