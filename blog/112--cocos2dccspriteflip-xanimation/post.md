
```objc
- (void) flipReveal : (CCNode *) node
{
  float d = 1.0; // duration
  CCEaseExponentialIn *flipHalf = [CCEaseExponentialIn 
    actionWithAction:[CCActionTween actionWithDuration:d key:@&quot;scaleX&quot; from:-1.0 to:0.0]
  ];
  CCCallFuncN *showSprite = [CCCallFuncN actionWithTarget:self selector:@selector(showSprite:)];
  CCEaseExponentialOut *flipRemainingHalf = [CCEaseExponentialOut 
    actionWithAction:[
      CCActionTween actionWithDuration:d key:@&quot;scaleX&quot; from:0.0 to:1.0]
    ];
  CCSequence* seq = [CCSequence actions:flipHalf,showSprite,flipRemainingHalf, nil];
  [node runAction:seq];
}

- (void) showSprite : (id) node
{
	[node setVisible:YES];
}
```

Usage :
`[self flipReveal:(id)mSprite];`