
![](drupal2grav.png)
* blog를 어느정도 사용 할 수 있을 정도가 되면 회사 홈페이지도 다시 구성 하려고 했는데 
* 결국 Drupal 의 복잡한 구조를 빠르게 다 이해하지 못해서 카테고리 라든지 static page 등을 보여주는 걸 못했고
* Adsense 플러그인 하고 뭐가 안 맞는지 결국은 광고를 유치하는데 실패 
* drupal 관련파일만 800메가고 sites 이하 커스텀 파일만 130메가.. 덩치가 불필요하게 큰게 아닌가?
* 또 sqlite3 를 썼는데 아주 못마땅한 성능이 나왔음. 포스트는 200개 정도 밖에 안되는데 이건 너무한게 아닌가 싶을 정도로
* Ghost 를 도입 했지만 설치과정에서 raspberri pi 3 에서는 메모리부족등의 이유로 진행이 어려웠고 
* 마찬가지로 도입을 하더라도 커스텀 하고 광고 유치 하는데 상당한 노력이 필요 할 것 같아서 
* 결국 Grav에 정착 결정 
* 일단은 구조가 나름 단순해서 
* 기존 포스트들을 migration 하는데는 따로 툴을 만들어야 했고 [링크](https://github.com/YUChoe/ghost2grav) 
* 워드프레스에서 [code] [embed] 등 특수 기능들을 많이 가져다 써서 일일이 바꿔줘야 하는 불편함이 있고
* 이미지 등은 복구가 힘들 것 같지만 기억과 백업을 통해 복구 할 수 있는 것들은 천천히 진행 하기로 함 

### TODO
* [x] https 인증서 이전 및 서비스 적용 
* [x] http to https redirection 
* [x] alphacom365의 static page migration 
* [x] solvigchoi.co.uk blog migration
* [ ] degustezlemonde.wordpress.com blog migration
* [x] Remove Grav footer 
* [x] Sidebar 정리 [tags](https://github.com/getgrav/grav-plugin-taxonomylist/issues/24)
* [x] disqus comment - comments.html.twig 를 많이 수정 했어야 했음 
* [x] Adsense 
* [x] Title Header Text/Logo 
* [ ] Project page 
* [ ] CV page 
* [x] mobile 에서 Title icon 이 default 로 나오는 문제
* [x] NAS Backup (daily)
