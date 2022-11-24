import json

# from django.contrib.auth.models import User
import cryptocode
import pymysql
from django.contrib.messages.storage import session
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

from users.models import User

abc_access = ""
abc_secret = ""


def getdata(request, sql):
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    login_id = request.user
    try:
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()

        sql = "SELECT access_key,secret_key FROM abcbit.users_user" + " WHERE id = %s"
        curs.execute(sql, login_id)
        result = curs.fetchall()

        abc = []
        for key in result:
            row = {"access_key": key[0],
                   "secret_key": key[1]}
            abc.append(row)

        global abc_access
        abc_access = abc[0]['access_key']
        global abc_secret
        key = "abcbit"
        abc_secret = cryptocode.decrypt(abc[0]['secret_key'], key)

    finally:
        curs.close()
        conn.close()
        return request


def main_index(request):
    getdata(request)  # DB에서 키 가져오기

    print(abc_access)
    print(abc_secret)

    upbit = pyupbit.Upbit(abc_access, abc_secret)

    krw = upbit.get_balance()  # 현금 조회
    my_balance = upbit.get_balances()  # 코인 조회

    print(upbit.get_order(["KRW-DOGE", "KRW-BTC"], state="done"))

    return render(request, 'history/index.html', {'my_balance': my_balance, 'krw': krw})
