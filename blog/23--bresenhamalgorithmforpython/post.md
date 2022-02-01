
![](http://poorpuppet.egloos.com/4109119) 에서 이동

<pre><code>def __drawLine(startX, startY, destX, destY) :
  # 변수 초기화
  path = []
  error = 0

  orginalX = startX
  originalY = startY

  # x2 &gt;= x1, y2 &gt; y1 이 되도록 한다.
  if startX &gt; dx :
    (startX, dx) = (dx, startX)

  if startY &gt; dy :
    (startY, dy) = (dy, startY)

  delta_x = dx - startX
  delta_y = dy - startY

  path.append( [startX, startY] )

  if delta_x &gt; delta_y :
    y = startY
    half = int( delta_x / 2 )
    for x in range((startX+1), dx) :
      error += delta_y
      if error &gt; half :
        y += 1
        error -= delta_x
      path.append([x, y])
  else :
    x = startX
    half = int( delta_y / 2 )
    for y in range((startY+1), dy) :
      error += delta_x
      if error &gt; half :
        x += 1
        error -= delta_y
      path.append([x, y])

  return path</code></pre>

<del>변수값 swap 할때 python식의 더 나은 방법이 필요한데 귀찮고 시간이 없어서 저런 식으로 구현을 ;</del>

2011-01-07 수정