
```
$ gcc ex.c
$ ./a.out
datetime: 09-25 12:32:17.871410
```

===

```c
#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <string.h>

static char* datetime(char * buf)
{
  struct timeval tv;
  time_t nowtime;
  struct tm *nowtm;
  char timestrbuf1[64]; timestrbuf1[0] = 0x0;

  gettimeofday(&tv, NULL);
  nowtime = tv.tv_sec;
  nowtm = localtime(&nowtime);

  strftime(timestrbuf1, 64, "%m-%d %H:%M:%S", nowtm);
  sprintf(buf, "%s.%06ld", timestrbuf1, tv.tv_usec);

  return buf;
}

void main()
{
    char buff[128]; buff[0] = 0x00;

    printf("datetime: %s \n", datetime(buff));
}
```
