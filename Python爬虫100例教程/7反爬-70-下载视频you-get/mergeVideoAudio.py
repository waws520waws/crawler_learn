'''
合并 无声视频 与 音频
'''

import ffmpeg

input_video = ffmpeg.input('video.mp4')  # 等价于在命令行输入 ffmpeg，所以系统还需要安装 ffmpeg
input_audio = ffmpeg.input('audio.mp3')

# v=1： 设置输出视频流的数量，也就是每个片段中的视频流的数量。默认值为1。
# a=1：设置输出音频流的数量，也就是每个片段中的音频流的数量。默认值为0
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./finish_video1.mp4').run()
