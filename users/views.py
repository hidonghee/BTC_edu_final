from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from users.models import User
import cryptocode


def main_index(request):
    return render(request, 'users/index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                id=request.POST['userid'],
                password=make_password(request.POST['password1']),
                name=request.POST['username'],
                email=request.POST['email'],
                sex=request.POST['sex'],
                addr=request.POST['addr'],
                access_key=request.POST['access_key'],
                secret_key=request.POST['secret_key']
            )
            key = "abcbit"
            print("암호화 전2", user.secret_key)
            user.secret_key = cryptocode.encrypt(user.secret_key, key)
            print("암호화 후", user.secret_key)
            # user.password(make_password(user.password))
            # user.set_password(user.password)
            user.save()
            # auth.login(request, user)
            return redirect('/')
        return render(request, 'users/signup.html')
    return render(request, 'users/signup.html')
