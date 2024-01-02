import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
print('done 1')
from gensim.models import KeyedVectors
wv.save('D:/Main_Project/vectors.kv')
print('done 2')