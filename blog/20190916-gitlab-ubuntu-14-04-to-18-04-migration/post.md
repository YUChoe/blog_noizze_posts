
![](/blog/20190916-gitlab-ubuntu-14-04-to-18-04-migration/7ca844ab1a8b6536a2ed805ab7e0ed5d%5B1%5D.png)

ubuntu 14.04에서 gitlab-ce를 운영하다 올해 초 쯤에 11.10.8 로 패키지 업데이트가 멈추었다. 2019년 9월 16일 현재 최신 저번은 12.2.5 이유를 확인 해 보니 https://packages.gitlab.com/gitlab/gitlab-ce 를 통해 더이상 14.04는 11.10.8 이상 지원 하지 않는 것으로 확인.

이것 저것 방법을 찾다가 어차피 개발팀에서 운영을 직접 해야 하니 OS를 18.04로 올리는 것으로 합의를 봄. 

1. 기존 데이터 백업. `gitlab-rake gitlab:backup:create`  
2. 새로 OS 설치 및 네트워크 설정(netplan)
3. `curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash` 로 apt 레포지토리 등록
4. `apt upgrade` 로 패키지 갱신. 
5. `apt install gitlab-ce=11.10.8-ce.0` 로 사용하던 버전으로 설치. 버전을 맞추지 않으면 복원이 안됨
6. `export external_url="https://gitlab.example.com";  gitlab-ctl reconfigure`
7. `cd /var/opt/gitlab/backup` 에 1번에서 백업 한 파일 위치 시키고 permission 설정(git.git)
8. `gitlab-rake gitlab:backup:restore` 로 복원 
9. `.ssh/authorized_keys` 이전
10. `/etc/gitlab` 설정 이전
11. `/var/opt/gitlab/nginx/conf/gitlab-http.conf` 확인  
12. `gitlab-ctl restart` 로 서비스 재시작 

이렇게 데이터 이전이 정상적으로 되었는지 확인 하고 최신버전으로 업그레이드 해야 하는데, gitlab-ce 는 메이저 업그레이드가 지원 하는 버전 까지 단계적으로 업그레이드를 해야 한다. 다행히 11.11.x 이 바로 다음 버전이어서 한번만 하면 됨 

1. `apt install gitlab-ce=11.11.8-ce.0` 로 11.10.8 을 11.11.8 로 올림 
2. `apt upgrade` 로 전체 패키지를 업그레이드 하면서 gitlab-ce도 12.2.5-ce.0 로 업그레이드 

