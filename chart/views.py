import asyncio

from django.shortcuts import render
import asyncio
import chart.ticker
# Create your views here.
from django.http import HttpResponse


def main_index(request):
    return render(request, 'chart/index.html' )
    # return HttpResponse("장고 chart 앱 입니다.")
