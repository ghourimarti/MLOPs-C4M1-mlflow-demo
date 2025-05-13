import mlflow

# Create a new experiment
experiment_name = "my_new_experiment"
experiment_id = mlflow.create_experiment(experiment_name)

print(f"Created experiment with ID: {experiment_id}")


mlflow.set_experiment("my_new_experiment")

