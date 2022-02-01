
참조 : https://pypi.python.org/pypi/psutil
 
```
>>> import psutil
>>> psutil.net_connections()
[pconn(fd=115, family=, type=, laddr=('10.0.0.1', 48776), raddr=('63.186.135.19', 8080), status='ESTABLISHED', pid=1254),
 pconn(fd=117, family=, type=, laddr=('10.0.0.1', 43761), raddr=('172.17.204.10', 8080), status='CLOSING', pid=2987),
 pconn(fd=-1, family=, type=, laddr=('10.0.0.1', 60759), raddr=('172.17.204.4', 8080), status='ESTABLISHED', pid=None),
 pconn(fd=-1, family=, type=, laddr=('10.0.0.1', 51314), raddr=('172.17.204.183', 443), status='SYN_SENT', pid=None)
 ...]
>>> p = psutil.Process(576)
>>> p.open_files()
[popenfile(path='/home/giampaolo/svn/psutil/somefile', fd=3)]
>>> p.connections()
[pconn(fd=115, family=, type=, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED'),
 pconn(fd=117, family=, type=, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING'),
 pconn(fd=119, family=, type=, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED'),
 pconn(fd=123, family=, type=, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT')]
```