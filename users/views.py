from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main_index(request):
    return render(request , 'users/index.html')
    return HttpResponse("장고 로그인/로그아웃/회원가입 앱 입니다.")
