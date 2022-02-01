
```objc
UITextView *textView = [[UITextView alloc] 
                         initWithFrame:CGRectMake(100,100, 480/2, 320/2)];
textView.backgroundColor = [UIColor clearColor];
textView.textColor = [UIColor redColor];
textView.text = @&quot;I am First enemy&quot;;
[textView setEditable:NO]; 
    
[[[CCDirector sharedDirector]openGLView]addSubview:textView];
```