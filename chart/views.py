import asyncio
import json

import cryptocode
import pymysql
import pyupbit
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# key값 전역 변수 선언
abc_access = ""
abc_secret = ""
upbit = pyupbit.Upbit(abc_access, abc_secret)


# DB에서 KEY 꺼내서 복호화해서 전역변수에 넣어줌
def getkey(request):
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    login_id = request.user
    print("유저아이디값:", login_id)
    try:
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()

        sql = "SELECT access_key,secret_key FROM abcbit.users_user" + " WHERE id = %s"
        curs.execute(sql, login_id)
        result = curs.fetchall()
        print("아이디", login_id)
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
    getkey(request)  # 로그인한 ID의 키값 넣어줌

    # 라이브러리 선언
    upbit = pyupbit.Upbit(abc_access, abc_secret)
    krw = upbit.get_balance()  # 현금 조회
    my_balance = upbit.get_balances()  # 코인 조회
    print(type(my_balance))
    # print("파싱전 코인양", my_balance.currency)

    coinlist = []
    for i in my_balance:
        row = {'coin_name': i['currency'],
               'balance': i['balance'],
               'avg': i['avg_buy_price']
               }
        coinlist.append(row)
    print(coinlist)

    # 코인 리스트 가져오기
    kind = "KRW"
    ver_ticker = ticker_list(kind, True)
    nor_ticker = ','.join([str(i) for i in list(ticker_list(kind, False))])
    return render(request, 'chart/index.html', {'my_balance': my_balance, 'krw': krw, 'coinlist': coinlist, 'ver_ticker': ver_ticker, 'nor_ticker': nor_ticker})
    # return HttpResponse("장고 chart 앱 입니다.")


# 매수 매도 주문
def trade(request):
    getkey(request)
    upbit = pyupbit.Upbit(abc_access, abc_secret)
    print("매수매도 키", abc_access)
    print("매수매도 키", abc_secret)
    print("요청값", request.POST['side'])
    if request.POST['side'] == 'bid':
        side = request.POST['side']
        market = request.POST['market']
        volume = request.POST['volume']
        print(market, volume, side)
        res = upbit.buy_market_order(market, volume)
        print(res)
        return HttpResponseRedirect("/chart")

    elif request.POST['side'] == 'ask':
        print("판매 들어옴")
        market = request.POST['market']
        volume = request.POST['volume']
        res = upbit.sell_market_order(market, volume)
        print(res)
        return HttpResponseRedirect("/chart")
    return HttpResponseRedirect("/chart")


# 종목 조회
def ticker_list(kind, verbose):
    # verbose = True하면 market, korean_name, english_name이 출력
    # false하면 market만 list로 출력됨.
    tickers = pyupbit.get_tickers(kind, verbose=verbose)
    return tickers
