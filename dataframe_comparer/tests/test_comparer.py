import unittest
import pandas as pd
from dataframe_comparer import compare_dataframes

class TestComparer(unittest.TestCase):
    def test_identical_dfs(self):
        df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        result = compare_dataframes(df1, df2)
        self.assertEqual(result, 'Dataframes are identical.')

    def test_different_dfs(self):
        df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 5]})
        result = compare_dataframes(df1, df2)
        self.assertIn((1, 'col2'), result)

if __name__ == '__main__':
    unittest.main()