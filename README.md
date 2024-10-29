# XiaocxPlugin

更新日志0.1

更新了主程序画图命令多次执行不会排队的bug，现在插件每次执行一个请求等2秒继续执行下一个。<br />
更新了主程序的注解，现在全部都有注解了。

## 安装
配置完成 [QChatGPT](https://github.com/RockChinQ/QChatGPT) 主程序后使用管理员账号向机器人发送命令即可安装：<br />

```
!plugin get https://github.com/sanxianxiaohuntun/XiaocxPlugin.git
```
或查看详细的[插件安装说明](https://github.com/RockChinQ/QChatGPT/wiki/5-%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8)
## 目前集成<br />
&nbsp;<br />
/看妹妹（返回cos妹妹图）/看腿 (返回腿照) /色图 (返回有点色的图) /真色图 (返回真的色图) /表情包 (返回二次元表情包) <br />
/毒鸡汤 (返回毒鸡汤) /励志英语 (返回励志英语) /骚话 (返回骚话) /天气 XXXX (返回XXXX天气比如/天气 北京 返回天气北京)<br />
/舔狗日记 （随机生成舔狗日记）/画图(AI绘图)
&nbsp;<br />
<br />
## AI绘图<br />
调用dall-e-3进行绘图（其他太慢了），需要自己拿api和api地址（百度或者自己想办法，买也行）<br />
命令"/画图DALL·E-3 你想要的内容"比如"/画图DALL·E-3 一只可爱的猫娘"，觉得命令长的可以仔细阅读如何修改。<br />
&nbsp;<br />
&nbsp;<br />
效果图
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E7%BB%98%E5%9B%BE%E6%8F%92%E4%BB%B6.png)<br />
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E7%BB%98%E5%9B%BE%E6%8F%92%E4%BB%B62.png)<br />
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E7%BB%98%E5%9B%BE1.png)<br />
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E7%BB%98%E5%9B%BE.png)<br />
 


## 注意<br />
&nbsp;<br />
json色图是非跳转式的随机色图采用json格式返回的参考代码模式
&nbsp;<br />
因为是直接运行.py请不要让它加载任何危险程序！！！（就那种可能盗取数据和带毒的程序！不要运行你根本看不懂的程序！）
&nbsp;<br />

## 注意真色图和色图R18是真的返回R18请注意！！！

## 关于色图小程序<br />
&nbsp;<br />
色图搜和色图R18是带搜索功能的，另外的不带搜索功能（只用于代码学习展示不可用作其他用途）
&nbsp;<br />
## 如何使用色图搜索<br />
&nbsp;<br />
&nbsp;<br />
&nbsp;<br />
在"/色图"和"/色图R18"下空格加要搜索标签比如"/色图 刻晴"即可搜索刻晴的图片R18同理只不过出来的是R18图片。（只用于代码学习展示不可用作其他用途）
&nbsp;<br />
&nbsp;<br />
&nbsp;<br />
## 使用

&nbsp;<br />
这只是一个加载小程序的插件，data里内部包含一些小程序案例，可以让用户自主添加小程序，比如/天气 /色图 /今日运势 之类的各种小功能<br />
&nbsp;<br />
小程序开发及其简单，把你需要的功能告诉gpt然后把我的案例程序代码给GPT，GPT生成后丢到data目录下即可，目前还在更新测试，如何写自己想要的功能请参考下面《小白专用GPT自制插件生成教程》<br />
&nbsp;<br />
## 使用方法：
1.用GPT或者自己写又或者下载的py小程序（只支持图片和文本类）<br />
&nbsp;<br />
2.放到QChatGPT\plugins\XiaocxPlugin\data（该目录以后都简称data目录）<br />
&nbsp;<br />
3.使用/命令启用小插件（放进去后无需重启主程序）比如你放入了文件叫做"色图.py"，你就使用"/色图"命令即可使用，如果要增加小程序把"xxx.py"文件放到插件data目录下文件逻辑写即可，不知道在哪可以看位置图以及上一条<br />
&nbsp;<br />
4.文件类型（可以参考data目录下文件） /命令 xxxx类型文件可参考"天气.py"，图片类型参考"色图.py"<br />
&nbsp;<br />
5.如果"/"命令冲突可以修改QChatGPT\plugins\XiaocxPlugin目录下main.py的"if cleaned_text.startswith('/'):"位置"/"修改为你想要的即可比如：/改为AAA，"if cleaned_text.startswith('AAA')"<br />
&nbsp;<br />
&nbsp;<br />
## 位置图
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E4%BD%8D%E7%BD%AE.png)
&nbsp;<br />
&nbsp;<br />
&nbsp;<br />
## 插件图
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E8%89%B2%E5%9B%BE.png)
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E5%A4%A9%E6%B0%94.png)
![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E5%A4%9A%E4%B8%AA.png)

## 小白专用GPT自制插件生成教程

![before](https://raw.githubusercontent.com/sanxianxiaohuntun/wodecuntu12/refs/heads/main/%E6%95%99%E5%AD%A6.jpg)
