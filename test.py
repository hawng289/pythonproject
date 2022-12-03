import pickle
import re
import pandas as pd
from nltk.stem.porter import PorterStemmer
import index
def main(text):
    with open("Y", 'rb') as f2:
      Y =pickle.load(f2)
    with open('vectorizer', 'rb') as f3:
      vectorizer = pickle.load(f3)
    with open("X", 'rb') as f4:
      X = pickle.load(f4)
    def stemming(content):  
      stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
      stemmed_content = stemmed_content.lower()
      stemmed_content = stemmed_content.split()
      with open('stopword', 'rb') as f5:
        stopwords = pickle.load(f5)
      port_stem = PorterStemmer()
      stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords]
      stemmed_content = ' '.join(stemmed_content)
      return stemmed_content
    
    with open('model', 'rb') as f1:
      model=pickle.load(f1)
    X_train_prediction = model.predict(X)
    # training_data_accuracy = accuracy_score(X_train_prediction, Y)
    # print('Accuracy score of the training data : ', training_data_accuracy)
    
    X_new = vectorizer.transform(pd.Series(stemming(text)))
    
    prediction = model.predict(X_new)
    # print(prediction)
    
    if (prediction[0]==0):
      r = 'The news is highly likely to be FAKE. Be careful with what you read.'
    else:
      r ='The news is highly likely to be REAL.'
    return r

    
    
    