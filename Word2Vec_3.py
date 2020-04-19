import gensim
import pandas as pd

word2vec_file = 'news_sohusite_cutword_vec'
model = gensim.models.Word2Vec.load(word2vec_file)

# 获取词向量
# model.wv.__getitem__(word)

# 获取词典
# model.wv.vocab

# 查看近义词
print(pd.Series(model.wv.most_similar('百度')))
print(pd.Series(model.wv.most_similar('微信')))

# 正向词和反向词
print(pd.Series(model.most_similar(positive=['足球', '明星'])))
print(pd.Series(model.most_similar(positive=['球星'],negative=['明星'])))

# 词的相似度
print(model.wv.similarity('我', '你'))
print(model.wv.similarity('儿子', '女儿'))

print(model.wv.words_closer_than('我', '你'))