## anaconda3
### 1、conda常用命令
- `conda create -n env_name python=3.6.5`       创建环境
- `conda create -n env_name python=3.7 pandas numpy keras`  conda create -n 环境名称 python=3 包1 包2 包3
- `source(conda) activate env_name`	                激活环境(新版的变成使用conda激活)
- `source deactivate`		                    退出当前环境
- `conda env list`	                            有哪些环境
- `conda remove -n my_py_env --all`             删除环境
