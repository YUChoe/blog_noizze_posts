
```
/opt/eff.org/certbot/venv/bin/python: No module named pip.__main__; 'pip' is a package and cannot be directly executed
```

메시지와 함께 pip --version 을 확인 할 수 없다는 메시지가 출력되는데, 원인은 python 버전이 낮은 등의 이유로 vertualenv 가 정상적으로 작동하지 못하는 것이고 

`letsencrypt-auto` 파일의 약 1500, 1511번 줄의 (버전마다 다를 수 있음) 코드를 

```python
# pip_version = StrictVersion(check_output(['/opt/eff.org/certbot/venv/bin/python', '-m', 'pip', '--version'])
pip_version = StrictVersion(check_output(['pip', '--version'])
...

# command = ['python', '-m', 'pip', 'install', '--no-index', '--no-deps', '-U']
command = ['pip', 'install', '--no-index', '--no-deps', '-U']
```

위와 같이 변경 해 주면 일단 실행이 된다. 

12.04는 이제 더이상 유지보수가 안 되고 있어서 바꾸고 싶지만 내 서버가 아니므로 일이 쉽지가 않구나. ㅠㅠ