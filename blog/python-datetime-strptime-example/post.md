
```python
import datetime 

a = "10-12 11:50:14.069208"
b = "10-12 11:50:14.069339"

dt_a = datetime.datetime.strptime(a, "%m-%d %H:%M:%S.%f").replace(year=2021)
dt_b = datetime.datetime.strptime(b, "%m-%d %H:%M:%S.%f").replace(year=2021)

assert (dt_a > dt_b) == False
assert (dt_a < dt_b) == True
```