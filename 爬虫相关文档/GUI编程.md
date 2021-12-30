## GUI
- 图形用户界面（Graphical User Interface，简称 GUI）

## tkinter
- 简介：tkinter 是 Python 的标准 GUI 库；Python标准库里自带
  - 文档1：https://www.runoob.com/python/python-gui-tkinter.html
  - 文档2: https://docs.python.org/3/library/tkinter.html
- 优点：
  - 小工具，简单，入门级，基础
  - 著名的python IDLE 就是使用 Tkinter 实现 GUI 的
  - 创建的 GUI 简单，学起来和用起来也简单
  - Tkinter的API比较稳定
  - Tkinter就是个单纯的GUI库
- 缺点：
  - 界面相对简陋
  - 提供的控件都是比较基础的
- 使用
  - tkinter.ttk：Tk 风格的控件，tkinter.ttk 模块自 Tk 8.5 开始引入，可用于访问 Tk 风格的控件包；
    tkinter.ttk 的基本设计思路，就是尽可能地把控件的行为代码与实现其外观的代码分离开来。
    【参考】http://tkdocs.com/tutorial/index.html
  - 使用案例：爬虫100例中的例67
  
  - 代码打包（打包成可执行程序）
    - 注意打包的时候，如果程序中设置了软件图标，那么打包的时候，需要调整的代码较多
    - 1、安装打包模块：`pip install pyinstaller`
    - 2、命令行执行：`pyinstaller -F filename/newsimg.py --noconsole`
        - 会在当前命令行所在路径下生成可执行程序