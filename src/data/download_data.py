import kagglehub
from pathlib import Path
import shutil

DATASET = "blastchar/telco-customer-churn"

download_path = kagglehub.dataset_download(DATASET)

print(f"Downloaded dataset to: {download_path}")

source = Path(download_path) / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

destination = Path("data/raw")
destination.mkdir(parents=True, exist_ok=True)

shutil.copy(source, destination / source.name)

print("Dataset copied into project directory.")