
http://python-twitter.googlecode.com 의 파이썬 모듈을 이용해서 일일 다이제스트 기능을 구현 해보려 하는데..
일단 UserTimeline 을 가져오는 예제는 돌려서 성공 ~~했는데 10월 20일 이후로 16개 달랑 받아 옴...~~(해결)
하루치.. 날짜별로 가져오는건 힘들라나 ?
하루에 2~3개의 트윗을 하고 5개 정도 ReTweet을 하는데 리트윗한 것을 가져오려면 인증이 필요할라나

XAuth 가 귀찮긴 귀찮구나 -_-

```python
# python 2.7
import twitter
api = twitter.Api()
usertimeline = api.GetUserTimeline(user = 'someones id', count = 100)
print [s.text for s in usertimeline]
```