import pandas as pd
import scipy.stats as stats
import numpy as np

def combined_tests(df_input, col1, col2, alpha):

    def normality_test(data):
        statistic, p_value = stats.shapiro(data)
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

df = pd.DataFrame({'group1': np.random.normal(5, 2, 100),
                  'group2': np.random.normal(6, 1, 100)})
combined_tests(df,'group1','group2',0.05)