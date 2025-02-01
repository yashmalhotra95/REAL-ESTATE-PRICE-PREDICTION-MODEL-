//## 1.EDA
df.isnull().any()
//There are NAN values in columns 'exterior walls', 'roof' and 'basement'.
//The correlation matrix shows the correlation between each features. From the 'tx_price' column, we can see that less then 6 features have a correlation higher than 0.4 with the transaction price.
df_numeric = df.select_dtypes(include=[np.number])
