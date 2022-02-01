
 > 이 예제는 [facebook의 게임/앱 스터디 그룹](http://www.facebook.com/groups/131873050221514/?ap=1)을 위해 작성 되었습니다.</em>
 
cocos2d 템플릿을 이용 한 프로젝트 시작과 스프라이트 이미지를 등록 하고 화면에 출력하겠습니다.

프로젝트를 생성하기 위해 xcode를 실행 합니다. 아래 화면과 코드 작성은 Mac OS X 10.7(Lion)에서 XCode 4.1(app)에 cocos2d-iphone 1.0.1 로 했습니다. 특별한 기능을 사용하는 것은 아니기 때문에 iOS3이상을 지원하는 다른 버전의 환경에서도 충분히 작동합니다.

![](http://blog.noizze.net/wp-content/uploads/2011/07/x1.png)

cocos2d 프레임웍의 템플릿으로 새 프로젝트를 선택 하는데, cocos2d 설치는 [사이트](http://www.cocos2d-iphone.org/)의 메뉴얼을 참조 해 주세요.

![](http://blog.noizze.net/wp-content/uploads/2011/07/x2.png)

새로 만들어진 프로젝트를 시뮬레이터로 실행하면 관련 프레임웍과 클래스를 어느정도 세팅을 미리 해 놓아서 아래와 같은 결과를 보여주는 예제를 볼 수 있습니다.

![](http://blog.noizze.net/wp-content/uploads/2011/07/sim.jpg)

 > **스프라이트?**
 > 사전적의미로는 "비디오 게임의 2D 평면적인 사물" ([http://cglink.com/1024(http://cglink.com/1024) 이라고 할 수 있는데, 게임에서 움직인다든지 배경에 깔린다든지 애니메이션을 보여준다든지 등 어떠한 역할을 할 수 있는 것의 단위입니다.

우선 플레이어, 인베이더 스프라이트 크기를 32*32 픽셀 정도 크기로 생각 했는데 정식으로 작업 된 디자인은 아직 없으니 구글링 해서 대강 비슷한 아이콘 하나를 골라 플레이어 스프라이트로 사용 해 보겠습니다.

![](http://blog.noizze.net/wp-content/uploads/2011/07/imgres-1.jpeg)

이런 이미지를 다운로드 받아 둔 다음에 드래그 해서 xcode (기본으로 보이는) 프로젝트 네비게이터의 Resources 항목 안으로 드롭 해 넣으면 다음과 같이 됩니다. (저는 Sprites라는 그룹을 생성해서 넣었지만 상관 없습니다)

![](http://blog.noizze.net/wp-content/uploads/2011/07/resource.png)

특이할 점은 xcode 에서는 리소스가 다른 그룹(폴더)에 있다고 해서 네임스페이스를 따른 다든지 하지 않습니다. 오직 파일이름으로만 구분되니 주의 해야 합니다.

다음은 위의 프로젝트 네비게이터에도 보이는 HelloWorldLayer.m 에 플레이어를 올려 놓을 수 있는 코드를 작성 해 보겠습니다.
코드 중에 init 메소드부분을 보면 템플릿을 통해 생성했으므로 다음과 같은 코드가 미리 들어 가 있습니다.

```objc
// on "init" you need to initialize your instance
-(id) init
{
	// always call "super" init
	// Apple recommends to re-assign &quot;self&quot; with the "super" return value
	if( (self=[super init])) {

		// create and initialize a Label
		CCLabelTTF *label = [CCLabelTTF labelWithString:@"Hello World" fontName:@"Marker Felt" fontSize:64];

		// ask director the the window size
		CGSize size = [[CCDirector sharedDirector] winSize];

		// position the label on the center of the screen
		label.position =  ccp( size.width /2 , size.height/2 );

		// add the label as a child to this Layer
		[self addChild: label];
	}
	return self;
}
```

이 중에 쓰지 않는 부분을 삭제 하고 다음과 같이 스프라이트를 화면에 위치 시키는 코드를 입력 합니다.

```objc
// on "init" you need to initialize your instance
-(id) init
{
	// always call "super" init
	// Apple recommends to re-assign "self" with the "super" return value
	if( (self=[super init])) {

    CCSprite *playerSprite = [CCSprite spriteWithFile:@"imgres-1.jpeg"];
    playerSprite.position = ccp(50, 50);

		[self addChild: playerSprite];
	}
	return self;
}
```
그리고 시뮬레이터로 실행 하면 다음과 같이 나옵니다.

![](http://blog.noizze.net/wp-content/uploads/2011/07/game1.jpg)
