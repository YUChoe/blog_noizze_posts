
Usage:
```
# journalctl -fu {service name}
```

Example: 
```
# journalctl -fu ntpd
-- Logs begin at Fri 2020-01-17 07:53:02 KST. --
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 9 lo ::1 UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 10 eth4 fe80::3efd:feff:feed:82b UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 11 p2p4 fe80::3efd:feff:feed:823 UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 12 eth0 fe80::b226:28ff:fe93:7d3f UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 13 eth1 fe80::b226:28ff:fe93:7d3e UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listen normally on 14 eth6 fe80::b226:28ff:fe93:7514 UDP 123
Feb 24 19:35:47 SBC1-1 ntpd[25165]: Listening on routing socket on fd #31 for interface updates
Feb 24 19:35:47 SBC1-1 ntpd[25165]: 0.0.0.0 c016 06 restart
Feb 24 19:35:47 SBC1-1 ntpd[25165]: 0.0.0.0 c012 02 freq_set kernel 0.000 PPM
Feb 24 19:35:47 SBC1-1 ntpd[25165]: 0.0.0.0 c011 01 freq_not_set
```