# nslookup命令

> 类似于 Linux 中的 dig 命令

## 用法
```powershell
用法:
   nslookup [-opt ...]             # 使用默认服务器的交互模式
   nslookup [-opt ...] - server    # 使用 "server" 的交互模式
   nslookup [-opt ...] host        # 仅查找使用默认服务器的 "host"
   nslookup [-opt ...] host server # 仅查找使用 "server" 的 "host"
```

查看DNS记录的网址对应的IP
```powershell
PS C:\Users\pinesnow> nslookup github.com 223.5.5.5
服务器:  public1.alidns.com
Address:  223.5.5.5

非权威应答:
名称:    github.com
Address:  13.229.188.59
```