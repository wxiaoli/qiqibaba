# 七七八八

- [七七八八](#七七八八)
  - [系统相关](#系统相关)
  - [python环境配置相关](#python环境配置相关)
    - [jupyter-server配置](#jupyter-server配置)
  - [其它](#其它)
***

## 系统相关

**WINDOWS应用**  
```
- windows后台运行jupyter notebook并重定向禁止其输出信息：
    start /b jupyter notebook >nul 2>nul &
- 查看端口占用：netstat -ano|findstr "8888"  
```
**Linux应用**  
```
- 查看某一端口的占用情况： lsof -i:端口号
- 查看显卡信息：lspci | grep -i vga（nvidia） 
- 查看操作系统版本：cat /etc/issue
- 查看cuda版本： cat /usr/local/cuda/version.txt 或 nvcc -v
- 查看cudnn版本： cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
- 显卡应用情况：nvidia-smi 
- 启动ssh服务：/etc/init.d/ssh start
- scp -r E:\curforlpr username@<server ip>:path //注：是把整个curforlpr文件夹传过去
- cudann: cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
- tar -zxvf cars_train.tgz
- 远程端口映射：
  ssh -N -f -L localhost:8889:localhost:8888 -p port username@mapped_ip  
  localhost:8889 指本地端口   
  localhost:8888指远程服务器端口 
```

## python环境配置相关
**conda**  
```
- conda create -n your_env_name python=3.X
- conda remove -n env_name --all
- conda update -n base -c defaults conda //更新conda版本

- conda activate 环境名

- conda deactivate 
- conda config --show #查看已经安装过的镜像源
- conda config --add channels https://mirrors...
- conda config --remove channels https://mirrors... 
- conda config --set show_channel_urls yes

- conda安装pytorch加速镜像
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

python -m pip install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
pip源： https://pypi.douban.com/simple
安装包 bak：
python -m pip install jieba matplotlib simplejson pandas seaborn

conda安装pytorch加速镜像
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

conda config --set show_channel_urls yes

conda install pytorch torchvision torchaudio cpuonly
```

### jupyter-server配置
[jupyter基本配置](https://www.cnblogs.com/wxiaoli/p/10648251.html) 
```  
python -m pip install jupyter -i https://pypi.doubanio.com/simple
jupyter notebook --generate-config
附加：
配置jupyter密码：  
>>> from notebook.auth import passwd  
>>> passwd() 

后台运行jupyter: nohup jupyter notebook &  
解释:   
用&让命令后台运行, 并把标准输出写入jupyter.log中;  
nohup表示no hang up, 就是不挂起, 于是这个命令执行后即使终端退出, 也不会停止运行。  
终止进程：  
用【ps -ef | grep jupyter】查看进程pid。 
然后用【kill -9 <进程号>】终止主进程jupyter-notebook关闭jupyter server。   

在python环境中安装jupyter内核：
　　python -m pip install ipykernel -i https://pypi.douban.com/simple
　　python -m ipykernel install --user --name  [yourkernelname]

jupyter kernelspec list
jupyter kernelspec remove kernelname
notebook中高亮显示和代码补齐等：
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user --skip-running-check
然后开启jupyter服务后在主界面[Nbextensions]选项卡中配置。
```
[其他奇奇怪怪的问题](https://www.cnblogs.com/wxiaoli/p/13094327.html)  

## 其它 
```
MYSQL
  - 安装包下载： https://dev.mysql.com/downloads/windows/installer/8.0.html
  - vscode做mysql客户端配置：https://blog.csdn.net/Gineyc/article/details/103227874  

正则表达式**：https://www.liujiangblog.com/course/python/73  

树莓派  
  usb免驱动声卡 - 麦克风
  查看树莓派型号：cat /proc/device-tree/model
  查看CPU：cat /proc/cpuinfo 
  Raspberry Pi 3B 麦克风安装： http://www.alsrobot.cn/goods-579.html
  aplay有的声音播放不出来。
  用sox播放音频：
  sudo apt-get install sox
  sudo apt-get install sox libsox-fmt-all

ALSA (Advanced Linux Sound Architecture),是一个完全开放源代码的音频驱动程序集.  
  arecord -l  
  alsamixer  
  arecord -D plughw:1,0 -f S16_LE -c 1 -r 16000 -t wav q1.wav -d 5  
  查询声卡 id: cat /proc/asound/cards   
  aplay test.wav
  arecord -D plughw:1,0 -f S16_LE -c 1 -d 10 -r 16000 -t wav ./test.wav
  参数解析
  -D 指定了录音设备，0,1 是card 0 device 1的意思，也就是TDM_Capture
  -d 指定录音的时长，单位秒
  -f 指定录音格式
  -r 指定了采样率，单位时Hz
  -c 指定channel 个数
  -t 指定生成的文件格式
  其中S16_LE: signed 16 bits little endian,详见: https://blog.csdn.net/qingkongyeyue/article/details/52829886
  另，音频编码协议介绍： https://blog.csdn.net/dong_mingyi/article/details/41316559?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1-41316559.nonecase&utm_term=l16%20%E9%9F%B3%E9%A2%91%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F 

禁用windows update 服务
  REG add "HKLM\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc" /v "Start" /t REG_DWORD /d "4" /f
  
git命令
  $ git config --global user.name "Your Name"
  $ git config --global user.email "email@example.com"
  如果要修改：
  $  git config --global --replace-all user.name "Your Name"
  $  git config --global --replace-all user.email "email@example.com" 
  另，git查看命令： 
  $  git config --list 
  git checkout .  #本地所有的修改，没有提交的，都返回到原来的状态
  Git: Clone
  git add .  
  git commit -m "v1"
  git pull
  git push

  Error " OpenSSL SSL_read: Connection was reset, errno 10054"
  >> 解除ssl验证 git config --global http.sslVerify "false"

  clone 速度太慢
  >> https://gitclone.com/github.com/....
```
