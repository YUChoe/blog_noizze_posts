
![](fizzbuzz_test.jpeg)

내가 너무 쉽게 생각하고 있는건가? 시간은 따로 안 재 봤지만, 나도 2분 정도 걸림

```python
#!/usr/bin/env python2.7

for n in range(1,101) :
    if n % 3 == 0 and n % 5 == 0:
        print "FizzBuzz"
    elif n % 3 == 0 :
        print "Fizz"
    elif n % 5 == 0 :
        print "Buzz"
    else :
        print n
 ```
 
문제에 각 조건마다 간단한 출력만 들어가 있어서 이렇게 했지만, 만약 블록이 좀 더 커질 필요가 있거나 중복/반복해서 일해야 하는 부분이 생긴다면, 3배수, 5배수 각각에 대한 flag를 붙여서 조건문은 아래쪽에 따로 출력하도록 아래와 같이 했을 듯

```python
for n in range(1,101) :
    fizz = False
    buzz = False
    
    if n % 3 == 0 :
        fizz = True
    if n % 5 == 0 :
        buzz = True 
    
    if fizz :
        print("Fizz"),
    if buzz:
        print "Buzz",
    if not fizz and not buzz :
    	print n,
    print
```

아 근데 이렇게 하면 FizzBuzz 라고 안나오고 Fizz Buzz 라고 나오겠구나.. 그건 sys.stdout.write() 으로 처리 하면 되긴 할테고..