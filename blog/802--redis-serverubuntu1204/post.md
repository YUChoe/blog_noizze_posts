
기본 레포지토리의 sudo apt-get install redis-server 로는 2.2.12 까지밖에 버전이 안 올라가 있음

```
dev@server:~$ redis-cli info | grep redis_version
redis_version:2.2.12
dev@server:~$ sudo add-apt-repository ppa:rwky/redis
...
dev@server:~$ sudo apt-get update
...
dev@server:~$ sudo apt-get install redis-server
...

dev@server:~$ redis-cli info | grep redis_version
redis_version:3.0.6
```

14.04 에서는 아직 테스트 해보지 않았음