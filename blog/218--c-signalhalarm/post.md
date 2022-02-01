
루프와는 별개로 3초 마다 이벤트를 발생시키는 예제

<pre><code>#include &lt;stdio.h&gt;
#include &lt;signal.h&gt;

void ActiveSignal(void);
void AlarmRun(void);

void ActiveSignal(void)
{
  struct sigaction act;
  act.sa_handler = AlarmRun;
  sigemptyset(&amp;act.sa_mask);
  act.sa_flags = 0;
  sigaction(SIGALRM, &amp;act, NULL);
}
void AlarmRun(void)
{
  printf(&quot;signal!!! &quot;);
  fflush(0);
  alarm(3);
}
int main(void)
{
  ActiveSignal(); // start alarm
  signal(SIGALRM, AlarmRun);
  alarm(3);
  while (1)
  {
    printf(&quot;.&quot;);
    fflush(0);
    sleep(1);
  }
  return 0;
}</code></pre> 