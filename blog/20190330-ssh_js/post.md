
프로젝트가 지연 되는 이유부터 이야기 해 보자면, 
1. 서버 구성 중에 백엔드에서 microservice 들 끼리 통신하는데 문제. 
2. 어드민 대시보드 설계 / 변경 / 재설계 / 변경 ...
3. 보안 부분에 대한 걱정. 조작된 서버가 등록 되면 어떻게 알아내고 처리 할 것인가?
4. 또한, 나중에 P2P 형식으로 서비스가 되면 조작된 서버인지 아닌지 판단 로직을 또 바꿀 것인가? 
5. 기업시장에서 서비스 하기 위해 보안을 강화 한 ssh + socks5 로 통신하려면 브라우저 플러그인 만으로 가능 한가?
6. 빌링 시스템과 연계는 어떻게 할 것인가
7. NETFLIX 를 서비스 할 수 있는다?

아직까지 해결해야 하는 문제들이 많은데 이 중에서 이번에는 SSH 부분을 진행 해 보고자 한다. 

npm 에서 ssh 나 tunnel 로 검색하면 많은 프로젝트 들이 나오는데, 그 중에 테스트 장비에서 설치가 가능하고, 예제가 있는 것들을 찾다 보니 2~3개로 압축 되었고 이것들을 가지고 하나씩 테스트 해 보기로 했다. 

https://www.npmjs.com/package/ssh2 의 socksv5 모듈을 사용한 아래의 예제가 잘 작동 했다.

```js 
var socks = require('socksv5'),
    Client = require('ssh2').Client;

var ssh_config = {
  host: '192.168.100.1',
  port: 22,
  username: 'nodejs',
  password: 'rules'
};

socks.createServer(function(info, accept, deny) {
  // NOTE: you could just use one ssh2 client connection for all forwards, but
  // you could run into server-imposed limits if you have too many forwards open
  // at any given time
  var conn = new Client();
  conn.on('ready', function() {
    conn.forwardOut(info.srcAddr,
                    info.srcPort,
                    info.dstAddr,
                    info.dstPort,
                    function(err, stream) {
      if (err) {
        conn.end();
        return deny();
      }

      var clientSocket;
      if (clientSocket = accept(true)) {
        stream.pipe(clientSocket).pipe(stream).on('close', function() {
          conn.end();
        });
      } else
        conn.end();
    });
  }).on('error', function(err) {
    deny();
  }).connect(ssh_config);
}).listen(1080, 'localhost', function() {
  console.log('SOCKSv5 proxy server started on port 1080');
}).useAuth(socks.auth.None());

// test with cURL:
//   curl -i --socks5 localhost:1080 google.com
```

문제는 이 방법으로 하면 매 host 마다(세션마다?) SSH 커넥션을 하기 때문에 서버 엄청난 부하와 동시에 모바일 3G 시절의 퍼포먼스를 보여준다. 

일단 공부 해서 튜닝 하기 전에 결론부터 내리자면, 
 
1. Javascript only 로 SSH 와 Dynamic Forwarding 가능 
2. 소켓을 유지하고 공유하기 위해 약간의 수정이 필요하다 


 