import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Load and Basic Clean
df = pd.read_csv('data.csv')
df = df.drop(columns=['id', 'Unnamed: 32'], errors='ignore').dropna()
# 2. Preprocessing (Encoding & Scaling)
le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])
features = [col for col in df.columns if '_mean' in col]
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[features]), columns=features)
df_scaled['diagnosis'] = df['diagnosis'].values
df_scaled.to_csv('data_refined.csv', index=False)
# 3. Visualizations
# Heatmap
plt.figure(figsize=(10,8)); sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm'); plt.title('Correlation Heatmap')
plt.show()
# Boxplot
plt.figure(figsize=(12,6)); sns.boxplot(data=df_scaled[features]); plt.xticks(rotation=45); plt.title('Box Plots')
plt.show()
# Violin Plot (Challenge)
df_melted = pd.melt(df_scaled, id_vars='diagnosis', value_vars=features)
plt.figure(figsize=(12,6)); sns.violinplot(x='variable', y='value', hue='diagnosis', data=df_melted, split=True)
plt.xticks(rotation=45); plt.title('Violin Plot Analysis')
plt.show()
print("\n--- Challenge: Violin Plot Analysis ---")
print("What is a Violin Plot?")
print("A violin plot is a hybrid of a box plot and a kernel density plot. It provides:")
print("1. Median and Quartiles: Shown by the lines inside the 'violin'.")
print("2. Distribution Shape: The width shows where the data points are most concentrated.")
print("3. Density Comparison: It helps visualize how features (like cell area) differ between Malignant and Benign tumors.")

print("\nObservation:")
print("Based on the violin plots, features like 'area_mean' show longer, thinner 'necks' for Malignant cases,")
print("indicating the presence of high-value outliers in cancerous samples.")