
1. centos6.2 최소 설치 (![](http://ftp.daum.net/centos/6.2/isos/i386/))
2. 네트워크 설정
vi /etc/sysconfig/network-scripts/ifcfg-eth0 의 ONBOOT 를 yes 로 수정
3. 필요하다면 selinux 설정 수정 : vi /etc/selinux/config
4. nginx 의 yum repository 등록
<pre># cat &gt; /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=![](http://nginx.org/packages/centos/6/$basearch/)
gpgcheck=0
enabled=1
^D
#</pre>
5. CentOS 6/5.7 and Red Hat (RHEL) 6.1/6/5.7 Remi repository
<pre># rpm -Uvh ![](http://download.fedora.redhat.com/pub/epel/6/i386/epel-release-6-5.noarch.rpm)
# rpm -Uvh ![](http://rpms.famillecollet.com/enterprise/remi-release-6.rpm)
# vi /etc/yum.repos.d/remi.repo # Edit "enabled=1"
# yum update</pre>
6. MySQL 설치
<pre># yum install mysql mysql-server
# /usr/bin/mysql_secure_installation 
....
Set root password? [Y/n] Y
New password: 

Remove anonymous users? [Y/n] Y
 ... Success!
Disallow root login remotely? [Y/n] Y
 ... Success!
.... 
Remove test database and access to it? [Y/n] Y
 - Dropping test database...
Reload privilege tables now? [Y/n] Y
 ... Success!
...
# mysqladmin -u root password [password]</pre>
7. nginx + php-fpm 설치
<pre># yum install nginx php php-fpm php-common php-pear php-pdo php-mysql php-pgsql php-pecl-memcache php-gd php-mbstring php-mcrypt php-xml</pre>
* 의존성 때문에 httpd 가 설치되니, chkconfig에서 조정 할 필요가 있음
8. 방화벽firewall 설정
<pre># vi /etc/sysconfig/iptables
 ## -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT 추가</pre>
9. nginx 확인
<pre># ls -l /usr/share/nginx/html
total 8
-rw-r--r-- 1 root root 383 Dec 16 00:26 50x.html
-rw-r--r-- 1 root root 151 Dec 16 00:26 index.html</pre>
* 웹브라우저로 확인

10. php-fpm 세팅
<pre># vi /etc/nginx/conf.d/default.conf
 ## 1) pass the PHP scripts to FastCGI server 항목 주석 해제 
 ## 2) fastcgi_param 수정 
...
    location ~ .php$ {
        root           html;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        #fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        fastcgi_param SCRIPT_FILENAME /usr/share/nginx/html$fastcgi_script_name;

        include        fastcgi_params;
    }
...
# service nginx configtest
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
# service nginx restart 
Stopping nginx:                                            [  OK  ]
Starting nginx:                                            [  OK  ]
# cat &gt; /usr/share/nginx/html/test.php
&lt;?php phpinfo(); ?&gt;
^D
#</pre>
* 웹브라우저로 확인

Reference
* 우분투 10.04 LTS, nginx+php-fastcgi+mysql 설치하기 (![](http://folderfile.net/xe/2028))
* Nginx proxy to Apache (![](http://groups.drupal.org/node/50168))
* LEMP( Linux + Nginx + Mysql + php) (![](http://www.if-not-true-then-false.com/2011/lemp-on-fedora-centos-red-hat-rhel-linux-nginx-mysql-php-fpm/))