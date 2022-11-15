from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_index(request):
    return render(request, 'homepage/index.html')
    #return HttpResponse("장고 메인페이지 앱 입니다.")
