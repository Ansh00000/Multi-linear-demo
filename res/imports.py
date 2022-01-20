import numpy as np
import pandas as pd
from res import DataClass as dc
import matplotlib.pyplot as plt
from res import prints as prnt

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression