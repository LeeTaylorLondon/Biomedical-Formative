# Author: Lee Taylor, ST No: 190211479
from imports import *

## Read data
df = pd.read_csv("Data/data.csv")

## Create poisonous dataframe and edible dataframe
poi, edi = df.__copy__(), df.__copy__()
for i,v in enumerate(poi.values):
    if v[0] == 'e': poi = poi.drop(index=i)
    else: edi = edi.drop(index=i)

## Check shapes
print(df.shape)
print(poi.shape)
print(edi.shape)

## Create plot
fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8))
ax.scatter(x=poi['stalk-color-above-ring'], y=poi['stalk-color-below-ring'],
           color='red')
ax.scatter(x=edi['stalk-color-above-ring'], y=edi['stalk-color-below-ring'],
           color='green')
ax.grid()
plt.show()