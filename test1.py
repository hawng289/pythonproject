import pickle
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def main():
    X_train = pd.read_csv("train.csv")
    X_train = X_train.fillna('')
    X_train = X_train[(X_train.label == 1) | (X_train.label == 0)]
    Y = X_train['label']
    X_train['content'] = X_train['author'] + ' ' + X_train['title'] + ' ' + X_train['text']
    X_train = X_train['content']
    
    X_test = pd.read_csv("test.csv")
    X_test = X_test.fillna('')
    X_test['content'] = X_test['author'] + ' ' + X_test['title'] + X_test['text']
    X_test = X_test['content']
    
    def stemming(content):  
      global i
      stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
      stemmed_content = stemmed_content.lower()
      stemmed_content = stemmed_content.split()
      port_stem = PorterStemmer()
      stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
      stemmed_content = ' '.join(stemmed_content)
      stemmed_content = stemmed_content.strip()
      return stemmed_content
    X_test = X_test.apply(stemming)
    X_train = X_train.apply(stemming)
    
    with open('Y', 'wb') as f2:
        pickle.dump(Y, f2)
    vectorizer = TfidfVectorizer()
    vectorizer.fit(X_train)
    X_train = vectorizer.transform(X_train)
    with open('X', 'wb') as f1:
        pickle.dump(X_train, f1)
    with open('vectorizer', 'wb') as f3:
        pickle.dump(vectorizer, f3)
    X_test = vectorizer.transform(X_test)
    model = LogisticRegression()
    model.fit(X_train, Y)
    with open('model', 'wb') as f4:
        pickle.dump(model, f4)
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y)
    print('Accuracy score of the training data : ', training_data_accuracy)
    X_new = X_test[3]
    prediction = model.predict(X_new)
    print(prediction)
    
    if (prediction[0]==0):
      print('The news is Fake')
    else:
      print('The news is Real')
    