###############################################################
# FIT9133 ASSIGNMENT 2
# TASK 3: Building a Class for Data Visualisation
# Author's name: MUKUL GUPTA
# Student ID : 29873150
# Program first created : 27 September 2018
# Program last updated : 12 October 2018
###############################################################

###################################################################################################################
#####################---------INRODUCTION-----------####################
# In this program, we create a class Visualiser and compare the statistics for the two groups of children transcripts
# by plotting bar charts.

# before running this python fil, make sure that you have installed the following libraries
# 1. pandas
# 2. numpy
# 3. matplotlib

# import the Analyser class from task2_29873150 module in order to use the statistics from the Task 2
from task2_29873150 import Analyser
# import the pandas package to use dataframes
import pandas as pd
# import numpy for creating indexes for plotting bar chart
import numpy as np
# importing pyplot from matplotlib for plotting bar charts
from matplotlib import pyplot as plt
# import os for reading files
import os


# Visualiser class is created for visualising the statistics from two groups of children transcripts
# visualise the mean of all the 10 files' statistics in SLI with mean of all the 10 files' statistics in TD
class Visualiser:
    # initialise the statistics dataframe stats_df by converting the statistics dictionary of a particular child group
    # into dataframe
    # we have a dataframe with 6 columns representing the six statistics
    def __init__(self, stats_dict):
        self.stats_df = pd.DataFrame.from_dict(stats_dict)

    # returns the mean of all 6 statistics columns
    def compute_averages(self):
        return self.stats_df.mean()

    # visualise_statistics() takes a child group object as an argument in order to compare and visualise 2 child groups
    # simultaneously
    # Reference: Franck. (2017, May 23). Retrieved from
    # https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
    # Reference: Joe. (2017, September 17). Retrieved from
    # https://stackoverflow.com/questions/6705581/rotating-xticks-causes-the-ticks-partially-hidden-in-matplotlib/21122190
    def visualise_statistics(self, visualiserObj):
        # indexes for the graph are created as we are plotting bar chart using the arange() from numpy package
        # this creates a numpy array [0,1,2,3,4,5]
        ind = np.arange(len(self.stats_df.columns))

        # create subplots as we have multiple bar charts for two different objects
        ax = plt.subplot(111)
        # create one bar chart for SLI statistics' mean
        rects_SLI = ax.bar(ind - 0.4, self.compute_averages(), width=0.4, color='r', label='SLI')
        # create one bar chart for TD statistics' mean which we get from the object passed from the argument
        rects_TD = ax.bar(ind, visualiserObj.compute_averages(), width=0.4, color='b', label='TD')
        # legend is created using the label in each of the bar chart
        ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
        # x-axis would show the name of the statistics
        plt.xticks(ind - 0.2, self.stats_df.columns, rotation=90, fontsize=8)

        # autolabel function would print the value of each statistics' mean on  top the bar
        def autolabel(rects):
            for rect in rects:
                h = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2, h + 1, '{0:.1f}'.format(float(h)),
                        ha='center', va='bottom')
        # call autolabel() for both SLI and TD
        autolabel(rects_SLI)
        autolabel(rects_TD)
        # adding title, xlabel and ylabel for the plot
        plt.title('Comparison between the statistics of SLI and TD group')
        plt.xlabel('Statistics')
        plt.ylabel('Values')
        # setting a good layout for the plot
        plt.tight_layout()
        # graph is shown using this command
        plt.show()


# main function is where objects of the Visualise class are created and methods are called on those objects
# Analyser class from Task 2 is also called to find the statistics of each child group
def main():
    # SLI group
    files_group_SLI = 'SLI'
    # set the path for SLI group files
    path_clean_files = './ENNI Cleaned/' + files_group_SLI + '_cleaned/'
    # create an Analyser object for SLI group
    analyser_ObjSLI = Analyser()
    # for each SLI file analyse_script() is called to set the statistics dictionary dor SLI group
    for each in os.listdir(path_clean_files):
        analyser_ObjSLI.analyse_script(path_clean_files + each)

    # TD group
    files_group_TD = 'TD'
    # set the path for TD group files
    path_clean_files = './ENNI Cleaned/' + files_group_TD + '_cleaned/'
    # create an Analyser object for TD group
    analyser_ObjTD = Analyser()
    # for each file analyse_script() is called to set the statistics dictionary for TD group
    for each in os.listdir(path_clean_files):
        analyser_ObjTD.analyse_script(path_clean_files + each)

    # visualiser object for SLI group is created and the stats dictionary is passed as an argument
    visualiser_SLI = Visualiser(analyser_ObjSLI.get_stats_dict())
    # visualiser object for TD group is created and the stats dictionary is passed as an argument
    visualiser_TD = Visualiser(analyser_ObjTD.get_stats_dict())
    # visualise_statistics() method is called by SLI group object and TD group object is passed as an argument.
    # this would show a bar chart comparing the mean of SLI and TD group statistics
    visualiser_SLI.visualise_statistics(visualiser_TD)


# When the program is run, special variable __name__ is initialized to __main__
# Thus code only executes when we want to run the module as a program
# Reference: Mortensen, P. (2009). Retrieved from https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
