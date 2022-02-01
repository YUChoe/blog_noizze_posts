
pcap 파일을 분석 할 일이 자주 생겨서 틀을 만들려고 하는데, 가장 가벼워 보이는 pyshark 를 쓰기로 했다. 

```python
import pyshark

for packet in pyshark.FileCapture('dump-20200113-203532.pcap'):
    if 'IP' in packet:
        print(packet.sniff_time, packet.ip.src, packet.ip.dst)
```

그런데 이 예제 대로 하면  자꾸 pcap 파일의 맨 마지막 자료에서 OSError, `RuntimeError: Event loop is closed` 등의 에러를 뱉어 내서 방법을 찾아보니 다음 처럼 구현 하면 될 것 같아서 기록. 

```python
import pyshark

with pyshark.FileCapture('dump-20200113-203532.pcap') as pcap:
    for packet in pcap:
        if 'IP' in packet:
            print(packet.sniff_time, packet.ip.src, packet.ip.dst)
```

