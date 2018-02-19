###########################################################################
###########################################################################
## [TITLE]
## Chris Steingass
###########################################################################
###########################################################################

#%%
# -------------------------------------------------------------------------
# IMPORT LIBRARIES, SET OPTIONS
# -------------------------------------------------------------------------
# System
import os
from os import listdir, makedirs, getcwd, remove
from os.path import isfile, join, abspath, exists, isdir

# Base
import pandas as pd, numpy as np, matplotlib.pyplot as plt

# Options
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Path
path = getcwd() + '/Dropbox/_Code/'


# -------------------------------------------------------------------------
# IMPORT LIBRARIES, SET OPTIONS, READ DATA
# -------------------------------------------------------------------------
filenames = [

    ]

for filename in filenames:
    dataset = pd.read_csv(path + filename)
    globals()[filename.split('.')[0]] = dataset

    print(filename)
    dataset.head(3)
    print('')
