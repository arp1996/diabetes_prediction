# Heart Disease Prediction

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Therazerhub/diabetes)

A Django web app that predicts heart disease risk using an SVM machine learning model.

**Live demo:** https://diabetes-prediction.onrender.com (after deploying)

## Features

- **User authentication** — Register, login, and logout
- **Heart disease prediction** — Enter RestingBP, Cholesterol, FastingBS, MaxHR, and Oldpeak
- **SVM model** — Trained on heart disease dataset with ~85% accuracy
- **PostgreSQL** — Production-ready database on Render
- **Responsive UI** — Bootstrap-based, works on mobile and desktop

## How it works

1. Create an account
2. Log in
3. Enter your health metrics
4. Get a **Positive** or **Negative** prediction

## Tech stack

- **Django 6.0** — Python web framework
- **scikit-learn** — SVM classifier
- **joblib** — Model serialization
- **SQLite** (dev) / **PostgreSQL** (production)
- **Gunicorn** — WSGI server
- **Render** — Cloud deployment

## Run locally

```bash
git clone https://github.com/Therazerhub/diabetes.git
cd diabetes
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit **http://localhost:8000**

## Deploy to Render

Click the **Deploy to Render** button above, or:

1. Push this repo to GitHub
2. Go to [dashboard.render.com](https://dashboard.render.com)
3. Click **New → Blueprint**
4. Connect your repo
5. Render auto-detects `render.yaml` and sets everything up

## Dataset

The model was trained on the [Heart Disease Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) from Kaggle (5 features: RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak).

## License

MIT
