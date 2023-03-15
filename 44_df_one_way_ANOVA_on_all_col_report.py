import pandas as pd
from scipy.stats import f_oneway

# Create sample dataframe with multiple samples
#df = df_part3

def df_one_way_ANOVA_on_all_col_report(df):
    f_stat, p_val = f_oneway(*[df[col] for col in df.columns])

    # Check which set has a significant difference
    if p_val < 0.05:
        print("There is a significant difference between at least two sets")

        # Calculate the mean for each set
        means = df.mean()
        i = 0
        # Calculate the differences between sets that have a significant difference
        significant_sets = []
        for col1 in df.columns:
            for col2 in df.columns:
                if col1 < col2:
                    t_stat, p_val = ttest_ind(df[col1], df[col2])
                    if p_val < 0.05:
                        significant_sets.append((col1, col2, abs(means[col1] - means[col2]), p_val))

        # Print out the significant sets and their differences
        # Create a table to display significant differences
        print("There is a significant difference between at least two sets")
        print("| Column 1                        | Column 2                      | Mean Diff  | p-value   |")
        print("|--------------------------------|--------------------------------|------------|-----------|")
        for set in significant_sets:
            print(f"| {set[0]:<30} | {set[1]:<30} | {set[2]:.1f}  | {set[3]:<9.3g}    |")

            i += 1
            print("--" *  50)
    else:
        print("There is no significant difference between any sets")

    return df


#df_one_way_ANOVA_on_all_col_report(df_part3)
