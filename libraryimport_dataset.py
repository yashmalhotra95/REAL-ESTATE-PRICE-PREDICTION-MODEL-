import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
df = pd.read_csv("/content/real_estate_data.csv")
print ("Shape of dataframe: ",df.shape)
df = df.reset_index() #as there will be
df.head(5)
