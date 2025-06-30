import pandas as pd
import xgboost as xgb
import optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump

# Load and split data
data = pd.read_csv("data/synthetic_credit_data.csv")
X = data.drop("creditworthy", axis=1)
y = data["creditworthy"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3),
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
    }
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return accuracy_score(y_test, preds)

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)
best_model = xgb.XGBClassifier(**study.best_params)
best_model.fit(X_train, y_train)
preds = best_model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, preds))
print("✅ Accuracy:", accuracy_score(y_test, preds))

dump(best_model, "models/credit_model.pkl")