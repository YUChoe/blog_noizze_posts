
임베디드 장비에서 perl을 쓰다보니, CPAN을 쓸 수 없는 경우가 종종 생긴다. 대부분 pure perl 로 모듈을 재코딩하지만, 번거로운 부분이 많다.
<blockquote>/usr/lib/perl5/site_perl/5.8.1/i386-linux-thread-multi/auto/Digest/SHA/SHA.so
/usr/lib/perl5/site_perl/5.8.1/i386-linux-thread-multi/Digest/SHA.pm
/usr/lib/perl5/5.8.1/Digest.pm
/usr/lib/perl5/5.8.1/Digest/base.pm
/usr/lib/perl5/5.8.1/Digest/file.pm

#!/usr/bin/perl
use Digest::SHA qw(sha256_hex);
print sha256_hex('1234567890@gmail.com');
print "\n"; # EOL

# ./test.pl
42e3fdce10bc335b4f5870af3d6585b1932e3f9dccf2010b5d10f6e436f379fc</blockquote>
python 검증
<blockquote>import hashlib
h = hashlib.sha256(b'1234567890@gmail.com').hexdigest()
print(h)

$ python sha.py
42e3fdce10bc335b4f5870af3d6585b1932e3f9dccf2010b5d10f6e436f379fc</blockquote>