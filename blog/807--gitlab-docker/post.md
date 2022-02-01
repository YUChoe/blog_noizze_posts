
<img class="aligncenter wp-image-756" src="![](http://noizze.net/wp-content/uploads/2015/12/gitlab_logo.png)" alt="gitlab_logo" width="501" height="178" />

회사에서 내부 레포지토리/이슈관리/위키 용도로 gitlab을 운영 해 온지 3년이 지났는데 중간에 하드디스크 패일 등으로 날려먹은게 2번이고 업그레이드 잘 못해서 롤백하는 등 운영상 우여곡절과 부담이 많이 되는 상황이어서 아래의 선택지 중 하나를 택하는 것이 좋지 않을까 생각을 해 봤다.
<ol>
 	<li>bitbucket 과 같은 private repogitory 를 운영 할 수 있는 곳으로 이동</li>
 	<li>github 유료 서비스 이용</li>
 	<li>gitlab 을 그대로 쓰되 docker 패키지로 업그레이드 등을 관리 Dockerized GitLab <a href="![](https://github.com/sameersbn/docker-gitlab)" target="_blank">![](https://github.com/sameersbn/docker-gitlab</a></li>)
 	<li>gitlab 을 그대로 유지</li>
</ol>
운영상 문제
요즘(한 버전 7.x 부터?) 이나 되어서야 업그레이드가 그나마 편해졌지 그 전에는 큰 맘먹고 해 봐야 하는 정도였다. 물론 8.x 올라가면서 지금은 서비스내리고-백업하고-git fetch-git checkout-db마이그레이션-asset마이그레이션-설정/init스크립트-서비스올리기 정도로 끝나니까 큰 문제가 없다고 쳐도

&nbsp;

결론

결국은 ![](http://theterminallife.com/migrating-gitlab-to-gitlab-omnibus/) 버전으로 가기로 결정