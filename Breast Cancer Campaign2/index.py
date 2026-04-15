import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load and identify important features
df = pd.read_csv('data_refined.csv')
correlations = df.corr()['diagnosis'].abs().sort_values(ascending=False)
important_features = correlations[correlations > 0.6].index.tolist()
important_features.remove('diagnosis')
print(f"Important Features: {important_features}")

# Prepare sets
X_full = df.drop('diagnosis', axis=1)
X_reduced = df[important_features]
y = df['diagnosis']

# Split 80/10/10
X_train, X_temp, y_train, y_temp = train_test_split(X_full, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Find optimal k for KNN
knn_cv = GridSearchCV(KNeighborsClassifier(), {'n_neighbors': range(1, 21)}, cv=5)
knn_cv.fit(X_train, y_train)
best_k = knn_cv.best_params_['n_neighbors']

# Evaluate Models
for name, model in {'KNN': KNeighborsClassifier(n_neighbors=best_k), 
                    'RF': RandomForestClassifier(), 
                    'SVC': SVC()}.items():
    model.fit(X_train, y_train)
    print(f"{name} Accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")