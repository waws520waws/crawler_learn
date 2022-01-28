### 1、连接服务器
- Mac
  - `ssh root@47.101.158.121`
  - or `ssh usrname@47.101.158.121`
  - `Ctrl + D` or `exit` 断开连接
- Win
  - 先安装 xshell

### 2、新建用户并授权
- 【参考】https://www.cnblogs.com/lovelygang/p/11177794.html
- 1）新建用户 jieyang：`adduser jieyang`
- 2）为新用户创建初始化密码：`passwd jieyang`
- 3）为用户授权
- 4）切换用户
    - `su 用户名` 或 `su - 用户名` ：前者只是切换了用户(不需要密码)，要想连shell环境一起切换就用后边的(需要用户密码)。
  
### 3、项目部署到服务器
- Mac
  - 【参考】https://blog.csdn.net/lulusGirl/article/details/106690671
  - 1）项目打包(.tar) 或者 压缩(.zip)
  - 2）执行 `scp project_name.zip usrname@xx.xx.xx.xxx:/home/jieyang/data`
      - usrname : 服务器用户
      - xx.xx.xx.xxx ：服务器地址
      - /home/jieyang/data ：传输到哪个路径下

### 4、服务器上运行项目
- 1）在服务器上安装python环境
    - 可以安装miniconda（anaconda比较大）：https://repo.anaconda.com/miniconda
- 2）如何让项目在此python环境下运行？(我想使用conda环境)
    - 方法1：可在python文件中添加 `sys.path.append(path)` （path为包所在路径）（先添加包路径，再导入包）
        - `sys.path.append('/home/jieyangali/anaconda3/envs/crawler37/lib/python3.7/site-packages')`
        - 系统环境里有python3命令，执行 `python3 pyfile.py`
        - 命令前加上 `nohup`，即使断开连接程序依然会运行（后台运行脚本）： `nohup python pyfile.py`
      
    - 方法2：命令行执行项目之前先导入环境：`export PYTHONPATH=~/projects/vnf_flow:$PYTHONPATH`  
            或者先将路径写入到系统环境中 /etc/profile 或 ~/.bashrc（记得执行`source ~/.bashrc`让其生效）
        - 此时运行 `python pyfile.py` ，发现并没有使用所配置环境下的python（可以在脚本中导入模块试试）
        - 原因：系统会优先找 /usr/bin 下的启动文件，此时，进入/usr/bin，建立软连接（让此python指向我们配置的环境下的python）
            - `ln -s /home/jieyangali/anaconda3/envs/crawler37/bin/python ./python`
    
    - 方法3：先激活conda环境（`source activate crawler37`），这时可直接执行 python命令

    - 方法4：在定时脚本中，先写一些命令进入到conda环境目录下（或者先激活conda环境），再写执行项目的命令

- 2））不用conda环境，如何配置python环境并运行？
    - 阿里云自带 python3
        - `which python3` 查看路径
        - `python3 -V` 查看版本
        - `python3 -m pip install requests` 安装依赖包
        - `nohup python3 -u jxbfd.py >out.log 2>&1 &` 后台运行脚本
        -  `cat out.log` 查看日志
    - 此方法是在root下安装环境，不会污染环境吗？
    
- 3）可以将这些命令添加到一个定时执行的脚本中，利用linux的定时任务（crontab）来跑
    - 【参考】https://mapengsen.blog.csdn.net/article/details/109016423
        - `systemctl start crond`  启动服务 
        - `systemctl stop crond`  关闭服务 
        - `systemctl restart crond`  重启服务 
        - `systemctl reload crond`  重新载入配置
        - `service  crond status`  查看crontab运行状态
        - `chkconfig –level 35 crond on` 或 `chkconfig crond on`  加入开机自动启动
    - 定时crontab
        - `*/1 * * * * sh /home/jieyangali/test.sh > /home/jieyangali/crontab_shell.log 2>&1 &`
            - 解释：每分钟执行一次后面的命令
            - `>` 将输出重定向到log文件（通常是输出到终端，这里是输出到文件）（以覆盖的方式）
            - `>>` （以追加的方式）【参考：https://www.runoob.com/linux/linux-shell-io-redirections.html】
            - `2>&1` 将错误重定向到标准输出（而输出使用了 `>` 重定向到了log文件），所以log文件中会记录错误信息
            - 最后的 `&` 表示把该命令以 后台方式 执行
            
        - crontab定时任务中使用python相关命令要 **写全命令安装路径**
            - 例如：使用python执行py文件 `~/anaconda3/bin/python /home/jieyangali/project111/myfirst.py`
            - `which python` or `whereis python` 查看路径
      
- 3））scrapydweb中也可以定时
    

### 5、服务器上安装mongodb（centos）
- 【参考】https://www.cnblogs.com/zhenling/p/14415116.html
    - 此种方法安装后的配置文件在：/etc/mongodb.conf
- 添加用户
    - 【参考】https://www.cnblogs.com/stardust233/p/12193850.html

- 常用命令
    - `systemctl status mongod.service`　　 # 查看mongod状态
    - `systemctl start mongod.service`　　  # 启动
    - `systemctl stop mongod.service` 　　  # 停止
    - `systemctl enable mongod.service` 　　# 自启
    - `mongo`   进入mongodb

- 出现的问题
    - 1）注意配置文件（mongodb.conf）中的参数值的格式（值不加引号）
        ```commandline
        security:
          authorization: enabled   # disable or enabled
        ```
    - 2）无法启动服务（像自定义的方式）
        - 【参考】https://www.cnblogs.com/lax-17xu/p/11660700.html
        - 但是这种方法要启动两个终端（需要先运行 mongod）
    - 3）端口问题（mongodb远程连接不上）
        - 阿里云有个**安全组规则**，需要在里面打开需要用到的端口