import upbit as upbit
from django.shortcuts import render, redirect
import pyupbit
from history.views import abc_access, abc_secret, getdata
# Create your views here.
from django.http import HttpResponse

access = "###"  # 본인 값으로 변경
secret = "###"  # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


def main_index(request):
    return render(request, 'chart/index.html')


# return HttpResponse("장고 거래, 주문 앱 입니다.")

def trade(request):
    print("요청값", request.POST['side'])
    if request.POST['side'] == 'bid' :
        side = request.POST['side']
        market = request.POST['market']
        volume = request.POST['volume']
        print(market, volume, side)
        res = upbit.buy_market_order(market, volume)
        print(res)
        return redirect('chart/index.html')

    elif request.POST['side'] == 'ask' :
        print("판매 들어옴")
        market = request.POST['market']
        volume = request.POST['volume']
        res = upbit.sell_market_order(market, volume)
        print(res)
        return redirect('chart/index.html')
    return redirect('chart/index.html')
