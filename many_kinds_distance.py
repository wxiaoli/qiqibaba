# coding=utf-8
import numpy as np

''' 
    token-based distance/similarity 
'''
def min_edit_distance(s1, s2):
    if s1 is None:
        s1=''
    if s2 is None:
        s2=''
    # 针对token,而不是单一字符
    s1 = s1.split()
    s2 = s2.split()

    size1 = len(s1)
    size2 = len(s2)

    last = 0
    tmp = list(range(size2 + 1))
    value = None

    for i in range(size1):
        tmp[0] = i + 1
        last = i
        for j in range(size2):
            if s1[i] == s2[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j + 1])
            last = tmp[j+1]
            tmp[j+1] = value
            
    return value

def jaccard_index(s1,s2):
    c1 = set(s1.split())
    c2 = set(s2.split())
    common = c1 & c2
    union = c1 | c2
    return 1.0 *len(common)/len(union)


''' 
    vector-based distance/similarity
'''
def euclidean_distance(v1,v2):
    return np.linalg.norm(v1 - v2, ord=2, axis=None, keepdims=False)

def manhattan_distance(v1,v2):
    return np.linalg.norm(v1 - v2, ord=1, axis=None, keepdims=False)

def chebyshev_distance(v1,v2):
    return np.linalg.norm(v1 - v2, ord=np.inf, axis=None, keepdims=False)

def cosine_similarity(v1,v2):
    if np.all(v1==v2):
        return 1
    if np.all(v1==0) or np.all(v2==0):
        return 0
    _sim = np.dot(v1,v2)/(np.linalg.norm(v1)*(np.linalg.norm(v2)))
    # 0.5+0.5*_sim
    return _sim