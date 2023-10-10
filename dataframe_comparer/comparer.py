import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    """
    enhancement to add date created, date modified
    """
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
    return table_html

def compare_columns(df1: pd.DataFrame, df2: pd.DataFrame, name1: str, name2: str) -> str:
    # Columns in common
    common_columns = df1.columns.intersection(df2.columns).tolist()
    
    # Columns in df1 but not in df2
    df1_unique_columns = df1.columns.difference(df2.columns).tolist()
    
    # Columns in df2 but not in df1
    df2_unique_columns = df2.columns.difference(df1.columns).tolist()
    
    # Create a DataFrame with the comparison results
    comparison_data = {
        "Description": ["Columns in common", "Columns in df1 not in df2", "Columns in df2 not in df1"],
        "Number of Columns": [len(common_columns), len(df1_unique_columns), len(df2_unique_columns)],
        "Column Names": [common_columns, df1_unique_columns, df2_unique_columns]
    }
    comparison_df = pd.DataFrame(comparison_data)
    
    # Convert the dataframe to HTML format
    table_html = comparison_df.to_html(index=False, escape=False)
    return table_html

def compare_values(df1: pd.DataFrame, df2: pd.DataFrame) -> str:
    # Ensure dataframes have the same columns
    if set(df1.columns) != set(df2.columns):
        raise ValueError("The two dataframes don't have the same columns.")
    
    columns_all_equal = []
    columns_some_unequal = []
    summary_data = []

    for col in df1.columns:
        if df1[col].equals(df2[col]):
            columns_all_equal.append(col)
        else:
            columns_some_unequal.append(col)

            # Compute number of different values and the maximum difference
            mask = df1[col] != df2[col]
            num_different_values = mask.sum()
            
            # Calculate the maximum difference (if the column data type is numeric)
            if np.issubdtype(df1[col].dtype, np.number):
                max_difference = (df1[col] - df2[col]).abs().max()
            else:
                max_difference = "N/A"

            summary_data.append({
                "Column Name": col,
                "Data Type": df1[col].dtype,
                "Number of Different Values": num_different_values,
                "Maximum Difference": max_difference
            })

    # Convert the summary data to a DataFrame
    detailed_df = pd.DataFrame(summary_data)

    # High-level summary DataFrame
    high_level_data = {
        "Description": ["Columns with all observations equal", "Columns with some observations unequal"],
        "Count": [len(columns_all_equal), len(columns_some_unequal)]
    }
    high_level_df = pd.DataFrame(high_level_data)

    # Convert the dataframes to HTML
    table_html_high_level = high_level_df.to_html(index=False)
    table_html_detailed = detailed_df.to_html(index=False)

    return table_html_high_level, table_html_detailed

def plot_distributions(df1, df2, name1, name2, variable_name):
    """
    Plot the distributions of a variable from two dataframes and the distribution of their differences.
    
    Parameters:
    - df1: The first DataFrame.
    - df2: The second DataFrame.
    - variable_name: The name of the variable in both dataframes.
    """
    
    plt.figure(figsize=(12, 5))
    
    # Plot distributions of the variable from both dataframes
    plt.subplot(1, 2, 1)
    sns.histplot(df1[variable_name], color='blue', alpha=0.5, label=f'{name1}', kde=True)
    sns.histplot(df2[variable_name], color='red', alpha=0.5, label=f'{name2}', kde=True)
    plt.title('Distributions of the Variable from Two DataFrames')
    plt.legend()
    
    # Ensure both dataframes have the same number of rows for difference plotting
    if len(df1) != len(df2):
        raise ValueError("The two dataframes don't have the same number of rows.")
    
    # Plot distribution of the difference between the variables from the two dataframes
    plt.subplot(1, 2, 2)
    sns.histplot(df1[variable_name] - df2[variable_name], color='green', kde=True)
    plt.title(f'Distribution of Differences ({name1} - {name2})')
    
    plt.tight_layout()
    plt.show()

def output_results(metadata_table, column_table, value_table_high_level, value_table, name1, name2):
    # Construct the HTML string with mixed content
    html_output = f"""
    <h3>Comparison Results</h3>
    <p>The comparison is between <strong>{name1}</strong> and <strong>{name2}</strong>.</p>
    <p>Below is the detailed comparison:</p>
    {metadata_table}

    <h3>Column Comparison Results</h3>
    <p>Below is the detailed comparison of columns between the two dataframes:</p>
    {column_table}

    <h3>Value Comparison Results</h3>
    <h4>High-Level Summary:</h4>
    {value_table_high_level}
    <h4>Detailed Summary of columns with unequal values:</h4>
    {value_table}

    """
    
    # export to html file
    with open('your_report.html', 'w') as file:
        file.write(html_output)

    return html_output

# Example Usage:
# df1 and df2 are your dataframes
# html_result = compare_metadata(df1, df2, "DataFrame_1", "DataFrame_2")
# print(html_result)
