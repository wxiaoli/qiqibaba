    # 七七八八

    1.系统相关
    ==============================================================================
    为了在win10中从cmd中直接进入conda的shell，执行 conda init --all后重启terminal后，
    报错： “无法加载文件 C:\Users\Administrator\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。” 
    解决：
    1. 以管理员身份运行PowerShell
    2. 执行：get-ExecutionPolicy，回复Restricted，表示状态是禁止的
    3. 执行：set-ExecutionPolicy RemoteSigned即可

    2.远程访问相关
    ==============================================================================
    ssh -N -f -L localhost:8889:localhost:8888 -p port username@mapped_ip  
    localhost:8889 指本地端口   
    localhost:8888指部署jupyter的服务器端口  

    3.python环境配置相关
    ==============================================================================
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

    ==============================================================================
    [jupyter完整配置流程](https://www.cnblogs.com/wxiaoli/p/10648251.html)
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

    notebook中高亮显示和代码补齐等：
    pip install jupyter_contrib_nbextensions
    jupyter contrib nbextension install --user --skip-running-check
    然后开启jupyter服务后在主界面[Nbextensions]选项卡中配置。

    其它
    ==============================================================================
    git命令
    $ git config --global user.name "Your Name"
    $ git config --global user.email "email@example.com"
    如果要修改：
    $  git config --global --replace-all user.name "Your Name"
    $  git config --global --replace-all user.email "email@example.com" 
    另，git查看命令： 
    $  git config --list 
