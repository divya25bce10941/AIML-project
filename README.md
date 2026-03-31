# 🏥 Insurance Charges Predictor

A machine learning project that predicts individual medical insurance charges using Linear Regression, based on demographic and personal data such as age, BMI, smoking status, and more.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Output](#output)
- [Model Evaluation](#model-evaluation)
- [Extending the Project](#extending-the-project)

---

## Project Overview

This project builds an interpretable Linear Regression model to predict what an individual is likely to be charged by their health insurer, based on:

| Feature    | Description                              |
|------------|------------------------------------------|
| `age`      | Age of the primary beneficiary           |
| `sex`      | Gender (male / female)                   |
| `bmi`      | Body Mass Index                          |
| `children` | Number of dependents covered             |
| `smoker`   | Smoking status (yes / no)                |
| `region`   | Residential region in the US             |
| `charges`  | **Target** — medical cost billed       |

---

## Dataset

The project uses the publicly available **Medical Cost Personal Dataset** (`insurance.csv`).

- **Rows:** 1,338 records
- **Columns:** 7 (6 features + 1 target)
- **Source:** [Kaggle — Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

> **Download the dataset** and place it in a `data/` folder at the root of the project:
> ```
> data/
> └── insurance.csv
> ```

---

## Project Structure

```
insurance-charges-predictor/
│
├── data/
│   └── insurance.csv          # Dataset (download separately)
│
├── main.py                    # Training script
├── model.pkl                  # Saved trained model (generated after running)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)
- **pip** — comes bundled with Python 3.4+

To verify your Python installation, run:

```bash
python --version
# or
python3 --version
```

---

## Environment Setup

It is strongly recommended to use a **virtual environment** to avoid dependency conflicts.

### Step 1 — Clone or download the project

```bash
# If using Git
git clone https://github.com/your-username/insurance-charges-predictor.git
cd insurance-charges-predictor

# Or simply navigate to the folder where you saved the project files
cd path/to/insurance-charges-predictor
```

### Step 2 — Create a virtual environment

```bash
# On macOS / Linux
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# On Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

You should see `(venv)` appear at the start of your terminal prompt, indicating the environment is active.

---

## Installation

### Step 3 — Install dependencies

Create a `requirements.txt` file in the project root with the following content:

```
numpy
pandas
matplotlib
scikit-learn
```

Then install all dependencies:

```bash
pip install -r requirements.txt
```

To verify the key packages are installed:

```bash
pip show scikit-learn pandas numpy matplotlib
```

---

## Running the Project

### Step 4 — Add the dataset

Download `insurance.csv` and place it inside a folder named `data/` in the project root:

```
insurance-charges-predictor/
└── data/
    └── insurance.csv   ✅
```

### Step 5 — Run the training script

```bash
python main.py
```

> On some systems, use `python3` instead of `python`.

---

## Output

When the script runs successfully, you will see:

```
Accuracy : 74.52%       ← R² score on the test set (value will vary slightly)
```

A trained model file will also be saved to the project root:

```
model.pkl               ← Serialized Linear Regression model (ready for inference)
```

---

## Model Evaluation

The model is evaluated using the **R² (coefficient of determination)** score on a held-out test set (20% of the data). An R² of ~0.74 means the model explains approximately 74% of the variance in insurance charges.

| Metric | Description |
|--------|-------------|
| R²     | Proportion of variance explained by the model |
| Train/Test Split | 80% training / 20% testing |

For more rigorous evaluation, consider adding:
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **K-Fold Cross-Validation**

---

## Extending the Project

Here are some ways to build on this baseline:

- **Add regularization** — Try `Ridge` or `Lasso` regression to reduce overfitting
- **Feature engineering** — Create interaction terms (e.g., `bmi × smoker`)
- **EDA** — Add exploratory plots to visualize feature distributions and correlations
- **Inference script** — Load `model.pkl` and predict charges for new inputs
- **Web API** — Wrap the model in a Flask or FastAPI endpoint for real-time predictions

---

## Troubleshooting

| Problem | Solution |
|--------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` with the venv active |
| `FileNotFoundError: insurance.csv` | Ensure the file is placed inside a `data/` subfolder |
| `python` command not found | Try `python3` instead, or check your Python installation |
| Permission error on Windows (venv) | Run PowerShell as Administrator or use `Set-ExecutionPolicy RemoteSigned` |

---

## License

This project is intended for educational purposes. The dataset is sourced from Kaggle under its respective license.
