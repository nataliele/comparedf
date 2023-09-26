import pandas as pd

def compare_dataframes(df1, df2):
    """
    strictly compare dataframes with the same rows in the same order.
    dfs which dont have the same rows and in the same order can be an enhancement.
    """
    if not df1.equals(df2):
        diff_locations = (df1 != df2).stack()
        changed = diff_locations[diff_locations]
        changed.index.names = ['id', 'col']
        difference_locations = changed.index
        return difference_locations
    else:
        return 'Dataframes are identical.'

def subset_data_helper(df1, df2, index_list):
    # create an index from the two columns for each dataframe
    index_df1 = df1.set_index(index_list).index
    index_df2 = df2.set_index(index_list).index

    # filter df1 for rows where the index exists in df2, order by index_list
    subset_df1 = df1[index_df1.isin(index_df2)]

    # reset index
    ordered_subset_df1 = subset_df1.sort_values(by=index_list).reset_index(drop=True)

    return ordered_subset_df1

import pandas as pd

def compare_metadata(df1: pd.DataFrame, df2: pd.DataFrame, name1: str, name2: str) -> str:
    # Prepare a dictionary with the metadata
    comparison_data = {
        "Dataframe Name": [name1, name2],
        "Number of Rows": [df1.shape[0], df2.shape[0]],
        "Number of Columns": [df1.shape[1], df2.shape[1]]
    }
    
    # Create a dataframe from the dictionary
    comparison_df = pd.DataFrame(comparison_data)
    
    # Convert the dataframe to HTML format
    table_html = comparison_df.to_html(index=False)
    
    # Construct the HTML string with mixed content
    html_output = f"""
    <h3>Comparison Results</h3>
    <p>The comparison is between <strong>{name1}</strong> and <strong>{name2}</strong>.</p>
    <p>Below is the detailed comparison:</p>
    {table_html}
    """
    
    # export to html file
    with open('your_report.html', 'w') as file:
        file.write(html_output)

    return html_output

# Example Usage:
# df1 and df2 are your dataframes
# html_result = compare_metadata(df1, df2, "DataFrame_1", "DataFrame_2")
# print(html_result)
