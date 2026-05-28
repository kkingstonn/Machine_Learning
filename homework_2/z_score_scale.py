import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('encoded_penguin_data.csv')

# 选择需要标准化的连续型特征
continuous_features = ["Culmen_Length_mm", "Culmen_Depth_mm", "Flipper_Length_mm", "Body_Mass_g"]

# 创建标准化器
scaler = StandardScaler()

# 对连续型特征进行标准化
df[continuous_features] = scaler.fit_transform(df[continuous_features])

print(df.head())

# 保存为新文件
df.to_csv("scaled_penguin_data.csv", index=False)