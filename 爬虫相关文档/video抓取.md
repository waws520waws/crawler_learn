## you-get
- 简介：You-Get是运行在 Python 3 上，是一个小型命令行实用程序，用于从 Web 下载媒体内容（视频、音频、图像）, 目前支持大部分知名网站的抓取
    - 【官方文档】https://pypi.org/project/you-get/0.3.25/，可查看支持的网站及媒体内容
    - 可以看看源码，学习学习
- 安装
    - `pip install you-get`
- 使用
  - 方法1
      - 命令行：`you-get https://www.bilibili.com/video/BV15Z4y1D7Ud【网页url】`
      - 下载得到两个文件：视频文件，弹幕文件
  - 方法2
      - 在python中使用 os.system 执行cmd命令，可添加其他操作
  - 暂停/恢复下载
      - `ctrl + c` 中断下载
      - 下次you-get使用相同的参数运行时，下载进度将从上次会话恢复
  - 设置下载的格式
      - `you-get --format=flv https://www.bilibili.com/video/av2307316`
  - 如果下载出现了问题可以通过以下命令来排除问题：
      - `you-get --debug https://www.bilibili.com/video/av2307316`
  - 设置下载文件的路径和名称
      - `you-get -o ~/Videos -O filename.webm 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`
  - 代理设置
      - `you-get -x 127.0.0.1:8087 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`
  - ffmpeg视频格式转换
      - ffmpeg -i "输入文件名.格式" -c copy "输出文件名.格式"
  
## ffmpeg
- 简介：ffmpeg 有非常强大的功能, 包括: 视频采集、视频格式转换、视频抓图、给视频加水印，合并等功能.
- 安装
  - python安装： `pip install ffmpeg-python`
  - python调用ffmpeg模块，相当于是cmd命令，所以系统也需要安装 ffmpeg
    - 【Mac】先更新brew `brew update` -> `brew install ffmpeg`
- 使用
  - 1）视频与音频合并：
```python
import ffmpeg
input_video = ffmpeg.input('video.mp4')  # 等价于在命令行输入 ffmpeg，所以系统还需要安装 ffmpeg
input_audio = ffmpeg.input('audio.mp3')

# v=1： 设置输出视频流的数量，也就是每个片段中的视频流的数量。默认值为1。
# a=1：设置输出音频流的数量，也就是每个片段中的音频流的数量。默认值为0
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./finish_video1.mp4').run()
```