
### openjdk-8-jdk

```
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:openjdk-r/ppa

$ update-alternatives --set java /usr/java/jdk1.8.0_60/bin/java
# update-alternatives --all
```

### cassandra

```
$ sudo gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
$ sudo gpg --export --armor 2B5C1B00 | sudo apt-key add -
$ sudo gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
$ sudo gpg --export --armor 0353B12C | sudo apt-key add -
```

`$ sudo vi /etc/apt/sources.list.d/cassandra.sources.list`

```
deb http://www.apache.org/dist/cassandra/debian 21x main
deb-src http://www.apache.org/dist/cassandra/debian 21x main
```

`$ sudo vi /etc/apt/sources.list.d/openjdk-r-ppa-trusty.list`

```
deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu trusty main
```

```
$ sudo apt-get update
$ sudo apt-get install cassandra
```