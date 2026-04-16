import pandas as pd
from sklearn.cluster import KMeans, MeanShift, DBSCAN, estimate_bandwidth
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

# 1. Insurance Dataset Preprocessing
df = pd.read_csv('insurance.csv').dropna()
for col in ['sex', 'smoker', 'region']:
    df[col] = LabelEncoder().fit_transform(df[col])
X_ins = StandardScaler().fit_transform(df)

# 2. K-Means Elbow Method (Insurance)
inertias = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X_ins).inertia_ for k in range(1, 11)]
plt.plot(range(1, 11), inertias, marker='o'); plt.title('Elbow Method'); plt.show()

# 3. Mean-Shift Clustering (Insurance)
bw = estimate_bandwidth(X_ins, quantile=0.2)
ms = MeanShift(bandwidth=bw).fit(X_ins)
print(f"MeanShift found {len(set(ms.labels_))} clusters in Insurance data.")

# 4. Challenge: DBSCAN on Breast Cancer Dataset
bc = load_breast_cancer()
X_bc = StandardScaler().fit_transform(bc.data)
db = DBSCAN(eps=0.5, min_samples=5).fit(X_bc)
print(f"DBSCAN found {len(set(db.labels_))} clusters/noise in BC data.")