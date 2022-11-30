import datetime
import math
from urllib import request

import pymysql

# 서비스 사용중인지 확인용
from django.shortcuts import redirect
from django.urls import reverse


def loginid_select(request):
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    try:
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()
        sql = "SELECT member_id FROM abcbit.autotrading_autotrade" + " WHERE member_id = %s"
        curs.execute(sql, request.user)
        result = curs.fetchall()
        print("결과", result)

        if len(result) != 0:
            abc = []
            for key in result:
                row = {"id": key[0]}
                abc.append(row)
                autotrad_id = abc[0]['id']
        else:
            autotrad_id = ""

    finally:
        curs.close()
        conn.close()
    return autotrad_id


# 자동매매 서비스 사용 중지
def stop_autotrade(request):
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"

    try:
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()
        sql = "DELETE FROM abcbit.autotrading_autotrade WHERE member_id = %s"
        curs.execute(sql, request.user)
        result = curs.fetchall()
        print("결과", result)

    finally:
        conn.commit()
        curs.close()
        conn.close()
    return redirect('main')


# 자동매매 거래 리스트 가져오기
def trade_list_selete(request):
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    try:
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()
        sql = "SELECT member_id, side, price, created, volume FROM abcbit.autotrading_autotrade_list" + " WHERE member_id = %s ORDER BY created DESC"
        curs.execute(sql, request.user)
        result = curs.fetchall()
        # print("결과", result)
        autotrade_list = []
        print("파싱 전 데이터", result)
        if len(result) != 0:

            for key in result:
                date_format = '%Y-%m-%dT%H:%M:%S'
                if key[2] == None:
                    row = {"id": key[0],
                           "side": key[1],
                           "price": key[2],
                           "created": datetime.datetime.strptime(key[3][0:19], date_format),
                           "volume": key[4]
                           }
                    autotrade_list.append(row)
                elif key[2] is not None:
                    row = {"id": key[0],
                           "side": key[1],
                           "price": format(math.floor(float(key[2])), ','),
                           "created": datetime.datetime.strptime(key[3][0:19], date_format),
                           "volume": key[4]
                           }
                    autotrade_list.append(row)
            print("파싱 후 데이터", autotrade_list)

    finally:
        curs.close()
        conn.close()
    return autotrade_list
