from pathlib import Path

import joblib
import pandas as pd
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from sklearn.svm import SVC

from .forms import RegisterForm


def _load_model():
    model_path = Path(__file__).resolve().parent / "model.joblib"
    if model_path.exists():
        return joblib.load(model_path)

    df = pd.read_csv(Path(__file__).resolve().parent / "heart.csv")
    X = df[["RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]]
    y = df["HeartDisease"]

    model = SVC()
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model


def register(request):
        if request.method == 'POST':
           form =RegisterForm(request.POST)
           if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_view')
        else:
           form = RegisterForm()
        return render(request, 'register.html', {'form' : form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('predict')
    else:
            form = AuthenticationForm()
    return render(request, 'login.html',{'form' : form})

def logout1(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')
    
# Create your views here.
def index(request):
    		
        return render(request,'index.html')

def about(request):
    		
            return render(request,'about.html')
def predict(request):
    		
            return render(request,'predict.html')
def result(request):
    if request.method == 'POST':
        values = [
            float(request.POST.get('RestingBP', 0)),
            float(request.POST.get('Cholesterol', 0)),
            float(request.POST.get('FastingBS', 0)),
            float(request.POST.get('MaxHR', 0)),
            float(request.POST.get('Oldpeak', 0)),
        ]

        model = _load_model()
        feature_frame = pd.DataFrame([values], columns=["RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"])
        prediction = int(model.predict(feature_frame)[0])
        value = 'Positive' if prediction == 1 else 'Negative'

        return render(request, 'result.html', {
            'ans': value,
            'title': 'Predict',
        })

    return redirect('predict')
