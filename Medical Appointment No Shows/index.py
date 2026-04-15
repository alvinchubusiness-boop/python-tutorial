import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Reading the Dataset
df = pd.read_csv('KaggleV2-May-2016.csv')

# Drop missing values (one line of code)
df = df.dropna()

# 2. Feature Extraction
# Included Gender, Age, Scholarship, and correctly spelled medical features
features = ['Gender', 'Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received']
X = df[features].copy()
y = df['No-show'].copy()

# 3. Preprocessing
# Encoding target (No=0, Yes=1) and categorical Gender
le = LabelEncoder()
y = le.fit_transform(y)
X['Gender'] = le.fit_transform(X['Gender'])

# Scaling Age (Numerical feature)
scaler = StandardScaler()
X['Age'] = scaler.fit_transform(X[['Age']])

# 4. Splitting the Data (80% Train, 10% Validation, 10% Test)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 5. Training Decision Tree & Hyper-parameter Tuning (Criterion)
best_dt_acc = 0
best_crit = ""

for crit in ['gini', 'entropy']:
    dt = DecisionTreeClassifier(criterion=crit, random_state=42)
    dt.fit(X_train, y_train)
    acc = accuracy_score(y_val, dt.predict(X_val))
    print(f"Decision Tree (Criterion={crit}): Validation Accuracy = {acc:.4f}")
    if acc > best_dt_acc:
        best_dt_acc = acc
        best_crit = crit

# 6. Training Random Forest & Hyper-parameter Tuning (n_estimators)
print("\n--- Random Forest Tuning ---")
for n in [10, 50, 100]:
    rf = RandomForestClassifier(n_estimators=n, random_state=42)
    rf.fit(X_train, y_train)
    acc = accuracy_score(y_val, rf.predict(X_val))
    print(f"Random Forest (n_estimators={n}): Validation Accuracy = {acc:.4f}")

# Final Evaluation of the best model (Decision Tree with Gini)
dt_final = DecisionTreeClassifier(criterion=best_crit, random_state=42)
dt_final.fit(X_train, y_train)
y_pred = dt_final.predict(X_test)

print(f"\nFinal Classifier Accuracy (DT - {best_crit}): {accuracy_score(y_test, y_pred):.4f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))