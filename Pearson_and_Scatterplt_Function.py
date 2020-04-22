import os.path as op
import os
import numpy as np
import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pydoc import help
from scipy.stats.stats import pearsonr


# Directing MNE to read the data file 'AusEC.edf' and providing path to it on the desktop, and then creating a raw data object
mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)
raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')


#Reading the excel file which includes columns specifying subjective mood and focus likert-scale-values as well as those of GSR, EEG, and Date_Time values
MFT = pd.read_excel('Mood_Focus_Table.xlsx')


# Defining variables/columns for exploration of possible trends
GSR_Values = MFT['GSR_Values']
Mood_self_rating = MFT['Mood_self_rating']
Focus_self_rating = MFT['Focus_self_rating']
Date_Time = MFT['Date_Time']
Average_Total_Amplitude = MFT['Average_Total_Amplitude']
Alpha_Amplitude = MFT['Alpha_Amplitude']


#Creating Mood_Focus_Table customized (set by user) analysis of Pearson R and R^2

print("Below are the columns/data from which you may choose two to perform a pearson correlation analysis and scatterplot on. Choose two columns to begin and watch your spelling!")
print(MFT.columns)

Chosen_X = globals()[input("Type in your first (or x-axis) variable: ")]
Chosen_y = globals()[input("Type in your second (or y-axis) variable: ")]

#if Chosen_X == 'Mood' or Chosen_X == 'Mood':

#    print("Great pick for x")
#elif Chosen_y == 'Mood' or Chosen_y == 'Mood':
#    print("Great pick for y")
#else:
#    print("Uh oh, I don't know about that item")

print("Mood and focus self ratings have a pearson r and r^2 respectively of: " )
print(pearsonr(Chosen_X, Chosen_y))
#print(pearsonr(Mood, Focus))

# Create a scatter plot
plt.scatter(Chosen_X, Chosen_y)

#to access variable name
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# Set Axis Labels and Title
plt.xlabel(namestr(Chosen_X, globals()))
plt.ylabel(namestr(Chosen_y, globals()))
X_var_name = namestr(Chosen_X, globals())
Y_var_name = namestr(Chosen_y, globals())
#plottitle = concat(X_var_name + "Vs" + Y_var_name)
#plt.xlabel('Average_Total_Amplitude [in uV]')
#plt.ylabel('Alpha_Amplitude [in uV]')
plt.title(str(X_var_name) + "vs" + str(Y_var_name))
# Show and clean up again
plt.show()

# Show and clean up again
plt.clf()
