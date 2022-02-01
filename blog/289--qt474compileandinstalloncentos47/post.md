
* `yum install gcc-g++ xorg-x11-devel -y` 로 설치 하면 fontconfig-devel, freetype-devel, pkgconfig, freetype, xorg-x11-libs, xorg-x11-xfs 패키지들이 의존성 해결을 위해 같이 설치 됨
* `wget http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.7.4.tar.gz` 다운로드 받아서
* `tar xzf qt-everywhere-opensource-src-4.7.4.tar.gz` 압축을 풀고
* `cd qt-everywhere-opensource-src-4.7.4` 로 이동하여
* `./configure` 하면 라이센스 관련 여러가지를 물어보는데 opensource 를 선택하고 GPL 등에 yes로 agree하면 시작
* 설정이 완료 되면 `make` 로 컴파일
* `make install`
* `vim ~/.bash_profile` 에서 PATH에 `/usr/local/Trolltech/Qt-4.7.4/bin/` 추가

완료 all done