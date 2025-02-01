## 2. Feature Engineering
# add in house age
df["House Age"] = df.tx_year - df.year_built
# add in price/sqft
df["PriceSqft"] = df.tx_price / df.sqft
# add monthly fixed expenses
df["Expenses"] = df.property_tax + df.insurance
fig, ax = plt.subplots(figsize=(10,10))
ax2 = ax.twinx()
ax.plot(df.PriceSqft.groupby(by=df.tx_year).mean().index,df.PriceSqft.groupby(by=df.tx_year).mean().values)
ax2.plot(df.tx_price.groupby(by=df.tx_year).mean().index,df.tx_price.groupby(by=df.tx_year).mean().values,'r')
ax.set_xlabel('Year')
ax.set_ylabel("Mean price / sqft")
ax.set_title("Mean Housing Prices and Housing Prices per sq.ft from 1993 - 2016 ")
ax2.set_ylabel("Mean Housing price")
ax.legend(['Housing Prices/Sqft'],loc=1)
ax2.legend(['Mean Housing price'],loc=2)
<matplotlib.legend.Legend at 0x7b2e0bc0bdf0>
fig, ax = plt.subplots(figsize=(10,10))
ax2 = ax.twinx()
ax.plot(df.PriceSqft.groupby(by=df.tx_year).mean().index,df.PriceSqft.groupby(by=df.tx_year).mean().values)
ax2.plot(df.tx_year.groupby(by=df.tx_year).count().index,df.tx_year.groupby(by=df.tx_year).count().values,'m')
ax.set_title('Housing Prices/Sqft and No. of Transactions from 1993 - 2016 ')
ax.set_xlabel('Year')
ax.set_ylabel("Mean price / sqft")
ax2.set_ylabel("No. of Transactions")
ax.legend(['Housing Prices/Sqft'],loc=1)
ax2.legend(['No. of Transactions'],loc=2)
<matplotlib.legend.Legend at 0x7b2e0bc0bdf0>

# From the plot below, the size of houses in transaction are decreasing significantly from around 3,500 sqft in 1993 to 1,600 sqft in 2016.
plt.plot(df.sqft.groupby(by=df.tx_year).mean().index,df.sqft.groupby(by=df.tx_year).mean().values,'g')
plt.title('Size of houses')
plt.ylabel('Sq. Ft')
plt.xlabel('Year')

# Ensure `grouped_mean` only contains numeric columns
df_numeric = df.select_dtypes(include=[np.number])
grouped_mean = df_numeric.groupby(by='tx_year').mean()

# Assign to `byyear`
byyear = grouped_mean

# Extract the index (x), column names (n), and column values (v)
x = byyear.index
n = list(byyear.columns)
v = [byyear[col].values for col in byyear.columns]

# Check the output
print("Index (x):", x)
print("Column Names (n):", n)
print("Column Values (v):", v)

w = 8
h = 3
fig, ax = plt.subplots(h,w,figsize=(20,5))
plt.tight_layout()

for i in range(w):
    ax[0,i].plot(x,v[i])
    ax[1,i].plot(x,v[i+8])
    ax[2,i].plot(x,v[i+16])
    ax[0,i].set_title(n[i])
    ax[1,i].set_title(n[i+8])
    ax[2,i].set_title(n[i+16])
