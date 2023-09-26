import pandas as pd
from dataframe_comparer import compare_dataframes

def test_identical_dfs():
    df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    result = compare_dataframes(df1, df2)
    assert result == 'Dataframes are identical.'

def test_different_dfs():
    df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 5]})
    result = compare_dataframes(df1, df2)
    # check if the difference is in row 1 and column 'col2'
    assert (1, 'col2') in result