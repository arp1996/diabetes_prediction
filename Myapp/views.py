from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

        if request.method=='POST':
                glucose=request.POST['RestingBP']
                blood_pressure=request.POST['Cholesterol']
                skin_thickness=request.POST['FastingBS']
                insulin=request.POST['MaxHR']
                bmi=request.POST['Oldpeak']

        lis=[glucose,blood_pressure,skin_thickness,insulin,bmi] 
        print(lis)

        #training model
        from joblib import load
        model=load(r'C:\Users\ADMIN\Desktop\djangopro2\model.joblib')

        #make prediction
        result=model.predict([lis])
        print(result)

        if result[0]==0:
                print("No")
                value='Negative' 
        else:
                print("Yes")
                value='Positive'

        return render (request,'result.html', {
                'ans':value,
                'title':'Predict',
        }  )
