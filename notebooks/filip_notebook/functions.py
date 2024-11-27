import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats 
from matplotlib.colors import ListedColormap
from statsmodels.stats.proportion import proportions_ztest
import os

# inspect df
def inspect_dataframe(df):
    """
    Function to perform basic inspection on a DataFrame: 
    shape, column names, data types, and missing values.
    
    """

    print('Check the shape (rows, columns):')
    print(df.shape)

    print('\nColumn names:')
    print(df.columns)


    print('\nData types:')
    print(df.dtypes)


    print('\nMissing values:')
    print(df.isnull().sum())


# check unique and empty values
def check_unique_and_empty(df):
    """
    Function to print the unique and empty values for each column in a DataFrame.
    
    """
    result = []
    
    for column in df.columns:
        unique_values = df[column].dropna().unique()
        empty_values = df[column].isna().sum()
        
        result.append({
            'Column': column,
            'Unique value count': len(unique_values),
            'Empty value count': empty_values
        })
    
    result_df = pd.DataFrame(result)
    result_df.set_index('Column', inplace=True)
    
    print("Summary of Unique and Empty Values:\n")
    print(result_df)
    print("\n" + "-"*50 + "\n")

def calculate_completion_rate(group_df, group_label):
    """Calculate completion rate for a given group (Test or Control)."""
    completion_rate = group_df[group_df['process_step'] == 'confirm'].shape[0] / group_df.shape[0]
    print(f'{group_label} Completion Rate: {completion_rate:.2f}')
    return completion_rate

def plot_completion_rate_comparison(test_completion, control_completion):
    """Plot bar chart comparing completion rates between test and control groups."""
    completion_data = {
        'Group': ['Test Group', 'Control Group'],
        'Completion Rate': [test_completion, control_completion]
    }

    completion_df = pd.DataFrame(completion_data)
    plt.figure(figsize=(6, 4))
    sns.barplot(x='Group', y='Completion Rate', data=completion_df, hue='Group', palette='viridis', width=0.5)
    plt.title('Completion Rate Comparison', fontsize=16)
    plt.ylabel('Completion Rate', fontsize=14)
    plt.ylim(0, 1)
    plt.savefig('completion_rate_comparison.png', format='png', dpi=300, bbox_inches='tight')
    plt.show()

def perform_z_test(test_group, control_group):
    """Perform Z-test for proportions comparing test and control groups."""
    successes = [
        test_group[test_group['process_step'] == 'confirm'].shape[0], 
        control_group[control_group['process_step'] == 'confirm'].shape[0]
    ]
    totals = [test_group.shape[0], control_group.shape[0]]
    stat, p_value = proportions_ztest(successes, totals)
    print(f'Z-statistic: {stat:.2f}, P-value: {p_value:.2f}')
    return stat, p_value

def calculate_completion_rate_difference(test_completion, control_completion):
    """Calculate and print the difference in completion rates."""
    completion_rate_diff = test_completion - control_completion
    print(f'Completion Rate Difference: {completion_rate_diff:.2f}')
    return completion_rate_diff

def calculate_completion_rate_increase(test_completion, control_completion):
    """Calculate and print the percentage increase in completion rate."""
    completion_rate_increase = (test_completion - control_completion) / control_completion * 100
    print(f'Completion Rate Increase: {completion_rate_increase:.2f}%')
    return completion_rate_increase

def check_cost_effectiveness(completion_rate_increase, threshold=5):
    """Check if the completion rate increase meets the cost-effectiveness threshold."""
    if completion_rate_increase >= threshold:
        print("The new design meets the cost-effectiveness threshold.")
    else:
        print("The new design does not meet the cost-effectiveness threshold.")

def plot_error_rate(test_group, control_group, df_clean):
    """Calculate and plot error rates for test and control groups."""
    df_clean['previous_step'] = df_clean.groupby('visit_id')['process_step'].shift(1)
    df_clean['backward_step'] = df_clean['process_step'].astype(str) < df_clean['previous_step'].astype(str)

    error_rate_test = df_clean[(df_clean['variation'] == 'Test') & (df_clean['backward_step'] == True)].shape[0] / df_clean[df_clean['variation'] == 'Test'].shape[0]
    error_rate_control = df_clean[(df_clean['variation'] == 'Control') & (df_clean['backward_step'] == True)].shape[0] / df_clean[df_clean['variation'] == 'Control'].shape[0]

    print(f'Error Rate (Test): {error_rate_test:.2f}')
    print(f'Error Rate (Control): {error_rate_control:.2f}')

def calculate_time_spent_per_step(df_all_clean):
    """Calculate average time spent per process step."""
    df_all_clean['date_time'] = pd.to_datetime(df_all_clean['date_time'])
    df_all_clean = df_all_clean.sort_values(by=['client_id', 'date_time'])
    df_all_clean['time_diff'] = df_all_clean.groupby('client_id')['date_time'].diff()
    
    time_per_step = df_all_clean.groupby('process_step')['time_diff'].mean()
    print("Average time spent per step:")
    print(time_per_step)
    return time_per_step

def plot_time_spent_by_step(df_all_clean):
    """Plot average time spent on each step by variation group."""
    data = df_all_clean.sort_values(by=['visitor_id', 'date_time'])
    data['time_diff'] = data.groupby('visitor_id')['date_time'].diff()

    time_spent_by_step = data.groupby(['Variation', 'process_step'])['time_diff'].mean().reset_index()

    plt.figure(figsize=(8, 6))
    sns.barplot(x='process_step', y='time_diff', hue='Variation', data=time_spent_by_step, palette='coolwarm')
    plt.title('Average Time Spent on Each Step by Group', fontsize=16)
    plt.xlabel('Process Step', fontsize=14)
    plt.ylabel('Average Time (seconds)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('time_spent_per_step.png', format='png', dpi=300)
    plt.show()
