# 基于的基础镜像
FROM python:3.7.3

# 维护者信息
MAINTAINER 1275556926@163.com

# 代码添加到镜像中的code文件夹（也可以是COPY）
ADD ./docker_test /code

# 设置code文件夹是工作目录
WORKDIR /code

# 安装支持
RUN pip install -r requirements.txt

# 启动项目
CMD ["python", "/code/main.py"]