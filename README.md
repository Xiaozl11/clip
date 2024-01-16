# clip 基于[clip-interrogator](https://github.com/pharmapsychotic/clip-interrogator)做了一些调整<br>

1.以 **.txt格式**输出到图片文件夹中，可以更方便的进行lora模型的训练<br>

2.支持一次性操作**多个文件夹**中的图片<br>

安装环境：
```
git clone https://github.com/Xiaozl11/clip.git
# 建议使用conda 或者 python 创建在虚拟环境下运行
pip install clip-interrogator==0.5.4
# 根据自己的显卡安装cuda版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

存放图片路径格式：
clip/pic_folder/xxx/yyy.png<br>
xxx为文件夹的名字，
yyy为图片的名字<br>
运行命令为:<br>
```
python x_run_cli.py -f pic_folder/xxx
```

当然，你可以在pic_folder文件夹下存放很多个 xxx_1,xxx_2,...,xxx_n 等很多个子图片文件夹<br>
此时运行的命令为：<br>
```
python x_run_cli_folder.py -f pic_folder
```

更多详细的内容可以参考原作者[README](https://github.com/pharmapsychotic/clip-interrogator/blob/main/README.md)
