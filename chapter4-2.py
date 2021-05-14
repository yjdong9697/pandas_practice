import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.boxplot([tips[tips['sex'] == 'Female']['tip'], tips[tips['sex'] == 'Male']['tip']], labels = ["Female", 'Male'])
axes1.set_title("Boxplot of Tips by Sex")
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')

plt.show()