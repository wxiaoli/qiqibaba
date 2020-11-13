# coding=utf-8
import json
from NumpyEncoder import NumpyEncoder
def save_json(data,fname):
    with open(fname,'w') as f:
        json.dump(data,f,cls=NumpyEncoder)

def save_txt(data,fname):
    with open(fname,'w') as f:
        f.writelines('\n'.join(data))

import csv
def save_csv(fname,data,col_names):
    assert len(data[0]) == len(col_names)
    # Note: 这里编码方式用utf-8时，excel打开会乱码
    with open(fname,'w',encoding='gbk') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(col_names)
        for r in data:
            csv_writer.writerow(list(r))

import pandas as pd
def read_csv(fname):
    data = pd.read_csv(fname)
    print(data.shape)
    print(data.columns)
    print(data.index)
    return data

def read_multiline_json(filename):
    json_content=[]
    with open(filename,'rb') as f:
        lines = f.readlines()
        for line in lines:
            json_content.append(json.loads(line))
    return json_content 

# 解压缩文件
import zipfile
import os
'''
    zip_file: 压缩文件，
    extract_dir： 解压缩目录
    return: 解压缩后的所有文件路径
'''
def extract_zipfile(zip_file, extract_dir):
    # 解压
    with zipfile.ZipFile(zip_file,'r') as zz:
        zz.extractall(extract_dir)

    # 列出解压后的所有文件
    files = []
    for dirpath,dirnames,filenames in os.walk(extract_dir): 
        for filename in filenames:
            files.append(os.path.join(dirpath,filename))
    
    return files