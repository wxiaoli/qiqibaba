import pypinyin

# 不带声调的(style=pypinyin.NORMAL)
def pinyin(hans):    
    s = ''
    for i in pypinyin.pinyin(hans, style=pypinyin.NORMAL):
        s += ''.join(i)+ ' '
    return s
 
# 带声调的(默认)
def yinjie(hans):
    s = ''
    # heteronym=True开启多音字
    for i in pypinyin.pinyin(hans, heteronym=False):
        s = s + ''.join(i) + ' '
    return s

if __name__ == '__main__':
    hans = '你好啊'
    print(pinyin(hans)) # ni hao a 
    print(yinjie(hans)) # nǐ hǎo a 
