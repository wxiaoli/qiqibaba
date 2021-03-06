#coding = utf-8

import os
cur_dir = os.path.abspath(os.path.dirname('__file__')) #当前目录的绝对路径
join_dir = os.path.join(cur_dir,'some_dir') #拼接目录
par_dir = os.path.join(cur_dir,os.path.pardir) #取cur_dir的上一级目录

# 判断 python 版本是否是3
sys.version_info.major == 3

# 耗时
import time
timer = time.perf_counter
# 获取系统时间
import datetime
dt=datetime.datetime.now()
print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second) 
delta = datetime.timedelta(days=1)
yesterday = dt-delta

t1 = timer()
....
t2 = timer()
t2-t1 # 结果以 秒 为单位

# 修改dir_dispose目录下的所有文件的文件名
dir_dispose= ''
for dirpath,dirnames,filenames in os.walk(dir_dispose):
    for filename in filenames:
        new_name = filename[:6]+filename[-4:]  
        os.rename(os.path.join(dirpath,filename),os.path.join(dirpath,new_name))

# 判断目录是否存在，新建目录
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

import string
words1 = string.ascii_uppercase  # 26个大写英文字母
print(words1)
words2 = string.ascii_lowercase  # 26个小写英文字母
print(words2)
words3 = string.ascii_letters  # 52个小写和大写英文字母
print(words3)

# 自动生成size个字符
import string
def rand_chars(size):
    shuffled_ind = np.random.permutation(np.array(range(52)))
    chars = string.ascii_letters
    return [chars[shuffled_ind[:size][i]] for i in range(size)]

# 生成随机序列
_len = 20
shuffled_indices = np.random.permutation(np.array(range(_len)))

# 按照列表中元素第k维从大到小排序
k=0
_list.sort(key=lambda i:i[k], reverse=True)

# 取numpy vector的topk元素
import heapq
import numpy as np
_vec = np.array([1,3,2,4,5])
topk = 5
topk_large = heapq.nlargest(topk,_vec)#list
topk_index = heapq.nlargest(topk,range(len(_vec)), _vec.take) #list

# 压缩文件
import zipfile 

with zipfile.ZipFile('demo.zip','r') as zzz:
    print(zzz.namelist())

# 若压缩包里的文件名有中文，则容易出现乱码，要对中文文件名进行转码：
with zipfile.ZipFile('demo.zip','r') as zzz:
    for fn in zzz.namelist():
        print(fn.encode('cp437').decode('gbk'))
        
# .extractall() 可以把压缩包里的所有文件解压到'folder1'
# （解压后的文件保持原目录结构）
# ,pwd=b'123456'指压缩包密码，可省略
with zipfile.ZipFile('demo.zip','r') as zzz:
    zzz.extractall('folder1',pwd=b'123456')
    
# 创建zip压缩包，若向已有的压缩包添加文件，使用'a'
fn_list = ['file1.txt','file2.txt','temp_file.png','./py/hello.py']
with zipfile.ZipFile('sample.zip','w') as z:
    for fn in fn_list:
        z.write(fn)

# cpu核数
import os
os.cpu_count()

