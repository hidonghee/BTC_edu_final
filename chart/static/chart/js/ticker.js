var wsUri = "wss://api.upbit.com/websocket/v1";

var strong;

//  현재가 init
function init() {
    strong = document.getElementById("coin_strong");
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
    var msg = [
        {"ticket": "test"},
        {
            "type": "ticker",
            "codes": ["KRW-BTC"],
            "isOnlyRealtime": true
        },
        {"format": "SIMPLE"}
    ]
    msg = JSON.stringify(msg);
    doSend(msg);
}

function onMessage(evt) {
    var enc = new TextDecoder("utf-8");
    var arr = new Uint8Array(evt.data);
    //console.log(enc.decode(arr));
    var data = JSON.parse(enc.decode(arr));
    writeToScreen('<span style="color: blue;">' + data.tp + '</span>');
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
function writeToScreen(message) {
    var pre = document.getElementById("coin_strong");
    pre.innerHTML = message;
};

window.addEventListener("load", init, false);


