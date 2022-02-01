
<pre><code>CCMenuItemImage *redButton = [CCMenuItemImage itemFromNormalImage:@&quot;redbtn.png&quot; selectedImage:@&quot;redbtn_pushed.png&quot; target:self selector:@selector(timerGo:)];
CCMenu *menu =  [CCMenu menuWithItems:redButton, nil];
menu.position = ccp(370,175);
[self addChild:menu];</code></pre>
&nbsp;