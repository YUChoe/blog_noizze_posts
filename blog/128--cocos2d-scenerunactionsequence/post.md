
scene.m 의 init function에 아래와 같이 구현 

```objc
-(id) init
{
  if ((self = [super init]))
  {
    self.isTouchEnabled = YES;

    // 스테이지 구성 - 배경 
    id sceneStep_01 = [CCCallFuncN actionWithTarget:self selector:@selector(makeStage:)];  
    // 스테이지 구성 - 아군     
    id sceneStep_02 = [CCCallFuncN actionWithTarget:self selector:@selector(loadAllyConfig:)];
    // 게임 시작    
    id sceneStep_03 = [CCCallFuncN actionWithTarget:self selector:@selector(startTimers:)]; 

    [self runAction: [CCSequence actions:sceneStep_01, 
                                         sceneStep_02, 
                                         sceneStep_03, nil]]; 
  }
  return self;
}
```