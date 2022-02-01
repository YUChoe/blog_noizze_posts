
```
$ python /home/dev/analyze.py
Traceback (most recent call last):
File "/home/dev/analyze.py", line 105, in &lt;module&gt;
table.add_rows(ordered)
File "/home/dev/venv3/lib/python3.4/site-packages/texttable.py", line 361, in add_rows
self.add_row(row)
File "/home/dev/venv3/lib/python3.4/site-packages/texttable.py", line 340, in add_row
cells.append(self._str(i, x))
File "/home/dev/venv3/lib/python3.4/site-packages/texttable.py", line 413, in _str
if f - round(f) == 0:
OverflowError: cannot convert float infinity to integer
```

위와 같은 에러가 갑자기 나기 시작해서 살펴보니

```
$ pip list | grep texttable
texttable (0.9.1)
```

```
$ pip install texttable --upgrade
Downloading/unpacking texttable from https://pypi.python.org/packages/ba/16/ac997890d27d6a78e4bcb379ecd9ce105a0d923f4fefff2eb0c489697da0/texttable-1.2.1.tar.gz#md5=7761da214368903c2409c13f1280cffe
Downloading texttable-1.2.1.tar.gz
Running setup.py (path:/home/dev/venv3/build/texttable/setup.py) egg_info for package texttable

Installing collected packages: texttable
Found existing installation: texttable 0.9.1
Uninstalling texttable:
Successfully uninstalled texttable
Running setup.py install for texttable

Successfully installed texttable
Cleaning up...
```

0.9.1 을 1.2.1 로 업그레이드하고 정상 작동