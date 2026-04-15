import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Read and Clean Dataset
df = pd.read_csv('insurance.csv').dropna()

# 2. Preparation for Visualization (Encoding for Heatmap)
le = LabelEncoder()
df_viz = df.copy()
for col in ['sex', 'smoker', 'region']:
    df_viz[col] = le.fit_transform(df_viz[col])

# --- EDA & Visualization ---
# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df_viz.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.savefig('insurance_heatmap.png')

# Pair Plots
sns.pairplot(df, hue='smoker')
plt.savefig('insurance_pairplot.png')

# Box Plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['age', 'bmi', 'children']])
plt.title('Box Plot for Feature Distribution')
plt.savefig('insurance_boxplot.png')

# 3. Preprocessing (Encoding & Scaling)
for col in ['sex', 'smoker', 'region']:
    df[col] = le.fit_transform(df[col])

X = df.drop('charges', axis=1)
y = df['charges']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split Data (80% Train, 10% Val, 10% Test)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 5. Training & Hyperparameter Tuning
# Tuning Decision Tree criteria and depth
dt_grid = GridSearchCV(DecisionTreeRegressor(random_state=42), 
                       {'criterion': ['squared_error', 'absolute_error'], 'max_depth': [3, 5, 10]}, cv=5)
dt_grid.fit(X_train, y_train)

# Tuning Random Forest estimators and depth
rf_grid = GridSearchCV(RandomForestRegressor(random_state=42), 
                       {'n_estimators': [50, 100], 'max_depth': [3, 5, 10]}, cv=5)
rf_grid.fit(X_train, y_train)

# SVR with RBF kernel and optimized penalty C
svr = SVR(kernel='rbf', C=10000).fit(X_train, y_train)

# 6. Evaluation and Comparison
models = {'Decision Tree': dt_grid.best_estimator_, 
          'Random Forest': rf_grid.best_estimator_, 
          'SVR': svr}

print("--- FINAL PERFORMANCE ON TEST SET ---")
for name, model in models.items():
    preds = model.predict(X_test)
    print(f"{name}: R2 = {r2_score(y_test, preds):.4f}, MAE = {mean_absolute_error(y_test, preds):.2f}")