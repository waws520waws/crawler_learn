### 1、连接服务器
- Mac
  - `ssh root@47.101.158.121`
  - or `ssh usrname@47.101.158.121`
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
    
    - 方法3：在定时脚本中，先写一些命令进入到conda环境下，再写执行项目的命令

- 2））不用conda环境，如何配置python环境并运行？
    - 阿里云自带 python3
        - `which python3` 查看路径
        - `python3 -V` 查看版本
        - `python3 -m pip install requests` 安装依赖包
        - `nohup python3 -u jxbfd.py >out.log 2>&1 &` 后台运行脚本
        -  `cat out.log` 查看日志
    - 此方法是在root下安装环境，不会污染环境吗？
    
- 3）可以将这些命令添加到一个定时执行的脚本中，利用linux的定时任务（crontab）来跑


### 5、服务器上安装mongodb（centos）
- 【参考】https://www.cnblogs.com/zhenling/p/14415116.html
- 添加用户
    - 【参考】https://www.cnblogs.com/stardust233/p/12193850.html

- 常用命令
    - `systemctl status mongod.service`　　 # 查看mongod状态
    - `systemctl start mongod.service`　　  # 启动
    - `systemctl stop mongod.service` 　　  # 停止
    - `systemctl enable mongod.service` 　　# 自启
    - `mongo`   进入mongodb