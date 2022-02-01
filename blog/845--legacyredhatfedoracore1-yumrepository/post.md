
`/etc/yum.conf`

```ini
[main]
cachedir=/var/cache/yum
debuglevel=2
logfile=/var/log/yum.log
pkgpolicy=newest
distroverpkg=fedora-release
tolerant=1
exactarch=1

[base]
name=Fedora Core $releasever - $basearch - Base
#baseurl=http://fedora.redhat.com/releases/fedora-core-$releasever
baseurl=http://archive.fedoraproject.org/pub/archive/fedora/linux/core/$releasever/i386/os/

[updates-released]
name=Fedora Core $releasever - $basearch - Released Updates
#baseurl=http://fedora.redhat.com/updates/released/fedora-core-$releasever
baseurl=http://archive.fedoraproject.org/pub/archive/fedora/linux/core/updates/$releasever/i386/

#[updates-testing]
#name=Fedora Core $releasever - $basearch - Unreleased Updates
#baseurl=http://fedora.redhat.com/updates/testing/fedora-core-$releasever
```