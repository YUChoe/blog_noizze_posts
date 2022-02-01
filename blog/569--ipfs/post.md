
* go-lang 관련 뉴스 보다가 [ipfs](https://github.com/jbenet/go-ipfs) 라는 재미있는 컨셉의 스토리지(?)를 발견해서 개발 초기이길래 [GUI-wrapper](https://github.com/YUChoe/ipfs-gui)를 개발 하면서 공부 해 볼겸 이것 저것 만져 보는데 
* 가장 기본적인 사용/작동법이 잘 이해가 안 간다. `ipfs init` 이 후에

```
$ cat README.md
# ipfs-gui

this project "is going to" wrap https://github.com/jbenet/go-ipfs
$ ipfs add README.md
added QmRTwxKKTsgVVSNYreTUEBzLsPeAcCiGXEh5Qp57VdwhDW README.md
$ ipfs cat QmRTwxKKTsgVVSNYreTUEBzLsPeAcCiGXEh5Qp57VdwhDW
# ipfs-gui

this project "is going to" wrap https://github.com/jbenet/go-ipfs
```

* 여기까지는 문제 없는데, 목록은 어떻게 보는 것으로 이해 해야 하지?

```
$ ipfs ls QmRTwxKKTsgVVSNYreTUEBzLsPeAcCiGXEh5Qp57VdwhDW
$ ipfs ls /ipfs/QmRTwxKKTsgVVSNYreTUEBzLsPeAcCiGXEh5Qp57VdwhDW/
```

* 만약에 리스트를 따로 볼 수 없다면 HASH를 잃어 버리면 그 파일을 더는 찾을 수 없다는 걸까 ?
* 커뮤니티나 이슈트래커에 물어보기 전에 좀 더 분석 해봐야 겠다.