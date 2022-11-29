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
    writeToScreen('<span style=color:'+ color +'>' + data.tp + '</span>', data.cd+'_price');
    if (document.getElementById(data.cd+'_main_price')!= null){
        eventwriteToScreen('<span style=color:'+ color +'>' + data.tp + '</span>',data.cd+'_main_price');
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

window.addEventListener("load", init, false);