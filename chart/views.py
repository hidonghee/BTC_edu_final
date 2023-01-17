import asyncio
import json
import math

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
    ip = "###"
    dbname = "###"
    username = "###"
    passwd = "###"
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
        return request, abc_access, abc_secret


def main_index(request):
    getkey(request)  # 로그인한 ID의 키값 넣어줌
    # 라이브러리 선언
    upbit = pyupbit.Upbit(abc_access, abc_secret)
    krw = format(math.floor(upbit.get_balance()), ',')  # 현금 조회
    my_balance = upbit.get_balances()  # 코인 조회

    # print("파싱전 코인양", my_balance.currency)

    coinlist = []
    for i in my_balance:

        if i['avg_buy_price'] != "0":
            row = {'coin_name': i['currency'],
                   'balance': i['balance'],
                   'avg': format(math.floor(int(i['avg_buy_price'])), ',')
                   }
            coinlist.append(row)

    # 코인 리스트 가져오기
    kind = "KRW"
    ver_ticker = ticker_list(kind, True)
    nor_ticker = ','.join([str(i) for i in list(ticker_list(kind, False))])  # norticker는 웹소켓에 보내줄 array 형식에 필요함.

    # 현재가 restapi로 일시적으로 불러오기
    trade_price = pyupbit.get_current_price(ticker_list(kind, False), verbose=True)
    for i in range(len(ver_ticker)):
        trade_price[i]["korean_name"] = ver_ticker[i]["korean_name"]
    return render(request, 'chart/index.html',
                  {'my_balance': my_balance, 'krw': krw, 'coinlist': coinlist, 'nor_ticker': nor_ticker,
                   'trade_price': trade_price})

    # return HttpResponse("장고 chart 앱 입니다.")


# 매수 매도 주문
def trade(request):
    getkey(request)
    upbit = pyupbit.Upbit(abc_access, abc_secret)

    if request.POST['side'] == 'bid':
        side = request.POST['side']
        market = request.POST['market']
        volume = request.POST['volume']
        res = upbit.buy_market_order(market, volume)
        return HttpResponseRedirect("/chart")

    elif request.POST['side'] == 'ask':

        market = request.POST['market']
        volume = request.POST['volume']
        res = upbit.sell_market_order(market, volume)

        return HttpResponseRedirect("/chart")
    return HttpResponseRedirect("/chart")


# 종목 조회
def ticker_list(kind, verbose):
    # verbose = True하면 market, korean_name, english_name이 출력
    # false하면 market만 list로 출력됨.
    tickers = pyupbit.get_tickers(kind, verbose=verbose)
    return tickers
