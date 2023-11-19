# SUITTC-IoT

简体中文 | [Englisd](README_en.md)

一个针对SUITTC（辽宁省鑫源温控技术有限公司）物联网设备（优e家）的HACS（Home Assistant社区商店）集成。

[SUITTC-IoT](https://github.com/BoyInTheSun/SUITTC-IoT)是个人项目，目前官方服务可用且正在维护。本插件将温控器以空调的形式接入Home Assistant，无需互联网即可使用。

如果你发现任何问题或者有相关建议，请提issue。

## 安装

todo

## 添加设备

### 支持的设备

由于测试设备有限，其他设备是否支持未知。如果能够为我提供测试环境，我愿意开发对其的支持。

| 类型 | 型号 | 网址 | 开关设备 | 锁定设备 | 目标温度 | 模式切换 | wifi信号强度 | 当前温度 | 点火状态 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 壁挂炉水暖温控器 | WK168无线(WIFI版) | [🔗](http://www.suittc.com/?p=549&a=view&r=605&city_name=) | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |

### 连接前准备

下载官方控制app[优e家](https://sj.qq.com/appdetail/com.ikecin.uehome)，使用其对设备进行联网配置，请记住设备密码。

为了防止设备长期不联网导致IP地址变化，建议在路由器做IP-MAC绑定。

### 自动添加

将设备接入局域网后，即可自动搜索设备。填写设备密码即可，默认`123456`。

注意，如果设备不处于同一网段，可能会添加失败。

### 手动添加

#### SN号

打开优e家app，连接设备后，选择要连接的设备，点击右上角，可以看到由数字组成的设备SN号，形如`123456789012`。

SN号也可以在设备包装等找到。

#### IP地址

关注路由器的已连接设备，将设备接入网络后，记下新出现的设备。设备名可能形如`ESP_123456`。

#### 设备密码

默认为`123456`。

#### 端口

控制端口默认为`60002`，广播端口默认为`60002`。

## 参考

- [Home Assistant 开发者文档](https://developers.home-assistant.io/docs/)

- [integration_blueprint](https://github.com/ludeeus/integration_blueprint)
仓库蓝图，这为开发节省了学习成本。

- [Midea AC LAN](https://github.com/georgezhao2010/midea_ac_lan/)
参考了该项目的部分代码。

- [辽宁省鑫源温控技术有限公司官网](http://www.suittc.com/)
在这里可以找到产品型号信息。没有技术文档。

## 支持我

TODO: 收款码
