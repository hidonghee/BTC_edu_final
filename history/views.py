from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_index(request):
    return render(request, 'history/index.html')
    # return HttpResponse("장고 잔고조회, 거래내역 조회 앱 입니다.")