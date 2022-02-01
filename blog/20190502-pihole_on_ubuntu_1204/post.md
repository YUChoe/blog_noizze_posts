
![](pihole_on_1204.png)

https://pi-hole.net/ DNS 기반 Ad/Malware Blocking 을 legacy system(Ubuntu 12.04LTS)에 설치 하려고 했다.

메뉴얼에 있는 대로 

```
$ sudo su
# curl -sSL https://install.pi-hole.net | bash
```
실행 했지만, 

```
  [✓] Checking for lsof
  [i] Checking for netcat (will be installed)
  [✓] Checking for psmisc
  [✓] Checking for sudo
  [i] Checking for unzip (will be installed)
  [✓] Checking for wget
  [i] Checking for idn2 (will be installed)
  [i] Checking for sqlite3 (will be installed)
  [i] Checking for libcap2-bin (will be installed)
  [i] Checking for dns-root-data (will be installed)
  [✓] Checking for resolvconf
  [i] Checking for libcap2 (will be installed)
```
여기까지 진행 되고 `/opt/pihole` 디렉토리를 생성하지 않고, `/etc/pihole/install.log` 파일도 없이 멈춤 

검색을 해 보니, https://github.com/pi-hole/pi-hole/issues/2380 가 있지만, 마지막 코멘트는 너무 오래 된 버전이라 기술 지원이 힘듬 이었다.

```
Ubuntu 12 is just far too old for us to support. This is a won't fix as there are limits to what we can do.
```

순서를 보아하니, dep package dependancy check 이후 이고, 위의 issue 에서도 볼 수 있듯이 dns-root-data 패키지가 존재하지 않아 생기는 문제이니 **미리 설치 해 두면 다음으로 넘어가지 않을까?**

```
$ sudo apt-get install python-software-properties
```
로 `add-apt-repository` 패키지를 설치 해 주고 `apt update`

```
$ sudo add-apt-repository ppa:malcscott/ppa
...
$ sudo apt-get update
```

그 후 의존성 체크에서 설치가 필요 함(will be installed) 표시가 된 패키지들을 설치 한다. 

```
$ sudo apt-get install netcat unzip idn2 sqlite3 libcap2-bin dns-root-data libcap2
```

그 후에 다시 

```
# curl -sSL https://install.pi-hole.net | bash
```

해주니 정상적으로 설치 완료. Good luck. 