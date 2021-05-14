import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

ax = plt.subplot()
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()