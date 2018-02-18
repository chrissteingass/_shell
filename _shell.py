###########################################################################
###########################################################################
## [TITLE]
## Chris Steingass
###########################################################################
###########################################################################

#%%
# -------------------------------------------------------------------------
# IMPORT LIBRARIES, SET OPTIONS, READ DATA
# -------------------------------------------------------------------------
# System
import os
from os import listdir, makedirs, getcwd, remove
from os.path import isfile, join, abspath, exists, isdir

# Base
import pandas as pd, numpy as np, matplotlib.pyplot as plt
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000

# Path 
path = getcwd() + '/Dropbox/_Git/Kaggle_Telstra'
