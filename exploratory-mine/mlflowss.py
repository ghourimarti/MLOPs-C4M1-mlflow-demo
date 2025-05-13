# import mlflow
from mlflow import log_metric, log_param, log_artifact


if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("threshold", 3)
    log_param("verbosity", "DEBUG")
    log_metric("timestamp", 10000)
    log_metric("TTC", 33)
    # log_artifact("produced-dataset.csv")

    log_param("num_dimensions", 8)
    log_param("regularization", 0.1)


    # Log a metric; metrics can be updated throughout the run
    log_metric("accuracy", 0.1)
    # ...
    log_metric("accuracy", 0.45)


    # # Log artifacts(output files)
    # log_artifact("roc.png")
    # log_artifact("model.pkl")

# https://mlflow.org/docs/latest/introduction/index.html