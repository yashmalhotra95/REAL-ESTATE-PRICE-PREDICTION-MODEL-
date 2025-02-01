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
## 1.EDA
df.isnull().any()
# There are NAN values in columns 'exterior walls', 'roof' and 'basement'.
# The correlation matrix shows the correlation between each features. From the 'tx_price' column, we can see that less then 6 features have a correlation higher than 0.4 with the transaction price.
df_numeric = df.select_dtypes(include=[np.number])
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Compute the correlation matrix
corr_matrix = df_numeric.corr()

# Define colormap
cmap = sns.diverging_palette(250, 10, as_cmap=True)

# Create a mask for the upper triangle
mask = np.zeros_like(corr_matrix, dtype=bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 10))

# Draw the heatmap
sns.heatmap(
    corr_matrix, cmap=cmap, mask=mask, square=True, 
    cbar_kws={"shrink": 0.5}, vmin=-1.0, vmax=1.0
)

# Set seaborn style
sns.set_style('white')

# Show the plot
plt.show()

# Grouping the columns by year give us the trend of the housing market.
df['tx_year'] = pd.to_numeric(df['tx_year'], errors='coerce')

# Drop rows where `tx_year` is NaN
df = df.dropna(subset=['tx_year'])
df_numeric = df.select_dtypes(include=[np.number])
grouped_mean = df_numeric.groupby(by='tx_year').mean()
