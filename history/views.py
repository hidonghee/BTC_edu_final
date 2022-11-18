import json

from django.shortcuts import render

import pyupbit
import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
# Create your views here.
from django.http import HttpResponse


def main_index(request):
    access = "jBdjuqbXRPYQweMUV9vq4IVLSxQpZHyosz82RKy4"  # 본인 값으로 변경
    secret = "ipdCj7ioQUexC0Haai9YtRjDrHfh9VZxdKaI2ehx"  # 본인 값으로 변경
    upbit = pyupbit.Upbit(access, secret)
    krw = upbit.get_balance()
    my_balance = upbit.get_balances()

    # print(my_balance[1]['currency'])
    # print(coin[1]['currency'])

    return render(request, 'history/index.html', {'my_balance':my_balance,'krw':krw})

    # return HttpResponse("장고 잔고조회, 거래내역 조회 앱 입니다.")