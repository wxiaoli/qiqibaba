# coding=utf-8
''' 用gensim的word2vec训练词向量 '''
import jieba
import os
from gensim.models import Word2Vec
import logging
jieba.add_word('广智微芯')

class Sentences(object):
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir

    def __iter__(self):
        for fname in os.listdir(self.corpus_dir):
            with open(os.path.join(self.corpus_dir, fname)) as f: #, encoding='utf8'
                for line in f:
                    yield list(jieba.cut(line))
                
class W2V_by_gensim(object):
    def __init__(self):
        pass
    
    def from_start_train(self,corpus_dir,embeddings_dir='',word_dim=200):
        ''' 从头开始训练 '''
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        sentences = Sentences(corpus_dir) 
        model = Word2Vec(sentences, size=word_dim, window=5, min_count=5, workers=4) #size：词向量维度
        
        model.save(os.path.join(embeddings_dir,'embeddings.bin'))
        model.wv.save_word2vec_format(os.path.join(embeddings_dir,'wv.dict'))#保存的模型仅包含词-向量信息
    
    def incre_train(self,corpus_dir,origin_embeddingFile, new_embeddings_dir):
        ''' 在已有embedding基础上增量训练 '''
        if isinstance(corpus_dir, str):
            sentences = Sentences(corpus_dir)
        if isinstance(corpus_dir, list):
            sentences = corpus_dir       
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = Word2Vec.load(origin_embeddingFile)
        model.build_vocab(sentences, update=True)
        model.train(sentences,epochs=500,total_examples=model.corpus_count)

        model.save(os.path.join(new_embeddings_dir,'embeddings.bin'))
        model.wv.save_word2vec_format(os.path.join(new_embeddings_dir,'wv.dict'))   

if __name__ == '__main__':
    train_w2v = W2V_by_gensim()
#     corpus_dir=''
#     train_w2v.from_start_train(corpus_dir,'embeddings_dir')
#     train_w2v.incre_train(corpus_dir,'XXX/embeddings.bin','wiki_embeddings_retuned')
#     train_w2v.incre_train(new_sentences,'XXX/embeddings.bin','wiki_embeddings_retuned')
