
이 전 포스트에 **prototype goal**이 다음의 3가지라고 정했다.

* 특정 socks5 서버에 접속
* 팝업을 통해 on/off 시킬 수 있을 것
* on/off 상태를 아이콘으로 구별 할 수 있을 것 

이 중 '특정 sock5 서버에 접속`은 구현이 가능 했고, 다음을 어떻게 할 것인가를 생각 해봤다. 

### OFF 를 어떻게 할 것인가?
여러번 프록시 서버를 꺼 놓고 개발과 테스트를 하다보니, extension을 disabled 나 삭제하지 않는 이상은 *상태가 유지(프록시 ON)* 되어, 사이트 접속할 수 없습니다. 메시지를 볼 수 있었다. OFF 하는 방법은 2가지가 있을 수 있을텐데.

1. ON하기 이전 설정으로 돌아가기.
2. 시스템 설정을 사용하기

이 둘 중에서 1번으로 하면 정확하겠지만, 2번 시스템 설정을 사용하는 것으로 했다.  

```js
Proxy.reset_connection = function() {
    var config = { mode: "system" };
    chrome.proxy.settings.set(
        {
            value: config,
            scope: 'regular'
        },
        function() {}
    );
}
```
버튼을 만들어서 간단히 테스트 해 보니 잘 된다. 이제는 개발중인 extension 이 있는 상태에서 마음놓고 웹브라우징을 할 수 있다. 

### Spectre.css 
UI를 배치하기 위해서 spectre 프레임웍을 사용하기로 했다.

```html
<link rel="stylesheet" href="libs/css/spectre.min.css">
<link rel="stylesheet" href="libs/css/spectre-exp.min.css">
<link rel="stylesheet" href="libs/css/spectre-icons.min.css">
```

그리고 문서의 예제 대로 스위치를 배치 한다.

```html
<div class="form-group">
    <div class="col-8 col-mx-auto">
        <label class="form-switch">
            <input id="onoff_switch" type="checkbox">
            <i class="form-icon"></i> via VPN
        </label>
    </div>
</div>
```

### on/off switch 
스위치(checkbox) 가 on/off 되면 각 상태에 대해 작동 하도록 조건문을 작성하고 popup창을 닫은 이후에도 상태 정보를 유지하기 위해 localStorage 에 값을 저장해 놓는다.  

```js
$("#onoff_switch").click(function() {
    Popup.onoff_switch_controller();
});

Popup.onoff_switch_controller = function() {
    var switch_status = $("#onoff_switch").is(":checked");
    if (switch_status) {
        Proxy.make_connection();
        localStorage.__onoff_status = "on";
    } else {        
        Proxy.reset_connection();
        localStorage.__onoff_status = "off";
    }
}
```

그리고 테스트를 해 보면 클릭 할 때 마다 스위치가 on/off 왔다 갔다 하고 프록시 설정/해체 잘 된다. 그러나 창을 닫으면 다시 off 상태로 보여진다. 

### popup 열 때 on/off 정보 확인 
localStorage에 on/off 정보가 저장 되어 있으니, `DOMContentLoaded` 이벤트에서 확인 해서 checked 를 설정 해 주면 될 것이다. 

```js
if (localStorage.__onoff_status == "on") {
    $("#onoff_switch").attr("checked", true);
} else {
    $("#onoff_switch").attr("checked", false);
}
```
아이콘을 클릭해서 창을 닫았다 열었다 계속 해도 사용 중이면 계속 ON 으로 보여진다. 

### 계속
이렇게 까지 하면 이제 다음은 아이콘으로 보여주는 건데.. 이건 디자인의 영역이라 좀 난감하다. 
