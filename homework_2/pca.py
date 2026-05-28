import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# 读取标准化和独热编码后的数据
df = pd.read_csv("scaled_penguin_data.csv")

# 选择连续型特征进行PCA
features = [
    "Culmen_Length_mm",
    "Culmen_Depth_mm",
    "Flipper_Length_mm",
    "Body_Mass_g",
    "Island_Biscoe",
    "Island_Dream",
    "Island_Torgersen",
    "Sex_FEMALE",
    "Sex_MALE"
]
X = df[features].values

# 创建PCA对象，提取前两个主成分
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 将PCA结果转换为DataFrame
pca_df = pd.DataFrame(
    data=X_pca,
    columns=['PC1', 'PC2']
)
pca_df['Species'] = df['Species']  # 添加物种标签

# 可视化：绘制二维 PCA 散点图
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=pca_df,
    x="PC1",
    y="PC2",
    hue="Species",          
    style="Species",        
    markers=["o", "s", "D"],
    palette="Set2",
    s=70
)
plt.title("2D PCA of Penguin Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Species')
plt.grid(True)
plt.show()

# 输出解释方差比例
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance explained by 2 PCs:", sum(pca.explained_variance_ratio_))