
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

X_train = pd.read_csv('train.csv')
X_train = X_train.fillna('')
X_train = X_train[(X_train.label == 1) | (X_train.label == 0)]
X_train['content'] = X_train['author'] + ' ' + X_train['title'] + X_train['text']
Y_train = X_train['label']
X_train = X_train['content']

with open('stopword', 'wb') as f1:
  pickle.dump(stopwords.words('english'), f1)
  f1.close()
with open('stopword', 'rb') as f2:
  stopwords = pickle.load(f2)
  f2.close()

def stemming(content, stopwords =  stopwords):  
  stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  port_stem = PorterStemmer()
  stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content

X_train = X_train.apply(stemming)
vectorizer = TfidfVectorizer()
vectorizer.fit(X_train)
X_train = vectorizer.transform(X_train)

model = LogisticRegression()
model.fit(X_train, Y_train)


X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Accuracy score of the training data : ', training_data_accuracy)

with open('model', 'wb') as f3:
  model=pickle.dump(model, f3)
  f3.close()

with open('vectorizer', 'wb') as f4:
  model=pickle.dump(vectorizer, f4)
  f4.close()