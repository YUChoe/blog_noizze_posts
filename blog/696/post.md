
밀린(...) 유튜브 구독물들을 정리 하다가 Ben Heck’s Raspberry Pi Media Center 영상을 봤다.

![](https://youtu.be/P7m6HTV7ysM)

안그래도 [라즈베리파이2](https://www.raspberrypi.org/)를 사놓고 놀려두고 있는 중인데다가 집에서 NAS에 있는 동영상들을 더이상 아이패드에 [nPlayer](https://itunes.apple.com/us/app/nplayer/id539397400?mt=8)가 아닌 (비교적 큰) 티비 화면으로 보기 위해 크롬캐스트를 살까 말까 하던 중이라 과감하게 추석프로젝트로 진행하기로 결정

* Ben Heck Show 에서처럼 [openelec.tv](http://openelec.tv/) 의 라즈베리파이2용 디스크 이미지를 사용
* 맥에서 `sudo dd if=OpenELEC-RPi2.arm-5.0.8.img of=/dev/disk3 bs=1m` 명령으로 disk3에 인식 된 USB microSD슬롯에쓰고,
* 라즈베리파이에 전원, (유선)네트워크 연결하고 부팅
* 최초 부팅될 때 OpenELEC이 파티션 조정 등 세팅을 몇번 함
* SSH 로 접속해서 (기본계정 root/openelec)
*  `mount -t nfs -o nolock,nfsvers=3,rsize=32768,wsize=32768,intr,noatime mynas:/mnt/zfs_videos videos` 로 videos디렉토리에 마운트
* 리모컨은 아래의 동영상을 참조 해서 Kodi Remote 앱으로 구동.

![](https://youtu.be/cjiKHTn9OMI)