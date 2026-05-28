import pandas as pd

df= pd.read_csv('penguin_classification_edu.csv')

# 连续型特征填中位数
continuous_features = ["Culmen_Length_mm", "Body_Mass_g"]
for col in continuous_features:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)
    print(f"{col} 用中位数 {median_val} 填补缺失值")

# 类别型特征填众数
categorical_features = ["Sex"]
for col in categorical_features:
    mode_val = df[col].mode()[0]
    df[col] = df[col].fillna(mode_val)
    print(f"{col} 用众数 {mode_val} 填补缺失值")

print("体重大于10000的样本数量:", (df["Body_Mass_g"] > 10000).sum())
print("脚蹼长度大于300的样本数量:", (df["Flipper_Length_mm"] > 300).sum())
# 异常值剔除
# 阈值设定
print(f"\n清洗后的样本数量: {len(df)}")
# 正常值条件
mask = (df["Body_Mass_g"] <= 10000) & (df["Flipper_Length_mm"] <= 300)

# 筛选
df_clean = df[mask]

print(f"异常值剔除后样本数量: {len(df_clean)}")

# 另存为新文件
df_clean.to_csv("cleaned_penguin_data.csv", index=False)