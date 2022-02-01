

 
<pre class="wrap:true lang:objc decode:true " >UISwitch *effectSoundOnOff = [self getChildByTag:SWITCH1];
UISwitch *flipOnOff = [self getChildByTag:SWITCH2];

NSMutableDictionary *dic = [[NSMutableDictionary alloc] init];
  
[dic setObject:([effectSoundOnOff isOn] ? @&amp;quot;YES&amp;quot; : @&amp;quot;NO&amp;quot;) forKey:@&amp;quot;effectSound&amp;quot;];
[dic setObject:([flipOnOff isOn] ? @&amp;quot;YES&amp;quot; : @&amp;quot;NO&amp;quot;) forKey:@&amp;quot;flip&amp;quot;];

NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSString *documentsDirectory = [paths objectAtIndex:0];
NSString *fileName = [documentsDirectory stringByAppendingPathComponent:@&amp;quot;options.data&amp;quot;];

[dic writeToFile:fileName atomically:YES];</pre> 

