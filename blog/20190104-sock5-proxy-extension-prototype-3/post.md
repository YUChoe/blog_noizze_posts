
기존 `prototype goal`에서 이제 `on/off 상태를 아이콘으로 구별 할 수 있을 것` 이 남았다. 

회색 기반의 off 아이콘 하고 색이 있는 on 아이콘 두가지와 웹스토어에 게시 될 메인 아이콘을 만들어서 넣고 

```
noizze@DESKTOP ~/extension_prototype/libs/img $ ls icon*
icon_off_16.png  icon_on_16.png  icon_128.png
```
manifest에 다음과 같이 정의

```js
"icons": {
      "128": "libs/img/icon_128.png",
      "16": "libs/img/icon_off_16.png"
    }
```

그리고 기존에 localStorage 에서 on/off 상태를 저장하고 확인하던 곳에 다음과 같이 `show_on()`, `show_off()` 실행을 추가 

```js
if (localStorage.__onoff_status == "on") {
    $("#onoff_switch").attr("checked", true);
    Popup.show_ON_icon();
} else {
    $("#onoff_switch").attr("checked", false);
    Popup.show_OFF_icon();
}
```

각각에 대해 정의

```js
Popup.show_ON_icon = function() {
    var on_icon = { path: 'libs/img/icon_on_16.png' };
    chrome.browserAction.setIcon(on_icon);
}

Popup.show_OFF_icon = function() {
	var off_icon = { path: 'libs/img/icon_off_16.png' };
    chrome.browserAction.setIcon(on_icon);
}
```

테스트 해 보니 잘 된다. 