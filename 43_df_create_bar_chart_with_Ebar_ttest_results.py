import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

class BarChart:
    def __init__(self,df,title):
        self.df = df
        self.title = title
        
    def create_bar_chart(self,col1,col2, col3):
        # Calculate mean and standard deviation
        mean = self.df[[col1,col2, col3]].mean()
        std = self.df[[col1,col2, col3]].std()

        # T-test comparison outcome
        t, p = ttest_ind(self.df[col1], self.df[col2])
        t2,p2, = ttest_ind(self.df[col1], self.df[col3])
        
        plt.figure(figsize=(2, 3))
        plt.rcParams.update({'font.size': 9})
        # Plot bar chart with error bars (standard deviation) and T-shape capsize
        # only show the bottom half of error bar 
        #lower_error = std/2
        # only show the to part
        std = self.df[[col1,col2,col3]].std()
        upper_std = np.array([std[col1]/2, std[col2]/2, std[col3]/2])
        
        #plt.bar(x=[col1, col2, col3], height=mean, width= 0.6, color = 'black', yerr=upper_std, align='center', \
         #       alpha=0.5, capsize = std/2)
        plt.title(self.title)
        
          # Plot bar chart with error bars (standard deviation) and T-shape capsize
        plt.bar(x=[col1, col2, col3], height=mean, width= 0.4, color = 'black', yerr=std, align='center', \
                alpha=0.5, capsize = 5, error_kw={'capsize': 5, 'capthick': 2, \
                                                                                                                                            'ecolor': 'black'})
        plt.title(self.title)
        
        move_p_val_upward = 5
        # Add t-test comparison outcome p-value to the plot
        #plt.text(0, (mean[0]+std[0])+move_p_val_upward, f'p={p:.3f}')
        plt.text(0.6, (mean[1]+std[1])+move_p_val_upward, f'p={p:.3f}')
        plt.text(1.2, (mean[2]+std[2])+move_p_val_upward, f'p={p2:.3f}')
        
        # Rotate the x-axis labels by 45 degrees
        plt.xticks(rotation=35)
        plt.xticks(np.arange(3),[col1, col2, col3])
      
        plt.show()
        

#         #ok- works 
# barchart = BarChart(df, "Title of the chart")

# barchart.create_bar_chart('t1_t2_pct_diff_Cor_Tra', 't1_t2_pct_diff_Tra_Sag', 't1_t2_pct_diff_Lmag')
