from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
X = vectorizer.fit_transform(corpus)

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=False, norm='l1')

counts = [[3, 0, 1],
           [2, 0, 0],
           [3, 0, 0],
           [4, 0, 0],
           [3, 2, 0],
           [3, 0, 2]]
tfidf = transformer.fit_transform(counts)
print(tfidf.toarray())


import tensorflow as tf
tf.contrib.learn.preprocessing.VocabularyProcessor (
                                          max_document_length,    
                                          min_frequency=0,
                                          vocabulary=None,
                                          tokenizer_fn=None)
x_text =[
    'i love you',
    'me too'
]

vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
vocab_processor.fit(x_text)
print next(vocab_processor.transform(['i me too'])).tolist()
x = np.array(list(vocab_processor.fit_transform(x_text)))
print(x)