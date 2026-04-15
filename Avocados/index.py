import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

df = pd.read_csv('avocado.csv').drop(['Unnamed: 0', 'Date', 'region'], axis=1).dropna()

df['type'] = LabelEncoder().fit_transform(df['type'])
X, y = df.drop('AveragePrice', axis=1), df['AveragePrice']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s, X_test_s = scaler.transform(X_val), scaler.transform(X_test)

for k in [2, 4, 6, 10]:
    knn = KNeighborsRegressor(n_neighbors=k).fit(X_train_s, y_train)
    print(f"KNN k={k} Val R2: {knn.score(X_val_s, y_val):.4f}")

best_knn = KNeighborsRegressor(n_neighbors=4).fit(X_train_s, y_train)
lr = LinearRegression().fit(X_train_s, y_train)

print(f"\nFinal KNN Test R2: {best_knn.score(X_test_s, y_test):.4f}")
print(f"Linear Regression Test R2: {lr.score(X_test_s, y_test):.4f}")