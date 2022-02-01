
* 현재 문제점 : 주로 태블릿용 윈도우나 몇몇 PC에서 발생. 설치과정에서 TAP 장치 설치가 되지 않음. 강제로 설치 한 이후에는 openvpn 연결/인증 후에 TAP 장치가 IP를 못 받아 옴

openvpn 최신 버전을 설치 해 봐도 해결되지 않았음. 기존 tap 장치를 삭제하고 다시 설치 하려고 해도, 정상적으로 삭제 되지 않음. 레지스트리를 정리 해도 마찬가지... 

여러번 사례가 있었는데 첫번째만 OS를 재설치 함으로써 문제가 사라졌고, 그 외의 케이스는 포기. 

* google 검색 : <a href="![](https://www.google.co.kr/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8)#newwindow=1&q=replacement%20windows%20tap%20adapter">replacement windows tap adapter</a>
* google 검색 : <a href="![](https://www.google.co.kr/search?newwindow=1&espv=2&biw=1680&bih=955&q=tap+windows+adapter+v9+not+working&revid=1218439268&sa=X&ei=-0AeVfbgAePRmAW3loLoDg&sqi=2&ved=0CIYBENUCKAI)">tap windows adapter v9 not working</a>

검색 해 보니 비슷비슷 한 증상이 있기는 한가 봄 

* <a href="![](https://social.technet.microsoft.com/Forums/en-US/e0653755-531d-45a6-8221-46e552328d8d/unwanted-tapwindows-adapter-v9-and-tapwin32-adapter-oas-drivers-installing?forum=w8itpronetworkingHope)">Unwanted TAP-Windows Adapter V9 and TAP-Win32 Adapter OAS drivers installing</a>
* <a href="![](http://support.vpnsecure.me/articles/frequently-asked-questions/openvpn-gui-no-tap-win32-adapters-on-this-system-error-fix)">OpenVPN GUI: "No TAP-WIN32 adapters on this system" error fix</a>

추가1> ![](https://github.com/OpenVPN/tap-windows6) 발견 답은 멀지 않은 곳에 있는 것일 수도? 테스트 예정 
추가2> 예전에는 안 보였는데, openvpn 커뮤니티에서 Installer (NDIS 6) 항목을 따로 두고 <a href="![](http://openvpn.net/index.php/open-source/downloads.html)">배포</a>도 하고 있었음. 