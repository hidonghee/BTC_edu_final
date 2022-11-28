
/*
* 코인별 차트 make js
* 내용:
* default onload: 종목은 비트코인 기본 onload, 차트는 기본적으로 1일이 먼저 표기
*
* */
window.onload = coin_chart("KRW-BTC")

function coin_chart(coin_name) {
    var dps1 = [], dps2 = [];
    var stockChart = new CanvasJS.StockChart("chartContainer", {
        theme: "light2",
        title: {
            text: "Technical Indicators: MACD"
        },
        subtitles: [{
            text: "Moving Average Convergence Divergence"
        }],
        charts: [{
            legend: {
                verticalAlign: "top",
                horizontalAlign: "left"
            },
            axisX: {
                tickLength: 0,
                lineThickness: 5,
                labelFormatter: function (e) {
                    return "";
                }
            },
            axisY: {
                prefix: "$"
            },
            data: [{
                color: "blue",
                risingColor: "red",
                type: "candlestick",
                name: "Stock Price",
                yValueFormatString: "$#,###.##",
                dataPoints: dps1
            }],
        }],
        navigator: {
            animationEnabled: true,
            dynamicUpdate: true,
            slider: {
                maskColor: "gray",
                outlineColor: "blue",
                outlineThickness: 2,
                maskOpacity: 0.3,
                minimum: new Date(2018, 03, 01),
                maximum: new Date(2018, 05, 01)
            }
        }
    });
    updateData();

    function addData(data) {
        for (var i = 0; i < data.length; i++) {
            if (Number(data[i].trade_price) - Number(data[i].opening_price) > 0) {
                var color = "red"
            } else {
                var color = "blue"
            }
            dps1.push({
                x: new Date(data[i].candle_date_time_kst),
                y: [Number(data[i].opening_price), Number(data[i].high_price), Number(data[i].low_price), Number(data[i].trade_price)],
                color: color
            });
        }
        stockChart.render();
        //setTimeout(updateData, 3500);
    }

    function updateData() {
        $.getJSON("https://api.upbit.com/v1/candles/days?market="+coin_name+"&count=200", addData)
    }

}