import pickle
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import csv

with open('stopword', 'rb') as f1:
  stopwords = pickle.load(f1)
  f1.close()

def stemming(content, stopwords =  stopwords):  
  stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  port_stem = PorterStemmer()
  stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content


with open('vectorizer', 'rb') as f2:
  vectorizer = pickle.load(f2)
  f2.close()
with open('model', 'rb') as f3:
  model = pickle.load(f3)
  f3.close()

def predict(csv_name):
  X_test = pd.read_csv(csv_name)
  X_test = X_test.fillna('')
  X_test['content'] = X_test['author'] + ' ' + X_test['title'] + X_test['text']
  X_test = X_test['content']
  X_test = X_test.apply(stemming)
  X_new = vectorizer.transform(X_test)  
  prediction = model.predict(X_new)
  return prediction

result = predict("test.csv")
X_test = pd.read_csv("test.csv")
X_test['label'] = result
print(type(X_test))
X_test.to_csv('test_after.csv')

  