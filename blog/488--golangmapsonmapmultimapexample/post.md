
&nbsp;
<pre class="lang:go decode:true">package main

import "fmt"

func main() {
  var wan map[int]map[string]string
  wan = make( map[int]map[string]string )

  wan[1] = make(map[string]string)
  wan[1]["int"] = "eth1"

  fmt.Println(wan)
  fmt.Println( wan[1]["int"] )
}</pre>
result :

map[1:map[int:eth1]]
eth1