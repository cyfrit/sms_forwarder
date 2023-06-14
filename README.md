# SMS Forwarder--基于随身WiFi的低成本短信转发

### 本项目适用于Linux环境的随身WiFi
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
2. clone或从releases下载
3. 修改config.example.py中的配置，并重命名为config.py
4. 运行
```
python3 main.py
```
5. 使用systemctl(推荐)或screen实现后台运行

以下为systemctl步骤

编辑`/etc/systemd/system/sms_forwarder.service`，添加以下内容，注意实际路径
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
sudo systemctl start sms_forwarder
```
开机自启
```
sudo systemctl enable sms_forwarder
```
***
### 自定义推送函数
在forward.py中添加如下函数：
```
def forward_to_foo(number,content,timestamp):
	#自定推送代码
	pass
```
函数名需以forward_to_开头，传入number,content,timestamp 3个参数
***
### 常见问题
1. Q:收到的短信包含乱码

A:将系统语言修改成使用utf-8的
***
### 免责声明
 本项目的所有内容仅供参考和学习目的，禁止用于商业用途。在使用本项目时，请您遵守所在国家和地区的相关法律法规，不得违反任何法律规定。
 使用本项目的任何内容，即表示您已阅读、理解并同意承担所有责任。无论因何种原因，本项目所有人均不对使用者的任何行为或后果承担任何责任。
 本项目的所有内容仅供参考和学习目的，本人不对这些内容的准确性、完整性和实用性作出任何保证或承诺。
 本项目不会将任何用户的数据传输到项目所有者的服务器上。但如果您使用转发功能，您的数据将被传输到第三方服务器上。在使用转发功能时，请您自行承担风险，并遵守该第三方服务的使用条款和隐私政策。