from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from users.models import User


def main_index(request):
    return render(request, 'users/index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                id=request.POST['userid'],
                password=request.POST['password1'],
                name=request.POST['username'],
                email=request.POST['email'],
                sex=request.POST['sex'],
                addr=request.POST['addr'],
                access_key=request.POST['access_key'],
                secret_key=request.POST['secret_key']
            )
            user.set_password(user.password)
            user.save()
            # auth.login(request, user)
            return redirect('/')
        return render(request, 'users/signup.html')
    return render(request, 'users/signup.html')