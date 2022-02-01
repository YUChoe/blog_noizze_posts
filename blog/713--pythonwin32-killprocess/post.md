
```python
import psutil

pid=5572
p = psutil.Process(pid)
p.kill()
```