import os
import gensim

filename = 'news_sohusite_cutword.txt'
word2vec_file = 'news_sohusite_cutword_vec'

def LineSentence(filename):
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            lines[index] = line.strip().split(' ') + ['\n']
        return lines

def train_word2vec(filename):
    sentences = LineSentence(filename)
    #sg=0 使用cbow训练, sg=1对低频词较为敏感
    model = gensim.models.Word2Vec(sentences,
                        size=100, window=5, min_count=2, sg=1, iter=10)
    model.save(word2vec_file)

train_word2vec(filename)
