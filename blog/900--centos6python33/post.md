
아직 CentOS6 를 사용 하는 서버가 많고, 사용하는 python은 2.7에서 3.3, 3.4로 모두 넘어갔지만 centos 와 epel 레포지토리는 아직 python3를 지원하지 않고 있다. 

<blockquote>
# yum install centos-release-SCL
# yum update
# yum install python33-python python33-python-virtualenv
# scl enable python33 bash
# virtualenv -p /opt/rh/python33/root/usr/bin/python3.3 venv3
# . venv3/bin/activate
(venv3)# pip -V
pip 1.4.1 from /root/venv3/lib/python3.3/site-packages (python 3.3)</blockquote>
