import pandas as pd

df = pd.read_csv('cleaned_penguin_data.csv')
# 对类别型特征进行独热编码
df_encoded = pd.get_dummies(df, columns=['Island', 'Sex'])

print(df_encoded.head())
# 保存为新文件
df_encoded.to_csv("encoded_penguin_data.csv", index=False)