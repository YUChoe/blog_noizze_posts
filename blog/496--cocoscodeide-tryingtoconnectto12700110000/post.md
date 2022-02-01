
<blockquote>Trying to connect to 127.0.0.1:10000</blockquote>
에서 연결 된 것 처럼 보이지만 디버그 접속이 안되서 테스트가 안되는 문제
(문제 자체를 설명하기가 어렵다)

어찌되었든, 해결 방법은 utorrent 를 끄는 것. utorrent 가 내부적으로 127.0.0.1:1000 을 Listen 하고 있어서 충돌이 나는 것이 문제였음. (turn the utorrent off and retry)

&nbsp;