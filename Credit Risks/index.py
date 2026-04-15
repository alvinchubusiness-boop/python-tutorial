import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    # 1. Reading the Dataset
    # Loading the local ARFF file and converting to a DataFrame
    data, meta = arff.loadarff('dataset_31_credit-g.arff')
    df = pd.DataFrame(data)

    # Decode byte strings into readable text
    for col in df.select_dtypes([object]).columns:
        df[col] = df[col].str.decode('utf-8')

    # Drop any missing values (Requirement: Pandas one-liner)
    df = df.dropna()

    # 2. Feature Selection
    # Selected 4 Numeric and 3 Nominal features
    numeric_features = ['duration', 'credit_amount', 'age', 'existing_credits']
    nominal_features = ['checking_status', 'savings_status', 'employment']
    
    X = df[numeric_features + nominal_features]
    y = df['class']

    # 3. Preprocessing Setup
    # Using ColumnTransformer to Scale numbers and Encode categories
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), nominal_features)
        ])

    # 4. Splitting the Data (80% Training, 10% Validation, 10% Test)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.20, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

    # Fit and transform the data
    X_train_proc = preprocessor.fit_transform(X_train)
    X_val_proc = preprocessor.transform(X_val)
    X_test_proc = preprocessor.transform(X_test)

    # 5. Training Classifiers & Hyper-parameter Tuning
    # Choosing the best k by validating on the validation set
    best_k = 1
    best_val_acc = 0

    for k in range(1, 21):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_proc, y_train)
        val_preds = knn.predict(X_val_proc)
        acc = accuracy_score(y_val, val_preds)
        
        if acc > best_val_acc:
            best_val_acc = acc
            best_k = k

    print(f"Hyper-parameter Tuning: Best k = {best_k} (Val Accuracy: {best_val_acc:.4f})")

    # 6. Final Evaluation on Test Set
    knn_final = KNeighborsClassifier(n_neighbors=best_k)
    knn_final.fit(X_train_proc, y_train)
    test_preds = knn_final.predict(X_test_proc)

    print("\n--- FINAL KNN RESULTS ---")
    print(f"Accuracy Score: {accuracy_score(y_test, test_preds):.4f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, test_preds))

    # 7. Challenge Yourself: Random Forest Model
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train_proc, y_train)
    rf_preds = rf.predict(X_test_proc)
    
    print("\n--- OPTIONAL: RANDOM FOREST RESULTS ---")
    print(f"Accuracy Score: {accuracy_score(y_test, rf_preds):.4f}")

if __name__ == "__main__":
    main()