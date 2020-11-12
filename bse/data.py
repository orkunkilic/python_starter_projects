import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as dr
import datetime

sns.set_context("poster")
sns.set(rc={'figure.figsize': (16, 9.)})
sns.set_style("whitegrid")


start=datetime.datetime(2019,1,1)
end=datetime.datetime(2019,8,23)


ülker=dr.get_data_yahoo("ULKER.IS",start,end)
close=ülker.Close
close.index = pd.DatetimeIndex(close.index)

yedi=close.rolling(window=7).mean()
on=close.rolling(window=10).mean()
yirmi=close.rolling(window=20).mean()

print(close.describe().T)

close.plot(style="-")
yedi.plot(style=".")
on.plot(style=">")
yirmi.plot(style="*")
plt.legend(["input", "yedi","on","yirmi"], loc = "upper left")

plt.show()