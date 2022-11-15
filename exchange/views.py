from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main_index(request):
    return render(request, 'exchange/index.html')
# return HttpResponse("장고 거래, 주문 앱 입니다.")
