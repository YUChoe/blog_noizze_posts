
YUM 으로 설치 하기엔 의존성 문제가 너무 많이 생겨서 바이너리 모듈을 설치하기로 결정

기존에 php 5.1.6 이 설치 되어 있는 상태 

설치/설정
<code>1. 서비스를 위해서 iptables 설정과 selinux 설정을 확인
2. wget ![](http://downloads.zend.com/optimizer/3.3.9/ZendOptimizer-3.3.9-linux-glibc23-i386.tar.gz) (64비트는 따로)
3. tar xzf ZendOptimizer-3.3.9-linux-glibc23-i386.tar.gz
4. cp ZendOptimizer-3.3.9-linux-glibc23-i386/data/5_1_x_comp/ZendOptimizer.so /usr/lib/php/modules
5. php.ini 수정 : zend_extension=/usr/lib/php/modules/ZendOptimizer.so
6. httpd restrt</code>

확인
<code>1. php -m
2. php -i |grep Zend
</code>