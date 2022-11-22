"""
pip install pyupbit
pip install dash

"""
import dash
from dash import dcc
from dash import html
import datetime
import pyupbit
import pandas as pd
import plotly.graph_objects as go


# 여기서 모든  캔들 함수는 데이터프레임 타입!

# 최대 200개
# 분봉
# minute 변수에는 1,3,5,10,30,60이 가능하고 반드시 문자열로 사용!
def minute_candle(market, minute, count):
    default = 'minute'
    minutef = pyupbit.get_ohlcv(market, default + minute, count)
    minutef = __chart_data_edit(minutef)
    return minutef


# 최대 200개
# 일봉(Day) 조회
def day_candle(market, count):
    dayf = pyupbit.get_ohlcv(market, 'day', count)
    dayf = __chart_data_edit(dayf)
    return dayf


# 최대 200개
# 주봉(Week) 조회
def week_candle(market, count):
    weekf = pyupbit.get_ohlcv(market, "week", count)
    weekf = __chart_data_edit(weekf)
    return weekf


# 최대 200개
# 월봉(Month)조회
def month_candle(market, count):
    monthf = pyupbit.get_ohlcv(market, "month", count)
    monthf = __chart_data_edit(monthf)
    return monthf


# 데이터프레임 처리
# 지역함수
def __chart_data_edit(data):
    df = data.drop(['value'], axis=1)
    df = df.reset_index()
    df = df.rename(columns={'index': 'date'})
    return df

# 사용하지 않는 차트임!!!
# def make_chart(coin_df,coin_name) :
#   data = [{
#       'type': 'candlestick',
#       'x': coin_df.date,
#       'open': coin_df.open,
#       'close': coin_df.close,
#       'high': coin_df.high,
#       'low': coin_df.low,
#       'name': coin_name,
#       'increasing_line_color': 'red', # 양봉 색상
#       'decreasing_line_color': '#398bff', # 음봉 색상
#       'showlegend': True
#     },]
#   for (window, color) in [(5, '#00c50d'), (20, '#ff333a'), (60, '#f48416'),
#                         (120, '#892dff')]:
#     MA = coin_df.close.rolling(window=window, min_periods=1).mean()
#     trace = {
#         'x': coin_df.date,
#         'y': MA,
#         'type': 'scatter',
#         'mode': 'lines',
#         'line': {
#             'width': 1,
#             'color': color
#         },
#         'name': '{} 이동평균선'.format(window)
#     }
#     data.append(trace)
#   return data
#
# def chart_layout(coin_name) :
#   title = '{} 차트'.format(coin_name)
#   layout = go.Layout({
#       'title': {
#           'text': title,
#           'font': {
#               'size': 11
#           }
#       }
#   })
#   return layout
