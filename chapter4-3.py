import matplotlib.pyplot as plt
import seaborn as sns

def recode_sex(sex):
    if sex == 'Female':
        return 0
    else : return 1

tips = sns.load_dataset('tips')
fig = plt.figure()

tips['sex_color'] = tips['sex'].apply(recode_sex)
axes1 = fig.add_subplot(1, 1, 1)
axes1.scatter(
    x = tips['total_bill'],
    y = tips['tip'],
    s = tips['size'] * 10,
    c = tips['sex_color'],
    alpha = 0.5
)

axes1.set_title("Total Bill vs Tip Colored by Sex and Sized by Size")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")
plt.show()