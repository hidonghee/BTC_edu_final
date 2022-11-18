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
    access = "zNoKwaKvzaxoQl9c8AuVSOoKAXPAK4dG3LdCvPvP"  # 본인 값으로 변경
    secret = "Ew8TtCScDYGV5QTOexlhTeoptob0RSCixm32iTr9"  # 본인 값으로 변경
    upbit = pyupbit.Upbit(access, secret)

    krw = upbit.get_balance()
    my_balance = upbit.get_balances()
    # print(my_balance)
    print(upbit.get_order(["KRW-DOGE", "KRW-BTC"], state="done"))
    return render(request, 'history/index.html', {'my_balance': my_balance, 'krw': krw})

    # return HttpResponse("장고 잔고조회, 거래내역 조회 앱 입니다.")
