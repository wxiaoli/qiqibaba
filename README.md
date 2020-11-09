# 七七八八

- [七七八八](#七七八八)
  - [系统相关](#系统相关)
  - [远程访问相关](#远程访问相关)
  - [python环境配置相关](#python环境配置相关)
    - [conda与python环境](#conda与python环境)
    - [jupyter-server配置](#jupyter-server配置)
  - [其它](#其它)
***

## 系统相关
```
**WINDOWS应用**
+ windows后台运行jupyter notebook并重定向禁止其输出信息：
    start /b jupyter notebook >nul 2>nul &
+ 查看端口占用：netstat -ano|findstr "8888"  
+ 为了在**win10**中从cmd中直接进入conda的shell，执行 conda init --all后重启terminal后，
报错： “无法加载文件 C:\Users\Administrator\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。” 
解决：
1. 以管理员身份运行PowerShell
2. 执行：get-ExecutionPolicy，回复Restricted，表示状态是禁止的
3. 执行：set-ExecutionPolicy RemoteSigned即可

**Linux应用**
+ 查看某一端口的占用情况： lsof -i:端口号
+ 查看显卡信息：lspci | grep -i vga
+ 查看cuda版本： cat /usr/local/cuda/version.txt 或 nvcc -v
+ 显卡应用情况：nvidia-smi 
+ 启动ssh服务：/etc/init.d/ssh start
```

## 远程访问相关
```
ssh -N -f -L localhost:8889:localhost:8888 -p port username@mapped_ip  
localhost:8889 指本地端口   
localhost:8888指部署jupyter的服务器端口  
```

## python环境配置相关
### conda与python环境
```
**conda**
+ conda create -n your_env_name python=3.6
+ conda update -n base -c defaults conda //更新conda版本
+ conda activate 环境名
+ conda deactivate 
+ conda config --show #查看已经安装过的镜像源
+ conda config --add channels https://mirrors...
+ conda config --remove channels url    #删除镜像地址url 

GPU版本pytorch安装：  
conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch

GPU版本tensorflow安装：  
python -m pip install tensorflow-gpu==2.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

conda create -n env_name python=version_number
conda remove -n env_name --all

python -m pip install ipykernel  
python -m ipykernel install --user --name tf

安装包 bak：
python -m pip install jieba matplotlib simplejson pandas seaborn
```
### jupyter-server配置
[jupyter基本配置](https://www.cnblogs.com/wxiaoli/p/10648251.html)   
附加：
```
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

notebook中高亮显示和代码补齐等：
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user --skip-running-check
然后开启jupyter服务后在主界面[Nbextensions]选项卡中配置。
```
[其他奇奇怪怪的问题](https://www.cnblogs.com/wxiaoli/p/13094327.html) 

## 其它
```
**android studio打开时报错： unable to access android sdk add-on list**
选下面的setup Proxy选项，然后在后面的界面中间，选“Manual proxy configuration”，再选“Http”，在host name里填 “mirrors.neusoft.edu.cn” ，这是东软的一个镜像站，然后点ok.  

**MYSQL**
+ 安装包下载： https://dev.mysql.com/downloads/windows/installer/8.0.html
+ vscode做mysql客户端配置：https://blog.csdn.net/Gineyc/article/details/103227874  
**正则表达式**：https://www.liujiangblog.com/course/python/73  

**树莓派**  
usb免驱动声卡 + 麦克风
查看树莓派型号：cat /proc/device-tree/model
查看CPU：cat /proc/cpuinfo 
Raspberry Pi 3B 麦克风安装： http://www.alsrobot.cn/goods-579.html
aplay有的声音播放不出来。
用sox播放音频：
sudo apt-get install sox
sudo apt-get install sox libsox-fmt-all


**ALSA**(Advanced Linux Sound Architecture),是一个完全开放源代码的音频驱动程序集.  
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

git命令
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
如果要修改：
$  git config --global --replace-all user.name "Your Name"
$  git config --global --replace-all user.email "email@example.com" 
另，git查看命令： 
$  git config --list 
https://code.visualstudio.com/docs/editor/github
 Git: Clone
git add .  
git commit -m "v1.0"
git pull
git push
```
