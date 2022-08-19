# sample csv file 
```
$ ls -lh 1500000\ Sales\ Records.csv
-rw-rw-r-- 1 yuchoe yuchoe 179M Jul 29  2017 '1500000 Sales Records.csv'
$ head 1500000\ Sales\ Records.csv
Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
Sub-Saharan Africa,South Africa,Fruits,Offline,M,7/27/2012,443368995,7/28/2012,1593,9.33,6.92,14862.69,11023.56,3839.13
Middle East and North Africa,Morocco,Clothes,Online,M,9/14/2013,667593514,10/19/2013,4611,109.28,35.84,503890.08,165258.24,338631.84
Australia and Oceania,Papua New Guinea,Meat,Offline,M,5/15/2015,940995585,6/4/2015,360,421.89,364.69,151880.40,131288.40,20592.00
Sub-Saharan Africa,Djibouti,Clothes,Offline,H,5/17/2017,880811536,7/2/2017,562,109.28,35.84,61415.36,20142.08,41273.28
Europe,Slovakia,Beverages,Offline,L,10/26/2016,174590194,12/4/2016,3973,47.45,31.79,188518.85,126301.67,62217.18
Asia,Sri Lanka,Fruits,Online,L,11/7/2011,830192887,12/18/2011,1379,9.33,6.92,12866.07,9542.68,3323.39
Sub-Saharan Africa,Seychelles ,Beverages,Online,M,1/18/2013,425793445,2/16/2013,597,47.45,31.79,28327.65,18978.63,9349.02
Sub-Saharan Africa,Tanzania,Beverages,Online,L,11/30/2016,659878194,1/16/2017,1476,47.45,31.79,70036.20,46922.04,23114.16
Sub-Saharan Africa,Ghana,Office Supplies,Online,L,3/23/2017,601245963,4/15/2017,896,651.21,524.96,583484.16,470364.16,113120.00
```

# python version
```
$ python --version
Python 3.9.5
```

# test1 - readlines + in operator
```py
import time
fn = '1500000 Sales Records.csv'

st = time.process_time()
r = []
with open(fn) as fp:
    for l in fp.readlines():
        if 'Asia' in l:
            r.append(l)
ft = time.process_time()
print('Elapsed Time:', ft - st)
print('result:', len(r), 'lines')
```
```
$ python go.py
Elapsed Time: 1.234564642
result: 218882 lines
```

# test2 - open + in operator
```py
import time
fn = '1500000 Sales Records.csv'

st = time.process_time()
r = []
for l in open(fn):
    if 'Asia' in l:
        r.append(l)
ft = time.process_time()
print('Elapsed Time:', ft - st)
print('result:', len(r), 'lines')
```
```
$ python go.py
Elapsed Time: 1.093251205
result: 218882 lines
```

# test3 - while readline instead of readlines + in operator
```py
import time
fn = '1500000 Sales Records.csv'

st = time.process_time()
r = []
with open(fn) as fp:
    while True:
        l = fp.readline()
        if 'Asia' in l:
            r.append(l)
        if not l: break
ft = time.process_time()
print('Elapsed Time:', ft - st)
print('result:', len(r), 'lines')
```
```
$ python go.py
Elapsed Time: 1.266936215
result: 218882 lines
```

# test4 - strstr() c function 
* cffi_string.h
```c
char *cffi_strstr (const char *s1, const char *s2);
```

* cffi_string.c
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cffi_string.h"

char *cffi_strstr (const char *s1, const char *s2)
{
    return strstr(s1, s2);
}
```

* cffi_build.py
```py
from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("char *cffi_strstr (const char *s1, const char *s2);")
ffibuilder.set_source("cfficfunc", '#include "cffi_string.h"', sources=["cffi_string.c"])
ffibuilder.compile()
```
```
$ python cffi_build.py
$ ll cfficfunc*
-rw-rw-r-- 1 yuchoe yuchoe 24089 Aug 19 12:31 cfficfunc.c
-rwxrwxr-x 1 yuchoe yuchoe 34768 Aug 19 13:45 cfficfunc.cpython-39-x86_64-linux-gnu.so
-rw-rw-r-- 1 yuchoe yuchoe 32184 Aug 19 13:45 cfficfunc.o
```

* go.py
```py
import time
fn = '1500000 Sales Records.csv'

st = time.process_time()
r = []
for l in open(fn, 'rb'):
    if cffi_strstr(l, b'Asia'):
        r.append(l)
ft = time.process_time()
print('Elapsed Time:', ft - st)
print('result:', len(r), 'lines')
```
```
$ python go.py
Elapsed Time: 0.9503289070000001
result: 218882 lines
```

# conclusion
* `for line in open(fn)` 이 제일 빠름.
* 이 경우 readline/readlines 불필요 
* `in` operator 는 충분히 빠르지만 cffi 로 C 가져다 쓴게 아주 약간 빠르게 됨 

