/*
웹소켓은 해당 종목에 대한 atp(누적금액)이 변경되었을 해당 종목을 수신, 발신할 수 있다.
 */

var wsUri = "wss://api.upbit.com/websocket/v1";

// var strong;

//  현재가 init
function init() {
    // strong = document.getElementById("coin_strong");

    testWebSocket();
}


function testWebSocket() {
    websocket = new WebSocket(wsUri);
    websocket.binaryType = 'arraybuffer';
    //websocket.binaryType = 'Blob';
    //websocket.binaryType = 'String';
    websocket.onopen = function (evt) {
        onOpen(evt);
    };
    websocket.onmessage = function (evt) {
        onMessage(evt)
    };
    websocket.onerror = function (evt) {
        onError(evt)
    };
}

function onOpen(evt) {
    //writeToScreen("연결완료");
    //console.log(test);
    var msg = [
        {"ticket": "test"},
        {
            "type": "ticker",
            "codes": coin_list.split(',') ,
            "isOnlyRealtime": true
        },
        {"format": "SIMPLE"}
    ]

    msg = JSON.stringify(msg);
    //console.log(msg);
    doSend(msg);
}

function onMessage(evt) {
    var enc = new TextDecoder("utf-8");
    var arr = new Uint8Array(evt.data);
    //console.log(enc.decode(arr));
    var data = JSON.parse(enc.decode(arr));

    // color select
    var color;
    if (data.c == 'FALL'){color = '#1261c4'}
    else if (data.c == 'RISE'){color = '#c84a31'}
    else if(data.c == 'EVEN') {color = '#4f555a'}
    // notification fadeout
    notification(data.cd+'_current',data,color)
    //writeToScreen('<span id='+data.cd+'_current style=color:'+color+'>'+data.tp+'</span>', data.cd+'_price');
    if (document.getElementById(data.cd+'_main_price')!= null){
        eventwriteToScreen('<span style=color:'+ color +'>' + Number(data.tp).toLocaleString('ko-KR') + '</span>',data.cd+'_main_price');
    }
}

function onError(evt) {
    test_writeToScreen('<span style="color: red;">에러:</span> ' + evt.data);
}

function doSend(message) {
    //writeToScreen("발신: " + message);
    websocket.send(message);
}

// 동작확인용 output
function test_writeToScreen(message) {
    var pre = document.getElementById("coin_strong");
    pre.innerHTML = message;
}

// message 인자는 응답.
function writeToScreen(message, htmlid) {
    var pre = document.getElementById(htmlid);
    pre.innerHTML = message;
}
function eventwriteToScreen(message, htmlid){
    var main_price2 = document.getElementById(htmlid);
    main_price2.innerHTML = message;
}
function notification(htmlid,data,color) {
    var current = document.getElementById(htmlid).innerText;
    current = current.replace(/,/g,"")
    if(data.tp > current){
        writeToScreen('<span class="ticker_notification_up" id='+data.cd+'_current style=color:'+color+'>'+Number(data.tp).toLocaleString('ko-KR')+'</span>', data.cd+'_price');
    }else if(data.tp < current){
        writeToScreen('<span class="ticker_notification_down" id='+data.cd+'_current style=color:'+color+'>'+Number(data.tp).toLocaleString('ko-KR')+'</span>', data.cd+'_price');
    }
}

window.addEventListener("load", init, false);