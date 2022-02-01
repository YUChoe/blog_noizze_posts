
 > 이 예제는 [facebook의 게임/앱 스터디 그룹](http://www.facebook.com/groups/131873050221514/?ap=1)을 위해 작성 되었습니다.

화면 방향을 세로(포트레이트=portrait)방향으로 세팅하고 터치 이벤트를 받아들여 플레이어 스프라이트를 움직여 보도록 하겠습니다.

프로젝트 네비게이터에서 **GameConfig.h** 파일의 다음 부분을 수정 합니다.

```obj-c
//#define GAME_AUTOROTATION kGameAutorotationUIViewController ==> 아래 행으로 수정
#define GAME_AUTOROTATION kGameAutorotationNone
```

다음은 **AppDelegate.m** 파일의 다음 부분을 수정 합니다.

```objc
/*
#if GAME_AUTOROTATION == kGameAutorotationUIViewController
[director setDeviceOrientation:kCCDeviceOrientationPortrait];
#else
[director setDeviceOrientation:kCCDeviceOrientationLandscapeLeft];
#endif
==> 아래 행으로 수정 */
[director setDeviceOrientation:kCCDeviceOrientationPortrait];
```

이렇게 하면 자동 회전 기능에 영향을 받지 않고 화면을 세로로 길게(portrait)로 고정 시킬 수 있습니다. *(더 좋은 방법이 있을 수도?)*

![](http://blog.noizze.net/wp-content/uploads/2011/08/sim2.jpg)

처음 [기획 단계](https://blog.noizze.net/blog/158--invader-00)에서 UI를 어떻게 할 지를 빼먹긴 했는데 위와 같은 화면(아이폰3 기준 가로320/세로480)을 좌-중-우로 3등분 해서
* 좌 지역이 터치 되면 플레이어 캐릭터를 좌측으로 움직이고
* 우 지역도 마찬가지
* 계속 누르고 있으면, 계속 이동
* 좌,우 화면 끝에 다다르면 더이상 이동하지 않음
* 중 지역은 다음 예제로 미사일을 발사

로 정의 하고 좌우 움직임에 해당하는 1,2 애니메이션을 만들어 봅시다. **HelloWorldLayer.h** 파일에 다음 내용을 기록 합니다.

```objc
@interface HelloWorldLayer : CCLayer
{
  BOOL onMoving;
  CCSprite *playerSprite;
}
```

onMoving 변수는 터치를 손을 계속 대고 있을 때 연속해서 플레이어 스프라이트를 움직이게 할 수 있도록 계속 움직일 것인지 멈출 것인지를 정의한 변수 입니다.
playerSprite 는 이름 그대로 플레이어 스프라이트를 클래스 전역으로 정의 한 변수 입니다.

```objc
// returns a CCScene that contains the HelloWorldLayer as the only child

+(CCScene *) scene;
-(void) moveLeftCheck:(id)anObject;
-(void) moveRightCheck:(id)anObject;

-(BOOL) ccTouchesBegan:(NSSet *)touches withEvent:(UIEvent *)event;
-(BOOL) ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event;
-(BOOL) ccTouchesMoved:(NSSet *)touches withEvent:(UIEvent *)event;
@end
```

cocos2d 프레임웍의 터치 이벤트 3종세트를 오버라이드 하여 사용 합니다.

* ccTouchesBegan : 터치를 하는 순간 이벤트를 처리 합니다.
* ccTouchesEnded : 손을 떼는 순간 이벤트를 처리 합니다.
* ccTouchesMoved : 누르고 이동(드레그) 하는 이벤트를 처리 합니다.

그리고 커스텀 메쏘드로 아무 생각 없이 지은 이름의 메쏘드 들 입니다

* moveLeftCheck : 왼쪽으로 이동 애니메이션 중에 계속 할지 말지를 검사하는 메쏘드
* moveRightCheck : 마찬가지로 오른쪽으로 이동 에니메이션 중에 검사 메쏘드

다음은, 터치 3종세트 이벤트에 어디에 터치가 이루어 졌는지는 확인 하는 코드 입니다. cocos2d에서 어떤 스프라이트에 터치가 되었는지를 정리해서 확인 하는 "특별한" 방법은 아직 없습니다. 그래서

```objc

-(BOOL) ccTouchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
  UITouch *touch = [touches anyObject];
  if (touch)
  {
    CGPoint touchedlocation = [[CCDirector sharedDirector] convertToGL: [touch locationInView:touch.view]];
    NSLog(@&quot;touchBegan:ccp(%.0f, %.0f)&quot;, touchedlocation.x, touchedlocation.y);
  }
  return YES;
}
```

위의 코드와 같은 방법으로 touch객체를 통해 Director에서 GL로 변환된(몰라도 됨) x,y 좌표 경로를 가져올 수 있습니다. touchedlocation.x 가 좌 1/3 인지 우 1/3 인지 판별해서 각각에 대한 에니메이션을 작성 하면 되겠습니다.