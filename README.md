# PredictFlow: MLOps Churn Prediction Tutorial

### Overview

In this tutorial, we build an end-to-end machine learning system for customer churn prediction.

We start with raw data and progressively build:

- Data preprocessing pipeline
- Feature engineering workflow
- Train/test evaluation setup
- Experiment tracking with MLflow
- (Future) Model serving API with FastAPI
- (Future) Containerization with Docker

This project is designed as a learning-first MLOps walkthrough, not just a final model.

### What You Will Learn

By completing this project, you will understand:

How to structure ML projects like production systems
How to clean and transform real-world tabular data
How to track experiments using MLflow
How to prepare models for deployment
How MLOps pipelines are organized in industry

📦 Project Structure
predictflow-mlops/
│
├── data/
│   ├── raw/              # Original dataset
│   ├── processed/        # Cleaned datasets
│
├── notebooks/            # Step-by-step learning notebooks
├── src/
│   └── data/             # Data ingestion scripts
│
├── requirements.txt
└── README.md

### Setup Instructions
1. Clone Repository
git clone <https://github.com/oeserha/predictflow-mlops.git>
cd predictflow-mlops
2. Create Virtual Environment
python -m venv .venv

Activate:

Mac/Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Download Dataset (Kaggle)

We use KaggleHub to download the Telco Customer Churn dataset.

Run:

python src/data/download_data.py

Expected output:

Dataset saved into data/raw/

### Step-by-Step Tutorial Flow
Step 1: Data Exploration
Load dataset
Inspect shape, types, missing values
Understand churn distribution

Output:

Basic dataset summary
Initial insights
Step 2: Data Cleaning
Handle missing values
Convert TotalCharges to numeric
Remove identifier columns

Output:

Clean dataset ready for feature engineering
Step 3: Feature Engineering

We transform categorical variables into numeric form:

Binary encoding (Yes/No → 0/1)
One-hot encoding for multi-class features
Domain-specific simplifications (e.g., “No internet service”)

Output:

Fully numeric dataset
Step 4: Train/Test Split

We split data using stratified sampling to preserve class balance.

Output:

train.csv
test.csv
Step 5: Experiment Tracking (MLflow)

We initialize MLflow to track:

model parameters
evaluation metrics
experiment runs

Output:

Local MLflow UI with tracked runs

### Model Development (Coming Next)

In the next phase, we will:

Train baseline models (Logistic Regression, Random Forest, XGBoost)
Compare model performance
Log results in MLflow

### Future Extensions

This project will evolve into a full MLOps system:

FastAPI inference service
Docker containerization
CI/CD pipeline
Model monitoring
Cloud deployment