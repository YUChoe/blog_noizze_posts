
![](vpn-3406770_640%5B1%5D.jpg)

기업용 VPN 서비스를 Google Chrome 등의 브라우저에서 플러그인으로 구성하는 것을 구상 중이다. 

SOCKS 프록시를 켜고 꺼는 형태로 만들 수 있지 않을까 해서 구성을 보니까. 

1. config 를 만든다. mode 가 `fixed_servers` 외에 여러가지가 있는데 [메뉴얼](https://developer.chrome.com/extensions/proxy)을 참조.
  
  ```js
socks_server_config = {
        mode: "fixed_servers",
        rules: {
    	        singleProxy: {
                    scheme: "socks5",
                    host: server_host,
                    port: server_port
                },
                bypassList: ["localhost", "api.socks5.your.server"]
        }
}  
```

2. 브라우저(chrome)에 설정을 적용 한다. 

```js
chrome.proxy.settings.set(socks_server_config, function() {
// error handling    });
```

일단은 여기까지만 보면 쉬운데... `chrome.proxy.settings.set()` 메소드를 콘솔에서 입력 해 보면, 

```
> chrome.proxy.settings.set()
Uncaught TypeError: Cannot read property 'settings' of undefined
```
로 나오고 메뉴얼에 따르면 익스텐션에서만 작동 하는 것으로 보인다. 그리고 `Manifest` 에 `permission` 도 해 줘야 한다. 

이걸 기반으로 아주 간단한 익스텐션을 만들어 보고, 서버 쪽에 SOCKS5 서버를 구축 해서 테스트 해 봐야 겠다. 

