# WeChatOpenDevTools

### 介绍

基于志远老师的WeChatOpenDevTools，用python来实现的。
因为我在win11下node-gyp编译失败，win10环境可以正常用。折腾好几天猜测是因为VS环境的win sdk不匹配。

>注意！！！ 3.9.9以上版本的微信对devtools添加一处检测，目前 已知3.9.9的小程序版本8555中有检测.

>检测点分析： 检测小程序菜单栏中的菜单项是否为devTools

>方案1 打静态或动态补丁修改对应data段 devTools

>方案2 设置小程序目录的8555为不可读不可写 强制不让wx使用8555

>方案3 下载3.9.8 版本或更早版本 其中的8555为无检测版本_

参考链接

https://github.com/x0tools/WeChatOpenDevTools

[志远公开课xcx某信X64DBG自更新教程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Cw411473D/?spm_id_from=333.999.0.0)


[微信历史版本下载](https://github.com/tom-snow/wechat-windows-versions)

---




这是一个专门为爬虫领域制作的库,用来快速调试PC端的微信浏览器和微信小程序.原理是利用Frida Hook微信的配置项,并使用反汇编技术修改了微信的指令集。

**注意只支持 Window 平台！！！！**

注意本库只能作为学习用途, 造成的任何问题与本库开发者无关, 如侵犯到你的权益，请联系删除

**需要提前运行微信.需要提前运行微信.需要提前运行微信**
