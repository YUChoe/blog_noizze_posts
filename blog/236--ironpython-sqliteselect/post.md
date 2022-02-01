

```python
import clr
clr.AddReferenceToFile("System.Data.SQLite.DLL")
from System.Data.SQLite import *

mySelectQuery = "SELECT * FROM testtable"
sqConnection = SQLiteConnection('Data Source=mydatabase.sqlite')
sqCommand = SQLiteCommand(mySelectQuery, sqConnection)
sqConnection.Open()
sqReader = sqCommand.ExecuteReader()

while sqReader.Read() :
    print sqReader[0], sqReader[1]

sqReader.Close()
sqConnection.Close()
```
