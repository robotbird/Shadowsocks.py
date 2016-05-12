# fq神器Shadowsocks自动获取密码 

### 自动获取Shadowsocks密码，并打开Shadowsocks.exe （暂时只有windows)

* Shadowsocks 下载地址：http://www.ishadowsocks.net/#download
> 第一次需要运行Shadowsocks.exe，填写服务器ip，端口密码，选择加密方式，确定后会在当前目录生成gui-config.json文件，
因为shadowscoks每隔6个小时自动更改密码，所以如果超时之后，需要关闭重新运行shadowsocks.exe，所以写了一个python程序用于自动获取密码并且自动运行exe文件

* 运行Shadowsocks.py 之前须安装python2.7环境
* 将Shadowsocks.py 跟Shadowsocks.exe 放在同一个文件夹
* 直接运行 Shadowsocks.py 就可以翻墙了
* 如果不能正常输出8位数密码则 欢迎在issues里提交反馈，我会在github里第一时间更新此py代码

