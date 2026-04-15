import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

df = pd.read_csv('Historical Product Demand.csv').dropna()
df['Order_Demand'] = df['Order_Demand'].str.replace('(', '', regex=False).str.replace(')', '', regex=False).str.strip()
df['Order_Demand'] = pd.to_numeric(df['Order_Demand'], errors='coerce')
df = df.dropna().sample(5000, random_state=42)

X = df[['Product_Category']]
y = df['Order_Demand']
X = pd.get_dummies(X)

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

print("KNN R-squared Tuning:")
for k in [3, 5, 10]:
    knn = KNeighborsRegressor(n_neighbors=k).fit(X_train, y_train)
    print(f"k={k}: R² = {knn.score(X_val, y_val):.4f}")

print("\nDecision Tree Tuning:")
for crit in ['squared_error', 'absolute_error']:
    dt = DecisionTreeRegressor(criterion=crit).fit(X_train, y_train)
    print(f"Criterion={crit}: R² = {dt.score(X_val, y_val):.4f}")

svr = SVR(kernel='rbf').fit(X_train, y_train)
print(f"\nSVR R-squared: {svr.score(X_test, y_test):.4f}")