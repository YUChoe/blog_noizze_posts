
후.. 윈도에서 python 프로그래밍 하기 힘들다.
그나마 cygwin을 써서 개발환경 만들기가 조금 편해지나 싶었는데, pgsql 연동을 위해 pip install psycopg2 를 하니

`error: Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat).`

에러가 난다. 30일 짜리 비주얼 스투디오를 설치 할 수도 있지만 이 컴퓨터로 개발을 하나만 하는 것도 아니고 지저분하게 이것 저것 깔아 쓰고 싶지 않았는데 마침

https://github.com/nwcell/psycopg2-windows

에서 pip 로 설치 할 수 있는 제대로 된 패키지를 제공한다.

```
$ pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py34#egg=psycopg2
Collecting psycopg2 from git+https://github.com/nwcell/psycopg2-windows.git@win64-py34#egg=psycopg2
Cloning https://github.com/nwcell/psycopg2-windows.git (to win64-py34) to c:\cygwin64\tmp\pip-build-dq69haws\psycopg2
Installing collected packages: psycopg2
Running setup.py install for psycopg2
Successfully installed psycopg2-2.5.2
```

리눅스의 yum이나 apt 처럼 바이너리 수준으로 설치하거나 아에 pypy 로 가는건 아직 먼 걸까.