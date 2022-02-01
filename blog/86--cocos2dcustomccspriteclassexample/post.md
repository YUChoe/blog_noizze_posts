
EnemySprite.h

<pre><code>#import &amp;lt;Foundation/Foundation.h&amp;gt;
#import &quot;cocos2d.h&quot;

@interface EnemySprite : CCSprite {
  int healthpoint;
}
@property (readwrite) int hp;

@end</code></pre>

EnemySprite.m

<pre><code>#import &quot;EnemySprite.h&quot;

@implementation EnemySprite
@synthesize hp;

-(id) initWithTexture:(CCTexture2D*)texture rect:(CGRect)rect
{
  if( (self=[super initWithTexture:texture rect:rect]))
  {
  }
  return self;
}
@end</code></pre>

<pre><code>EnemySprite *ep = [EnemySprite spriteWithFile:@&quot;redbar_20x2.png&quot;];</code></pre>