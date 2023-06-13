# SMS Forwarder--基于随身WiFi的低成本短信转发

### 本项目适用于已配置Linux环境的随身WiFi
***
实现监控短信，通过Email，Telegram进行转发，并支持自定转发函数，以实现转发到其他平台
***
在开始前，请确保你的随身WiFi可以正常使用基带，可通过以下命令确认
```
mmcli -m 0
```
如果无法正常使用，请参考酷安伏莱兮浜大佬的[教程](https://www.coolapk.com/feed/37834896?shareKey=OTQ3NWNhOTZkY2UwNjJkZjRhNDI)，尤其注意文章最后所提到的刷写基带的部分
***
### 目前已实现：
- 自动扫描短信
- 转发到Email，Telegram
### To Do List
- 转发到更多平台（目前计划Bark，Server酱）
- 支持发送短信
***
### 使用
1. 安装python环境
```
sudo apt update && sudo apt install python3
```
2. clone或下载本仓库
```
git clone https://github.com/ryltech/sms_forwarder
```
3. 修改config.example.py中的配置，并重命名为config.py
4. 使用systemctl(推荐)或screen实现后台运行

以下为systemctl步骤

编辑`/etc/systemd/system/sms-forwarder.service`，添加以下内容，注意实际路径
```
[Unit]
Description=SMS Forwarder

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/user/sms_forwarder/main.py

[Install]
WantedBy=multi-user.target
```
重新加载systemctl
```
sudo systemctl daemon-reload
```
启动服务
```
sudo systemctl start sms-forwarder
```
开机自启
```
sudo systemctl enable sms-forwarder
```
***
### 自定推送函数
在forward.py中添加如下函数：
```
def forward_to_foo(number,content,timestamp):
	#自定推送代码
	pass
```
函数名需以forward_to_开头，传入number,content,timestamp 3个参数
***
### 免责声明
本项目仅供交流学习使用，禁止商业用途，请严格遵守您所在国的法律。

任何用户使用SMS Forwarder,本项目作者(ryltech)及其贡献者将不承担任何责任。