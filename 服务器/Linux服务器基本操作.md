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
- 2）如何让项目在此python环境下运行？
    - 方法1：可在python文件中添加 `sys.path.append(path)` （path为包所在路径）（先添加包路径，再导入包）
        - `sys.path.append('/home/jieyangali/anaconda3/envs/crawler37/lib/python3.7/site-packages')`
    - 方法2：命令行执行项目之前先导入环境：`export PYTHONPATH=~/projects/vnf_flow:$PYTHONPATH`
    - 或者先将路径写入到系统环境中 /etc/profile 或 ~/.bashrc（记得执行`source ~/.bashrc`让其生效）
- 3）可以将这些命令添加到一个定时执行的脚本中，利用linux的定时任务（crontab）来跑