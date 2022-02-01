
CentOS 4.7 에서의 예제 QT 4.4.0+ 설치가 되어 있어야 함.
http://cutycapt.sourceforge.net/ cutycapt 사이트에서 메뉴얼 확인

```
# svn co https://cutycapt.svn.sourceforge.net/svnroot/cutycapt
# cd cutycapt/CutyCapt
# qmake && make
```

xorg-x11-Xvfb ttfonts-ko.noarch 설치. 의존성 문제로 xorg-x11-xauth, switchdesk, xorg-x11, xorg-x11-Xvfb, xinitrc 패키지가 같이 설치 됨

```
# yum install xorg-x11-Xvfb ttfonts-ko.noarch
```

```
# #xvfb-run 스크립트 카피 (![](http://blog.noizze.net/?p=295))
# xvfb-run --server-args="-screen 0, 1024x768x24" ./CutyCapt --url="http://www.someURL.net" --out="filename.png"
```
