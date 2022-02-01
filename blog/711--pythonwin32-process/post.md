
```python
# -*- coding: utf-8 -*-
from win32com.client import GetObject

WMI = GetObject('winmgmts:')

processes = WMI.InstancesOf('Win32_Process')

for p in processes :
  _p_name = p.Properties_('Name').Value
  _p_pid = p.Properties_('ProcessId').Value
```

```
>>> import psutil
>>> psutil.pids()
[1, 2, 3, 4, 5, 6, 7, 46, 48, 50, 51, 178, 182, 222, 223, 224,
 268, 1215, 1216, 1220, 1221, 1243, 1244, 1301, 1601, 2237, 2355,
 2637, 2774, 3932, 4176, 4177, 4185, 4187, 4189, 4225, 4243, 4245,
 4263, 4282, 4306, 4311, 4312, 4313, 4314, 4337, 4339, 4357, 4358,
 4363, 4383, 4395, 4408, 4433, 4443, 4445, 4446, 5167, 5234, 5235,
 5252, 5318, 5424, 5644, 6987, 7054, 7055, 7071]
```