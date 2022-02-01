
![](https://cython.org/images/headlogo.png)

기존에 `python(__main__)` 단일 파일로 되어 있는 경우 컴파일 예제

```
$ cython3 --embed -o ip.c ip.py # C 파일화 시키고
$ gcc -Os -I /usr/include/python3.4m -o ip ip.c -lpython3.4m -lpthread -lm -lutil -ldl # 로 컴파일
$ ldd ip
linux-gate.so.1 =&gt; (0xb776e000)
libpython3.4m.so.1.0 =&gt; /usr/lib/i386-linux-gnu/libpython3.4m.so.1.0 (0xb7380000)
libc.so.6 =&gt; /lib/i386-linux-gnu/libc.so.6 (0xb71d2000)
libpthread.so.0 =&gt; /lib/i386-linux-gnu/libpthread.so.0 (0xb71b5000)
libexpat.so.1 =&gt; /lib/i386-linux-gnu/libexpat.so.1 (0xb718c000)
libz.so.1 =&gt; /lib/i386-linux-gnu/libz.so.1 (0xb7172000)
libdl.so.2 =&gt; /lib/i386-linux-gnu/libdl.so.2 (0xb716d000)
libutil.so.1 =&gt; /lib/i386-linux-gnu/libutil.so.1 (0xb7169000)
libm.so.6 =&gt; /lib/i386-linux-gnu/libm.so.6 (0xb7122000)
/lib/ld-linux.so.2 (0xb776f000)
```
실행을 위해서는 /usr/lib/i386-linux-gnu/libpython3.4m.so.1.0 공유 라이브러리를 쓸 수 있는지 확인 필요