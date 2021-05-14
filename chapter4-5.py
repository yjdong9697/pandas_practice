import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
ax = plt.subplot()
ax = sns.regplot(x = 'total_bill', y = 'tip', data = tips)
ax.set_title("Scatterplot of Total Bill and Tip")
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()