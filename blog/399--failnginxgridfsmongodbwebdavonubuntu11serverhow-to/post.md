
<h2>step 00 : ready</h2>
ubuntu 11 server + openssh-server 설치
네트워크 세팅
<h2>step 01 : 컴파일 환경/소스/설정파일 준비</h2>
 
<pre class="striped:false lang:default decode:true " >$ cd ~
$ sudo apt-get -y install git subversion make gcc mongodb-dev libpcre3-dev zlib1g-dev libssl-dev # 의존성 관련 많이 설치 됨
$ mkdir src
$ cd src
$ svn export svn://svn.nginx.org/nginx/tags/release-1.0.9 nginx-1.0.9
$ git clone ![](https://github.com/JasonGiedymin/nginx-init-ubuntu.git)
$ git clone ![](https://github.com/mdirolf/nginx-gridfs.git)
$ cd nginx-gridfs/
$ git checkout -b v0.8 # stable
$ git submodule init
$ git submodule update</pre> 

<h2>step 02: nginx 컴파일 설정</h2>
## ssl/sha 등은 테스트를 위해 일단 제외
## gridfs, dav 모듈 활성화
<pre class="striped:false lang:default decode:true " >$ cd ../nginx-1.0.9/
$ cp auto/configure .
$ ./configure 
--add-module=../nginx-gridfs 
--with-http_dav_module 
--sbin-path=/sbin 
--conf-path=/etc/nginx/nginx.conf 
--error-log-path=/var/log/nginx/error.log 
--http-log-path=/var/log/nginx/access.log 
--pid-path=/var/run/nginx.pid 
--lock-path=/var/lock

...

Configuration summary
+ using system PCRE library
+ OpenSSL library is not used
+ using builtin md5 code
+ sha1 library is not found
+ using system zlib library

nginx path prefix: &quot;/usr/local/nginx&quot;
nginx binary file: &quot;/sbin&quot;
nginx configuration prefix: &quot;/etc&quot;
nginx configuration file: &quot;/etc/nginx/nginx.conf&quot;
nginx pid file: &quot;/var/run/nginx.pid&quot;
nginx error log file: &quot;/var/log/nginx/error.log&quot;
nginx http access log file: &quot;/var/log/nginx/access.log&quot;
nginx http client request body temporary files: &quot;client_body_temp&quot;
nginx http proxy temporary files: &quot;proxy_temp&quot;
nginx http fastcgi temporary files: &quot;fastcgi_temp&quot;
nginx http uwsgi temporary files: &quot;uwsgi_temp&quot;
nginx http scgi temporary files: &quot;scgi_temp&quot; </pre>

<h2>step 03: 설정파일 변경</h2>
## gcc 4.6 때문이기도 하고, 여러가지 문제로
## Makefile안에서 TAB 문자 주의
## manpage 제외.. 왜 오류 나는지 모르겠음 일단 테스트를 위해 제외
<pre class="striped:false lang:default decode:true " >$ vi Makefile
...
build:
$(MAKE) -f objs/Makefile
#$(MAKE) -f objs/Makefile manpage # 제거 
...

$ vi objs/Makefile

3:
CFLAGS = -pipe -O -W -Wall -Wpointer-arith -Wno-unused-parameter -Wunused-function -Wunused-variable -Wunused-value -Werror -g --std=c99 -Isrc -Wno-unused-but-set-variable -Wno-missing-field-initializers -Wno-clobbered

...

1158:
        test -d '$(DESTDIR)/usr/local/nginx/html' || cp -r docs/html '$(DESTDIR)/usr/local/nginx'
...

$ make
$ sudo make install
</pre>

<h2>step 04 : nginx 데몬 설정</h2>
## init 파일 수정
## configure 에서 세팅을 바꿔 놨으니 수정 해야 함 
<pre class="striped:false lang:default decode:true " >$ cd ../nginx-init-ubuntu
$ vi nginx
...
DAEMON=/sbin/nginx
...
lockfile=/var/lock/nginx
NGINX_CONF_FILE=&quot;/etc/nginx/nginx.conf&quot;
...

$ sudo cp nginx /etc/init.d/
$ sudo chmod 755 /etc/init.d/nginx
$ sudo update-rc.d nginx defaults
$ sudo service nginx start
</pre>
<h2>step 05: nginx-gridfs 설정</h2>
<pre class="striped:false lang:default decode:true " >$ sudo vi /etc/nginx/nginx.conf
## server 안에 
location /gridfs/ { 
  gridfs my_app;
}
...

$ sudo service nginx restart
</pre>
<h2>step 06 : nginx http 테스트 + gridfs 테스트 (FAIL)</h2>
1. 브라우저로 ![](http://192.168.56.104/) 접속 -> 정상 
2. 브라우저로 ![](http://192.168.56.104/gridfs) 접속

404 Not Found

<pre class="striped:false lang:default decode:true " >$ tail /var/log/nginx/error.log

2012/01/30 20:05:38 [error] 10424#0: *1 open() &quot;/usr/local/nginx/html/gridfs&quot; failed (2: No such file or directory), client: 192.168.56.1, server: localhost, request: &quot;GET /gridfs HTTP/1.1&quot;, host: &quot;192.168.56.104&quot;
2012/01/30 20:05:38 [error] 10424#0: *1 open() &quot;/usr/local/nginx/html/favicon.ico&quot; failed (2: No such file or directory), client: 192.168.56.1, server: localhost, request: &quot;GET /favicon.ico HTTP/1.1&quot;, host: &quot;192.168.56.104&quot;
</pre>
<h2>step 07 : webdav 설정 및 테스트 (FAIL)</h2>
## ref : ![](http://wiki.nginx.org/HttpDavModule)
<pre class="striped:false lang:default decode:true " >$ sudo mkdir /usr/local/nginx/html/data
$ sudo chmod 777 /usr/local/nginx/html/data
$ sudo vi /etc/nginx/nginx.conf

server {
listen 8000;

#auth_basic &quot;Restricted&quot;;
#auth_basic_user_file .htpasswd;

location / {
root html/data;
client_body_temp_path /usr/local/nginx/client_body_temp;

dav_methods PUT DELETE MKCOL COPY MOVE;
create_full_put_path on;
dav_access user:rw group:rw all:r;
}

$ sudo service nginx restart
</pre>

## 브라우저로 ![](http://192.168.56.104:8000) 접속

403 Forbidden

<pre class="striped:false lang:default decode:true " >$ tail /var/log/nginx/error.log

2012/01/30 20:19:02 [error] 10671#0: *1 directory index of &quot;/data/&quot; is forbidden, client: 192.168.56.1, server: , request: &quot;GET / HTTP/1.1&quot;, host: &quot;192.168.56.104:8000&quot;
</pre>