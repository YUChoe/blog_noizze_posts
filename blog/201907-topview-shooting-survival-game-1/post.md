
기본 적인 게임 메카닉은 다 만들었는데, 멀티플레이어로 만드는게 쉽지 않다. 
그런데다가 unity3d 가 기존 멀티플레이어 프레임웍을 바꾸고 있어서 (2019.07 현재) 새로운 정보를 구하기도 쉽지 않고... 

그래서 이제 계획은 일단 기존 HLAPI 를 이용 한 로비+멀티플레이어를 구현하고 나중에 프레임웍을 바꿔야 할 때가 되면 그때 생각하기로 했다. 런칭을 해야 바꿀 필요성이 생기는 법일테니.. 

다음 문제는, 멀티플레이어 로비 예제 구하기가 쉽지 않다는 것. 20분짜리 영상 20개를 봐야 하는 그런 영상들이 대부분이라.. 

[Quill18creates](https://www.youtube.com/channel/UCPXOQq7PWh5OdCwEO60Y8jQ)

[Game dev Tutorials BRACKEYS](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA)

이 두 유투버의 강좌를 기본으로 구현 할 예정. 

![](https://youtu.be/-m28axeuRNs)

* 현재 문제: 서버만 Cmd_shoot() 으로 총알이 발사 되는데, 클라이언트는 안 보임  
