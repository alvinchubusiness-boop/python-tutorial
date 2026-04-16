import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Reading and Cleansing
df = pd.read_csv('Wholesale customers data.csv')
df.dropna(inplace=True)

# 2. Feature Selection: Exclude Channel and Region (categorical)
X = df.drop(['Channel', 'Region'], axis=1)

# 3. Preprocessing: Scaling (Crucial for distance-based K-Means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. K-Means: Finding optimal k and recording Inertia/Silhouette
inertias = []
k_range = range(2, 11)
print("Clustering Metrics:")
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    # Silhouette score is used as a standard internal validation metric
    score = silhouette_score(X_scaled, labels)
    print(f"k={k} -> Inertia: {kmeans.inertia_:.2f}, Silhouette Score: {score:.4f}")

# 5. Visualization: Elbow Curve Plot
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertias, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Within-cluster Sum of Squares)')
plt.title('Elbow Curve for Wholesale Data')
plt.savefig('elbow_curve.png')

# 6. Best k selection (Best Silhouette is k=3, Elbow around k=5)
best_k = 5
model = KMeans(n_clusters=best_k, random_state=42, n_init=10)
predictions = model.fit_predict(X_scaled)
print(f"\nPredicted Clusters for first 10 samples (Best k={best_k}):")
print(predictions[:10])

# 7. Challenge: Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=best_k)
h_labels = hierarchical.fit_predict(X_scaled)
print(f"Hierarchical Clustering Labels (first 10): \n{h_labels[:10]}")