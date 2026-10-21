# Customer Churn Prediction

An end-to-end machine learning application that predicts whether a telecom customer is likely to churn. It includes a trained scikit-learn model (~84% ROC-AUC), a Flask API, and a React frontend with an Apple-inspired UI. The whole app is containerized with Docker and deployed on Render.


---

## Features

- Predicts churn probability from customer details
- Model trained and evaluated in a Jupyter notebook (ROC-AUC ≈ 0.84)
- Flask REST API serving the trained model
- React + Vite frontend with a clean, Apple-inspired design
- Dockerized for consistent builds and easy deployment
- Deployed on Render

---

## Tech Stack

| Layer | Technologies |
|-------|--------------|
| **ML** | Python, scikit-learn, pandas, NumPy |
| **Backend** | Flask |
| **Frontend** | React, Vite |
| **DevOps** | Docker, Docker Compose, Render |

---

## Project Structure

```
customer-churn-prediction-ML-/
├── backend/             # Flask API
├── frontend/            # React + Vite app
├── dataset/             # Training data
├── model/               # Saved trained model
├── notebook/            # EDA and model training notebook
├── src/                 # Training / preprocessing code
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── .dockerignore
```

---

## Model

- **Problem:** Binary classification (churn vs. no churn)
- **Dataset:** [name the dataset, e.g. Telco Customer Churn]
- **Algorithm:** [e.g. Random Forest / Logistic Regression]
- **Preprocessing:** [e.g. encoding categorical features, scaling, handling class imbalance]
- **Performance:** ROC-AUC ≈ **0.84**

See the `notebook/` folder for the full exploration and training workflow.

---

## Getting Started

### Option 1: Run with Docker (recommended)

```bash
git clone https://github.com/Deadly-ms/customer-churn-prediction-ML-.git
cd customer-churn-prediction-ML-
cp .env.example .env
docker-compose up --build
```

The app will be available at `http://localhost:[port]`.

### Option 2: Run locally

**Backend**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

```env
[VARIABLE_NAME]=your_value
```

---

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/predict` | Returns churn prediction and probability for the given customer data |

**Example request**
```json
{
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "Contract": "Month-to-month"
}
```

**Example response**
```json
{
  "prediction": "Churn",
  "probability": 0.78
}
```

---

## Deployment

The app is containerized with Docker and deployed on [Render](https://render.com) using the provided `Dockerfile`.

## Author

**Sriram**
- GitHub: [@Deadly-ms](https://github.com/Deadly-ms)
- LinkedIn: [sriram-s-12b80626b](https://linkedin.com/in/sriram-s-12b80626b)
- Email: minisriram8@gmail.com
