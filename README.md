# CheckHustBalance
> **用于查询和充值华中科技大学饭卡**

> 每次想要查询饭卡余额 或者 想要充钱的时候都莫名烦躁，因为又要打开又卡又满的微校园系统。最近在 Gtihub 上看到不少校友的登录代码，于是稍加修改，做成了一个可以查询和充值饭卡的程序，感谢无私奉献的大神们！

## 特别声明:
> **注意**： 本人是小白，只是根据几个大佬校友的脚本增添了此功能，如有建议欢迎指出。本项目仅用作技术交流，本人不对使用本脚本所产生的任何后果负责，请使用者学习原理后自行删除。
* 本仓库发布的项目中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断.

* 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

* chenyucheng0503 对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害.

* 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, chenyucheng0503 对于由此引起的任何隐私泄漏或其他后果概不负责.

* 请勿将该项目的任何内容用于商业或非法目的，否则后果自负.

* 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本.

* 任何以任何方式查看此项目的人或直接或间接使用该该项目的任何脚本的使用者都应仔细阅读此声明。chenyucheng0503 保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明.

 **您必须在下载后的24小时内从计算机或手机中完全删除以上内容.**  </br>


## 用法

### 推荐: Request 方法
> ### 本地运行
> 1. 安装相关依赖：运行以下代码  
     `python setup.py install`
> 2. 

<br></br>
<br></br>
### ~~Selenium 方法（已经放弃）~~
> 由于使用 selenium 比较慢。而且在 VPS 上运行会出现一个`BUG`（当 Chrome 设置为 headless 时，无法正常显示下半部分菜单，只能查询余额。但是在我的 CentOS 上很难配置非 headless 模式，当然也不排除是我不会。加上已经研究出来更为方便的 Request 方法，所以弃用了此方法，有兴趣的同学可以自己研究以下，具体代码见 Selenium 文件夹）

> ### 本地运行
> 1. 打开 check_balance.py 文件，在`acount`处填写学号，在`password`处填写密码。
> 2. 配置 selenium 环境，具体参见 [这篇文章](https://www.cnblogs.com/Neeo/articles/10671532.html)
> 3. 如果要**查询余额**，只需执行 `get_account` 函数, 将 `recharge` 函数禁用
> 4. 如果要**充值饭卡**，只需执行 `recharge` 函数, 将 `get_account` 函数禁用。在函数的第一个参数填写你要充值的数值，第二个参数输入你的饭卡充值密码（六位数）
> 5. **注意** 充值饭卡会输出当前余额，两个函数无法同时执行，请务必根据自己的需求调整

> ### 部署到 VPS 上 (建议)
> ~~selenium版存在问题，等放假了会研究一下直接 request 请求 ajax 来实现的。~~  
> 
> 已经解决，请使用 Request 方法。


# 特别感谢
特别感谢以下几位大佬做出的贡献（排名不分先后）  
[@naivekun](https://github.com/naivekun/libhustpass)  
[@CrossHustWall](https://github.com/CrossHustWall)  

