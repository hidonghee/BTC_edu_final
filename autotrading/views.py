import pymysql
from django.shortcuts import render, redirect

# Create your views here.

from chart.views import getkey


def main_index(request):
    return render(request, 'autotrading/index.html')


# key 전역 변수 선언
abc_access = ""
abc_secret = ""

def inserkey(request):
    print("함수 호출")
    print(request.user)
    ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
    dbname = "abcbit"
    username = "master"
    passwd = "qwer1234"
    login_id = request.user
    try:    
        conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
        curs = conn.cursor()
        print("login_id",login_id)
        sql = "INSERT INTO abcbit.autotrading_autotrade(member_id, member_access_key, member_secret_key) SELECT id, access_key, secret_key FROM abcbit.users_user" + " WHERE id = %s"
        curs.execute(sql, login_id)
        print("sql", sql)
        print("curs", curs)
        result = curs.fetchall()
        print(result)

        # abc = []
        # for key in result:
        #     row = {"access_key": key[0],
        #            "secret_key": key[1]}
        #     abc.append(row)
        #
        # global abc_access
        # abc_access = abc[0]['access_key']
        # global abc_secret
        # key = "abcbit"
        # abc_secret = cryptocode.decrypt(abc[0]['secret_key'], key)

    finally:
        conn.commit()
        curs.close()
        conn.close()
        return render(request, 'autotrading/index.html')

# def insertkey(request):
#     getkey(request)
#     ip = "abctest.cluster-czgliwfs2orh.ap-northeast-2.rds.amazonaws.com"
#     dbname = "abcbit"
#     username = "master"
#     passwd = "qwer1234"
#     login_id = request.user
#     print("유저아이디값:", login_id)
#     try:
#         conn = pymysql.connect(host=ip, user=username, password=passwd, db=dbname, use_unicode=True, charset='utf8')
#         curs = conn.cursor()
#
#         sql = "SELECT access_key,secret_key FROM abcbit.users_user" + " WHERE id = %s"
#         curs.execute(sql, login_id)
#         result = curs.fetchall()
#         print("아이디", login_id)
#         abc = []
#         for key in result:
#             row = {"access_key": key[0],
#                    "secret_key": key[1]}
#             abc.append(row)
#
#         global abc_access
#         abc_access = abc[0]['access_key']
#         global abc_secret
#         key = "abcbit"
#         abc_secret = cryptocode.decrypt(abc[0]['secret_key'], key)
#
#     finally:
#         curs.close()
#         conn.close()
#         return request