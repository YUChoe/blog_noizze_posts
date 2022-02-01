
<pre><code>  NSMutableArray *a = [[NSMutableArray alloc] init];

  [a addObject:@&quot;123166&quot;];
  [a addObject:@&quot;122377&quot;];
  [a addObject:@&quot;123188&quot;];
  [a addObject:@&quot;123199&quot;];
  [a addObject:@&quot;123100&quot;];

  for (NSString *ss in a)
  {
    NSLog(@&quot;%@&quot;, ss);
  }

  NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
  NSString *documentsDirectory = [paths objectAtIndex:0];
  NSString *fileName = [documentsDirectory stringByAppendingPathComponent:@&quot;example.dat&quot;];

  [a writeToFile:fileName atomically:YES];

  //

  NSMutableArray *aa = [NSMutableArray arrayWithContentsOfFile:fileName];
  NSLog(@&quot;array count %d&quot;, [aa count]);

  for (NSString *ss in aa)
  {
    NSLog(@&quot;result:%@&quot;, ss);
  }</code></pre>