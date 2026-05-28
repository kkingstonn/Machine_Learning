import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('penguin_classification_edu.csv')

# 计算每个类别的数量
species_counts = df['Species'].value_counts()

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Penguin Species')
plt.show()