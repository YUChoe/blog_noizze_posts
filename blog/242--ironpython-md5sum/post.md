
<pre><code>from System.Text import StringBuilder
from System.IO import FileStream, FileMode
from System.Security.Cryptography import MD5CryptoServiceProvider

filename = &quot;aaa.mp4&quot;
sb = StringBuilder()
fs = FileStream(filename, FileMode.Open)
md5 = MD5CryptoServiceProvider()
hash = md5.ComputeHash(fs)
fs.Close()
for hex in hash :
sb.Append(hex.ToString(&quot;x2&quot;))
print sb.ToString()</code></pre> 