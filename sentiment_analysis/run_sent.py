import pickle
from sklearn.svm import SVC
import string
import numpy as np
import spacy
#python -m spacy download en
from gensim.models import KeyedVectors
wv = KeyedVectors.load('./vectors.kv')

with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

def sent_vec(sent):
    vector_size = wv.vector_size
    wv_res = np.zeros(vector_size)
    ctr = 1
    for w in sent:
        if w in wv:
            ctr += 1
            wv_res += wv[w]
    wv_res = wv_res/ctr
    return wv_res
def spacy_tokenizer(sentence):
    doc = nlp(sentence)
    mytokens = [ word.lemma_.lower().strip() for word in doc ]
    mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]
    return mytokens
nlp = spacy.load("en_core_web_sm")
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
punctuations = string.punctuation

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

text=input("Enter text: ")
text=remove_html_tags(text)
text=spacy_tokenizer(text)
text=sent_vec(text)
predict=svm_model.predict([text])
print(predict)
