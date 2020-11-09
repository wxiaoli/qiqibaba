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
