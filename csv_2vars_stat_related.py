import pandas as pd

def load_csv_rm_nan(file_path: str):
    """
    - input file path for csv file 
    - drops any rows with missing values
    """
    df = pd.read_csv(file_path)
    df = df.dropna()
    return df

# a function for making the work faster
def ROI1_vs_ROI2_pct (df, ROI_a, time_a, scan_type_a, ROI_b, time_b, scan_type_b):
    
    ''' 
    filter two df 
    - merges the two selected data sets on the ID column 
    - and calculates the percentage change 
    - between the mean values of the two datasets using the percentage_change function. Finally, it 
    renames the columns of the merged dataset to Mean_t1 and Mean_t2 and returns the modified dataframe.
    '''
    # Step1: from the main data  get rows which match the condition for examole are: t2 mag and lesion
    df_t2 = df.loc[(df.ROI==ROI_b) & (df.time==time_b) & (df.scan_type==scan_type_b)]
    df_t1 = df.loc[(df.ROI==ROI_a) & (df.time==time_a) & (df.scan_type==scan_type_a)]
    
    # Step 2; merge two selected datasets to have means in side by side columns
    new_df = df_t2.merge(df_t1,on="ID")
    new_df.head(2)
    
    # Step 3: Use this function for calculating percentage change between columns
    def percentage_change(col1,col2):
        return ((col2 - col1) / col1) * 100
    
    def percent_diff(v1,v2):
        numerator = abs(v1 - v2)
        denominator = ((v1+v2)/2)
        pct_diff = numerator * 100 / denominator
        return pct_diff

    new_df['pct_change'] = percentage_change(new_df['Mean_x'],new_df['Mean_y'])   
    new_df['pct_diff'] = percent_diff(new_df['Mean_x'],new_df['Mean_y'])   

    # Step 4: Change the col names form y to t1 (for timepoint1) and from x to t2
    new_df.rename(columns={'Mean_x': 'Mean_t1', 'Mean_y': 'Mean_t2'}, inplace=True)
    
    return new_df

import pandas as pd
import scipy.stats as stats
import numpy as np

def stat_shapiro_ttest_corr_tests(df_input, col1, col2, alpha):

    def normality_test(data):
        statistic, p_value = stats.shapiro(data)
        data1 = df_input[col1]
        data2 = df_input[col2]

        # Shapiro-Wilk test to check for normality
        mean_timepoint01, p1 = stats.shapiro(data1)
        mean_timepoint02, p2 = stats.shapiro(data2)
        print('Data shapiro statistics results=%.3f, p=%.3f' % (statistic, p_value))
        #print('Data2 shapiro statistics results=%.3f, p=%.3f' % (mean_timepoint02, p2))

        if p_value > alpha:
            
            
            return True
        else:
            return False

    def ttest(data1, data2):
        ttest_stat, p_ttest = stats.ttest_rel(data1, data2)
        return ttest_stat, p_ttest

    def mannwhitneyu_test(data1, data2):
        U1, p_mannwith = stats.mannwhitneyu(data1, data2, method="exact")
        return U1, p_mannwith

    def pearson_correlation(data1, data2):
        pearson_corr, _ = stats.pearsonr(data1, data2)
        return pearson_corr

    def spearman_correlation(data1, data2):
        spearman_corr, _ = stats.spearmanr(data1, data2)
        return spearman_corr

    data1 = df_input[col1]
    data2 = df_input[col2]

    mean_t1 = data1.mean()
    mean_t2 = data2.mean()
    
    if normality_test(data1) and normality_test(data2):
        print("Both data sets are normally distributed")
        ttest_stat, p_ttest = ttest(data1, data2)
        print('Paired student ttest statistics results=%.4f, p=%.3f' % (ttest_stat, p_ttest))
        pearson_corr = pearson_correlation(data1, data2)
        print('Pearsons correlation: %.3f' % pearson_corr)
    else:
        print("One of the data sets is not normally distributed")
        U1, p_mannwith = mannwhitneyu_test(data1, data2)
        print('Mann whitney U test statistics results=%.4f, p=%.3f' % (U1, p_mannwith))
        spearman_corr = spearman_correlation(data1, data2)
        print('Spearmans correlation: %.3f' % spearman_corr)
        
    return mean_t1, mean_t2