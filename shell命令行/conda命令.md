## anaconda3
### 1、conda常用命令
- `conda create -n env_name python=3.6.5`       创建环境
- `conda create -n env_name python=3.7 pandas numpy keras`  conda create -n 环境名称 python=3 包1 包2 包3
- `conda activate env_name`	                激活环境(新版的变成使用conda激活)
- `conda deactivate`		                    退出当前环境
- `conda env list`	                            有哪些环境
- `conda remove -n my_py_env --all`             删除环境
- `pip list` 查看当前环境下已安装的包

## 一次性安装所有包
- `pip3 install -r requirements.txt`
- requirements.txt 文件的内容：
    ```text
    telethon
    requests
    pillow
    aiohttp
    hachoir
    ```

## 生成 requirements.txt 文件
- 方法1
  
  - 只生成当前目录下用到的包
  
    ```python
    # 安装pipreqs
    pip install pipreqs
    # 在当前目录生成requirement依赖
    # --force 为强制执行，如果当前生成目录下的requirements.txt存在时，则直接覆盖
    pipreqs . --encoding=utf8 --force
    ```
  
- 方法2

  - pycharm工具栏 —— `Tools` —— `Sync Python requirements`
  - 注意：此方法会生成当前pycharm打开的文件所用到的包

- 方法3
  - `pip freeze > requirements.txt` 当前python环境下的所有已安装包