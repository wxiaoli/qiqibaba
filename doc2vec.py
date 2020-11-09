# coding=utf-8
from gensim import corpora, models, similarities
class gensim_TFIDF:
    def __init__(self, standard_seq):
        '''
        # standard_seq is a list, each element is a token list
        ''' 
        seq_items = standard_seq
        _dct  = corpora.Dictionary(seq_items)# corpus dictionary
        # convert documents into the bows
        bows = [_dct.doc2bow(s) for s in seq_items] # docs in the form of bag of tf
        vec_model = models.TfidfModel(bows) # do bow->tfidf        
        
        self.dct = _dct.token2id
        self.bows = bows # csr形式
        self.docvectors  = [d for d in vec_model[bows]] # csr形式
        self.vec_model = vec_model
        self._dct = _dct
        
    def new_vec(self, word_list):
        return self.vec_model[self._dct.doc2bow(word_list)] # csr形式      
# #-------------------------------------------------------

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
class sklearn_TFIDF:
    def __init__(self, standard_seq):
        '''
        # standard_seq is a list, each element is a str
        ''' 
        vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')#不设置token_pattern会自动过滤长度为1的token
        transformer = TfidfTransformer()
        tfs = vectorizer.fit_transform(standard_seq)
        tfidf_csr = transformer.fit_transform(tfs)
        
        self.dct = vectorizer.vocabulary_
        self.bows = tfs
        self.docvectors  = transformer.fit_transform(tfs).toarray()        

# #-------------------------------------------------------

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
class doc_latentVec:
    def __init__(self, standard_seq, dim, model_file='', save_file=''):
        '''
        # standard_seq is a list, each element is a token list
        '''         
        # 如果模型已存在，则先加载模型
        if len(model_file)>0:
            vec_model = Doc2Vec.load(fname)                    
        # 训练....
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(standard_seq)]
        vec_model = Doc2Vec(documents, vector_size=dim, window=2, min_count=1)
        # 如果指定模型保存路径，则保存
        if len(save_file)>0:
            vec_model.save(save_file)
        # 删除缓存数据
        vec_model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
        
        self.vec_model = vec_model
        self.docvectors = vec_model.docvecs.vectors_docs # 与tag_list顺序一致的文档向量
        
    def new_vec(self, word_list):
        return self.vec_model.infer_vector(word_list)
    
# standard_seq = \
# [['录音', '资料', '经过', '鉴定', '证实', '未经', '剪辑', '拼凑', '篡改', '和', '臆造.'], 
#  ['在', '工地', '上面', '出', '了', '安全事故', '怎么', '来', '维护', '自己'],
#  ['商标注册', '有', '什么', '相对', '禁止', '的', '条件'],
#  ['建议', '你', '跟', '家人', '把', '这', '事情', '说', '清楚'], 
#  ['致使', '该', '驰名商标', '注册', '人', '的', '利益', '可能', '受到', '损害'], 
#  ['若', '对方', '有', '过错责任', '并', '造成', '损害', '的']]
