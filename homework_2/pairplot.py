import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

df = pd.read_csv('penguin_classification_edu.csv')

columns = ['Culmen_Length_mm', 'Culmen_Depth_mm', 'Flipper_Length_mm', 'Body_Mass_g', 'Species']

penguin_data = df[columns].dropna()

sns.pairplot(penguin_data, hue='Species', diag_kind='hist', markers=['o', 's', 'D'])
plt.suptitle('Pairplot of Penguin Features', y=1.02)

plt.show()