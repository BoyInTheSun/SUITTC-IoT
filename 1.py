# coding=UTF-8

from socket import *
import time

# IP地址为空""表示接收任何网段的广播消息
# IP地址也可以填 "0.0.0.0"
address = ("", 60002)

# 创建流式socket
s = socket(AF_INET, SOCK_DGRAM)

# 设置socket属性
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.settimeout(3)

# 绑定本地ip地址和端口
s.bind(address)

print("wait recv...")
while True:

    # 接收消息
    data, address_rx = s.recvfrom(65536)

    print("[recv form %s:%d]:%s" % (address_rx[0], address_rx[1], data))
    
    time.sleep(1)

# 关闭socket
s.close()

