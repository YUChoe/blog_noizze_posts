
백엔드에 다용도로 사용할 데이터저장소로써 mysql, mariadb, postgresql, mongodb, elasticsearch 등을 거의 5년 전 부터 물색하던 중에 특히 Multi-DataCentre-Replication과 CQL이라는 SQL 유사 언어를 사용하는 등의 장점으로 실험적으로 사용하고 있었는데, 이번에 내부 object-storage 프로젝트와 ERP 프로젝트가 동시에 진행되면서 Cassandra 를 도입해 보기로 했다.  (<a href="![](https://www.quora.com/What-are-the-pros-and-cons-of-using-the-Cassandra-database)" target="_blank">Quora에 정리 된 Cassandra의 장단점</a>)

단점으로도 꼽히는 JVM을 이용하는 것이 걸리긴 했는데, 하드디스크는 잡아먹지만 큰 부하를 추가로 주지 않고 개인적으로 Java로 개발하고 운영하는 것을 싫어한 이유는 xml로 된 설정들 탓도 크기 때문에 이는 별로 문제가 되지는 않았음.

&nbsp;
cassandra-driver (3.1.1)
django-cassandra-engine (0.7.4)
six (1.10.0)

&nbsp;