# https://seaborn.pydata.org/generated/seaborn.scatterplot.html
#.iloc[0:20][]
# pip install -U seaborn

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)

# Group by another variable and show the groups with different colors:


ax = sns.scatterplot(x="total_bill", y="tip", hue="time",    data=tips)

# Show the grouping variable by varying both color and marker:

ax = sns.scatterplot(x="total_bill", y="tip",  hue="time", style="time", data=tips)

#Vary colors and markers to show two different grouping variables:

ax = sns.scatterplot(x="total_bill", y="tip",   hue="day", style="time", data=tips)

##Show a quantitative variable by varying the size of the points:

ax = sns.scatterplot(x="total_bill", y="tip", size="size", data=tips)

# Also show the quantitative variable by also using continuous colors:

ax = sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", data=tips)