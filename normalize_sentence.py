# coding=utf-8
import re
import string
'''
input 和output 都是 str
ref:
正则表达式： https://www.liujiangblog.com/course/python/73
'''
re_num = '0-9'
re_en = 'a-zA-Z'
re_ch = '\u4e00-\u9fa5' #汉字
re_punctuation_en = '!"#$%&\'\(\)\*+,-./:;<=>\?@[\\]^_`{|}~' #string.punctuation
re_punctuation_ch = '！？、，：；。‘’“”（）＜＞｛｝《》「」『』【】'
# reg_express = '[^' + re_num + re_en + re_ch + ']+'

'''中英文通用'''
def white_space_fix(s):
    # 删除多余的空白(including spaces, tabs, line breaks)'''
    return re.sub(r'\s{2,}', ' ', s)

def remove_stop_words(s,stop_words=set()):
    return ' '.join(c for c in s if c not in _stopwords)

# 把不符合 _reg 的token全部用' '替换
def sub_notwant(s, _reg, token=' '):
    s = re.sub(r'[^' + _reg + ']+',token, s)
    return s

def clean(s):
    return white_space_fix(sub_notwant(s, re_en+re_num+re_punctuation_en))


'''中文'''
import jieba
jieba.initialize()  # 手动初始化并加载词典
def seg_by_jieba(s):    
    seg_generator = jieba.cut(s, cut_all=False)# 精确模式
    return ' '.join(seg_generator)

def add_words(word_file = 'add_words.txt'):
    with open(word_file,'r') as f:
        cont=0
        for line in f.readlines():
            cont+=1
            jieba.add_word(line.strip()) #注意这里要去掉换行标记
        print('共添加{}个词'.format(cont))
        
def seg_sent(s):
    # list(jieba.cut_for_search(s)) 
    return list(jieba.cut(s))