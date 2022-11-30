import math

import pymysql
import pyupbit
from django.shortcuts import render, redirect


# Create your views here.

from .auto_connect import loginid_select, trade_list_selete
from chart.views import getkey, abc_access, abc_secret

def main_index(request):
    loginid_select(request) #자동매매 사용 중인지 확인
    id = loginid_select(request)

    #잔고 조회
    test1 = getkey(request)
    access_key=test1[1]
    secret_key=test1[2]
    upbit = pyupbit.Upbit(access_key, secret_key)

    btc_balance = upbit.get_balance("KRW-BTC")  # 비트코인 갯수 조회
    btc_price = pyupbit.get_current_price("KRW-BTC")    #비트 코인 현재가격 조회
    btc = btc_balance * btc_price # 갯수 * 현재가격

    krw = upbit.get_balance("KRW")  # 비트코인 + 현금

    balance = krw + btc
    balance = format(math.floor(balance), ',')

    trade_list = trade_list_selete(request)
    return render(request, 'autotrading/index.html', {'id': id, 'trade_list': trade_list, 'balance': balance})


# key 전역 변수 선언
abc_access = ""
abc_secret = ""


def inserkey(request):


    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    login_id = request.user
    try:    
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()

        sql = "INSERT INTO abcbit.autotrading_autotrade(member_id, member_access_key, member_secret_key) SELECT id, access_key, secret_key FROM abcbit.users_user" + " WHERE id = %s"
        curs.execute(sql, login_id)

        result = curs.fetchall()


    finally:
        conn.commit()
        curs.close()
        conn.close()
        return redirect('main')
