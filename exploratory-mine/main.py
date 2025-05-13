import argparse
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--learning_rate", type=float, default=0.01)
parser.add_argument("--epochs", type=int, default=10)
args = parser.parse_args()

# Enable autologging
mlflow.sklearn.autolog()

# Load data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

# Start MLflow run
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=args.epochs)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
