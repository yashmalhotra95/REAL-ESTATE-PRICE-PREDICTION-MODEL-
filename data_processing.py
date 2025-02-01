## 3. Prepare Data for Modelling
df2 = df.iloc[:,[0,4,6,22,23,1]]  #select all the numerical data with highest correlation
df2.head(5)

fig, ax = plt.subplots(3,2,figsize=(20,20))

ax[0,0].boxplot(df2.iloc[:,1])
ax[0,0].set_title(df2.iloc[:,1].to_frame().columns.values)

ax[0,1].boxplot(df2.iloc[:,2])
ax[0,1].set_title(df2.iloc[:,2].to_frame().columns.values)

ax[1,0].boxplot(df2.iloc[:,3])
ax[1,0].set_title(df2.iloc[:,3].to_frame().columns.values)

ax[1,1].boxplot(df2.iloc[:,4])
ax[1,1].set_title(df2.iloc[:,4].to_frame().columns.values)

ax[2,0].boxplot(df2.iloc[:,5])
ax[2,0].set_title(df2.iloc[:,5].to_frame().columns.values)
Text(0.5, 1.0, "['tx_price']")

lot_sizeoutlier = df2[df2['lot_size']>600000]
lot_sizeoutlier
propertytaxoutlier = df2[df2['property_tax']>3000]
propertytaxoutlier
insuranceoutlier = df2[df2['insurance']>1200]
insuranceoutlier
sqftoutlier = df2[df2['sqft']>8000]
sqftoutlier

# Out-liers are removed to create a more accurate regression model.
#Remove out-lier
df2 = df2.drop(df2.index[[102,1019,1877]])

#Train-test-split
X3 = df2.drop(['tx_price'],axis=1)
y = df2.tx_price
X_train, X_test, y_train, y_test = train_test_split(X3, y, test_size=0.2, random_state=0)

X_train.head(5)

df4=df.loc[:,['index','tx_price','beds','baths','tx_year']]
X_train = pd.merge(X_train,df4,how='inner',on='index')
y_train = X_train.tx_price
X_train = X_train.drop(['tx_price','index'], axis=1)
X_test = pd.merge(X_test,df4,how='inner',on='index')
y_test = X_test.tx_price
X_test = X_test.drop(['tx_price','index'],axis=1)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
