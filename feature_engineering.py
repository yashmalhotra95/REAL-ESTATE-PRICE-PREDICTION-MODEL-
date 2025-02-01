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
