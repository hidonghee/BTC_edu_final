
/*
* 코인별 차트 make js
* 내용:
* default onload: 종목은 비트코인 기본 onload, 차트는 기본적으로 1일이 먼저 표기
*
* */

window.onload = coin_chart("KRW-BTC",document.getElementById("KRW-BTC_main_price"),document.getElementById("KRW-BTC_main_price").style.color);

function coin_chart(coin_name, price, change) {
    var dps1 = [], dps2 = [];
    var stockChart = new CanvasJS.StockChart("chartContainer", {
        theme: "light2",
        title: {
            text: "ABCbit Coin Chart",
            fontColor: "#000f4b",
            fontSize: 25,
            fontFamily: "tahoma",
            fontWeight: "bold",
            padding: 15,
        },
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
    list_main_event();

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
    function list_main_event(){
        var main_name, main_price;
        var temp_kr;
        // name
        main_name = document.getElementById("main_name");
        temp_kr = document.getElementById(coin_name+'_kr').innerText;
        main_name.innerText = temp_kr +'/' + coin_name;
        //price
        var color = change;
        if (color == 'RISE'){color = '#c84a31'}
        else if (color == 'FALL'){color = '#1261c4'}
        else if (color == 'EVEN') {color = '#4f555a'}
        else {color = change}
        main_price = document.getElementById("main_price");
        main_price.innerHTML = '<span id='+coin_name+'_main_price'+' style=color:'+color+'>'+price+'</span>'
    }

}

