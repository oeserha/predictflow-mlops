import mlflow

mlflow.set_experiment(
    "telco_churn"
)

with mlflow.start_run():

    mlflow.log_param(
        "model_type",
        "baseline"
    )

    mlflow.log_metric(
        "placeholder_metric",
        0.0
    )

print("Run complete")