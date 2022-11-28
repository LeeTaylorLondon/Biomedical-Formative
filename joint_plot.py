# Author: Lee Taylor, ST No: 190211479
from imports import *


## Read data
df = pd.read_csv("Data/data.csv")


## Create poisonous dataframe and edible dataframe
# poi, edi = df.__copy__(), df.__copy__()
# for i,v in enumerate(poi.values):
#     if v[0] == 'e': poi = poi.drop(index=i)
#     else: edi = edi.drop(index=i)

'''  
g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6)
'''

# Replace colors numerics
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('w', 1)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('b', 2)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('p', 3)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('n', 4)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('y', 5)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('c', 6)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('o', 7)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('g', 8)
df['stalk-color-above-ring'] = df['stalk-color-above-ring'].replace('e', 9)
print(df['stalk-color-above-ring'])

df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('w', 1)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('b', 2)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('p', 3)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('n', 4)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('y', 5)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('c', 6)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('o', 7)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('g', 8)
df['stalk-color-below-ring'] = df['stalk-color-below-ring'].replace('e', 9)

# Create joint-plot
g = sns.jointplot(x='stalk-color-above-ring',
                  y='stalk-color-below-ring',
                  kind="scatter", data=df,
                  hue='edible-poisonous')


# show the plot
plt.show()
