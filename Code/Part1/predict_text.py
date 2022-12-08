import pickle
import re
import pandas as pd
from nltk.stem.porter import PorterStemmer
with open('stopword', 'rb') as f1:
  stopwords = pickle.load(f1)
  f1.close()
with open('vectorizer', 'rb') as f2:
  vectorizer = pickle.load(f2)
  f2.close()
with open('model', 'rb') as f3:
  model = pickle.load(f3)
  f3.close()


def stemming(content, stopwords =  stopwords):  
  stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  port_stem = PorterStemmer()
  stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content

def predict(text):
  X_new = vectorizer.transform(pd.Series(stemming(text)))  
  prediction = model.predict(X_new)
  if (prediction[0] == 1):
    r = 'The news is highly likely to be FAKE. Be careful with what you read.'
  else:
    r ='The news is highly likely to be REAL.'
  return r

    
    
    