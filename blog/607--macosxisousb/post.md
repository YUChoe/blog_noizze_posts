
[http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)

이 예제가 제일 깔끔하고 쉽게 잘 만들어졌음

1. `terminal.app` or `iterm.app` 열고
2. `hdiutil convert -format UDRW -o {생성할.img} {사용할.iso}`
  * 주의 : 생성 된 파일 확장자는 .dmg 가 됨
3. USB 드라이브 꼽고/언마운트 (예: `diskutil unmountDisk /dev/disk3` )
4. `sudo dd if={2번에서만든 파일.img.dmg} of=/dev/disk3 bs=1m`
5. `diskutil eject /dev/disk3`
