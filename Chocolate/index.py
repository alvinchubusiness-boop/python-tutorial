import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
# 1. Load, Rename, and Clean
df = pd.read_csv('flavors_of_cacao.csv')
df.columns = ['Company', 'Origin', 'REF', 'ReviewDate', 'CocoaPercent', 'Location', 'Rating', 'BeanType', 'BroadOrigin']
print(f"Missing in BeanType: {df['BeanType'].isnull().sum()}")
df = df.dropna().copy()
# 2. Dataset Stats
print(f"Tuples: {len(df)} | Unique Companies: {df['Company'].nunique()}")
print(f"2013 Reviews: {len(df[df['ReviewDate'] == 2013])}")
# 3. Visualizations
df['Rating'].hist(bins=15, color='skyblue', edgecolor='black')
plt.title('Rating Distribution'); plt.show()
df['CocoaNum'] = df['CocoaPercent'].str.replace('%', '').astype(float)
df.plot.scatter(x='CocoaNum', y='Rating', alpha=0.1)
plt.title('Cocoa % vs Rating'); plt.show()
# 4. Normalization (Scikit-Learn)
scaler = MinMaxScaler()
df['NormalizedRating'] = scaler.fit_transform(df[['Rating']])
print("\nFirst 5 Normalized Ratings:\n", df['NormalizedRating'].head())
# 5. Encoding (Categorical Data)
le = LabelEncoder()
df['Company_Encoded'] = le.fit_transform(df['Company'])
df['Location_Encoded'] = le.fit_transform(df['Location'])
print("\nEncoded Data Sample:\n", df[['Company', 'Company_Encoded', 'Location', 'Location_Encoded']].head())