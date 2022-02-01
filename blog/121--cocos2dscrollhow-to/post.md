
<pre><code>-(BOOL)ccTouchesMoved:(NSSet *)touches withEvent:(UIEvent *)event {
  UITouch *myTouch = [touches anyObject];
  CGPoint location = [myTouch locationInView:[myTouch view]];
  location = [[CCDirector sharedDirector] convertToGL:location];
  
  for( UITouch *touch in touches ) {
    CGPoint touchLocation = [touch locationInView: [touch view]];   
    CGPoint prevLocation = [touch previousLocationInView: [touch view]];    
    
    touchLocation = [[CCDirector sharedDirector] convertToGL: touchLocation];
    prevLocation = [[CCDirector sharedDirector] convertToGL: prevLocation];
    
    CGPoint diff = ccpSub(touchLocation,prevLocation);
    diff.x = 0; // 위 아래 방향으로만 스크롤 고정 인 경우 
    [self setPosition: ccpAdd(self.position, diff)];
  }
	return YES;
}</code></pre>