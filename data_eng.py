from pandas.core.frame import DataFrame
# Pandas
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pip
install
ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
auto_mpg = fetch_ucirepo(id=9)

# data (as pandas dataframes)
X = auto_mpg.data.features
y = auto_mpg.data.targets

# metadata
print(auto_mpg.metadata)

# variable information
print(auto_mpg.variables) 