import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
obesity_data = pd.read_csv('data.csv')
obesity_data.head()
obesity_data = obesity_data.drop(0)
obesity_data = obesity_data.drop(1)
obesity_data.iloc[0][0] = ''
obesity_data.rename(columns={'Unnamed: 0':'Country'},inplace=True)
obesity_data.reset_index(inplace=True,drop=True)
obesity_both = {}
col = len(obesity_data.columns)
ran = list(range(1,col,3))
for i,j in obesity_data.iterrows():
    if(i == 0):
        pass
    else:
        _list = []
        m = j[0]
        t = j[ran]
        for l in t:
            _list.append(l.split(' ')[0])
        obesity_both[m] = _list
fig,a = plt.subplots(len(obesity_both))
year = list(range(1975,2017))
m = 0
for country,val in obesity_both.items():
    a[m].plot(year,val)
    a[m].set_title(country)
    m += 1
plt.show()
