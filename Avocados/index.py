import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Read the Dataset
df = pd.read_csv('avocado.csv')

# Drop missing values
df = df.dropna()

# 2. Feature Extraction
# Exclude 'region', 'Date', and the 'Unnamed: 0' index column
X = df.drop(['region', 'Date', 'Unnamed: 0', 'AveragePrice'], axis=1)
y = df['AveragePrice']

# 3. Preprocessing
# Encode 'type' (conventional vs organic) to numeric values
le = LabelEncoder()
X['type'] = le.fit_transform(X['type'])

# Scaling features (Standardization is essential for distance-based models like KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split the Data (80% training, 10% validation, 10% test)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.20, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

# 5. Train KNN Regression & Hyper-parameter Tuning
# We test different values of k to see which neighborhood size predicts price best
best_k = 0
best_r2_val = -float('inf')

print("KNN Tuning Results:")
for k in range(1, 21):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    val_preds = knn.predict(X_val)
    r2_val = r2_score(y_val, val_preds)
    print(f"k={k}: Validation R² = {r2_val:.4f}")
    
    if r2_val > best_r2_val:
        best_r2_val = r2_val
        best_k = k

print(f"\nBest k found on Validation Set: {best_k}")

# 6. Final Evaluation
knn_final = KNeighborsRegressor(n_neighbors=best_k)
knn_final.fit(X_train, y_train)
knn_test_r2 = r2_score(y_test, knn_final.predict(X_test))

# Challenge: Linear Regression Comparison
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_test_r2 = r2_score(y_test, lr.predict(X_test))

print("\n--- Final Performance on Test Set ---")
print(f"KNN Regressor R²: {knn_test_r2:.4f}")
print(f"Linear Regression R²: {lr_test_r2:.4f}")