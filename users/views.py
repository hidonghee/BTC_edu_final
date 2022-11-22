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


# 새로 로그인 로직
# def login(request):
#     response_data = []
#
#     if request.method == "GET":
#         return render(request, 'users/login.html')
#
#     elif request.method == "POST":
#         login_username = request.POST.get('username', None)
#         login_password = request.POST.get('password', None)
#         print("로그인 정보", login_username, login_password)
#         if not (login_username and login_password):
#             response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
#         else:
#             user = User.objects.get(id=login_username)
#             print("꺼내온 데이터 확인",user.password)
#             # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
#             if check_password(login_password, user.password):
#                 print("비밀번호 같은지 확인", login_password)
#                 print("비밀번호 같은지 확인",user.password)
#                 request.session['user'] = User.id
#                 # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
#                 # 세션 user라는 key에 방금 로그인한 id를 저장한것.
#                 print("비밀 번호 로직 통과")
#                 return redirect('/index.html')
#             else:
#                 print("비밀 번호 틀림")
#                 response_data['error'] = "비밀번호를 틀렸습니다."
#         print("응답값", response_data)
#         return render(request, 'users/login.html', response_data)
#
#
# def logout(request):
#     request.session.pop('user')
#     return redirect('/')
