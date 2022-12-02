import pickle
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.metrics import accuracy_score
import index
def main(text):
    with open('Y', 'rb') as f2:
      Y =pickle.load(f2)
    with open('vectorizer', 'rb') as f3:
      vectorizer = pickle.load(f3)
    with open('X', 'rb') as f4:
      X = pickle.load(f4)
    def stemming(content):  
      stemmed_content = re.sub('[^a-zA-Z]',' ',str(content))
      stemmed_content = stemmed_content.lower()
      stemmed_content = stemmed_content.split()
      port_stem = PorterStemmer()
      stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
      stemmed_content = ' '.join(stemmed_content)
      return stemmed_content
    
    with open('model', 'rb') as f1:
      model=pickle.load(f1)
    X_train_prediction = model.predict(X)
    training_data_accuracy = accuracy_score(X_train_prediction, Y)
    print('Accuracy score of the training data : ', training_data_accuracy)
    
    X_new = vectorizer.transform(pd.Series(stemming(text)))
    
    prediction = model.predict(X_new)
    print(prediction)
    
    if (prediction[0]==0):
      r = 'The news is Fake'
    else:
      r ='The news is Real'
    return r
print(main(index.get_testdata('https://sports.ndtv.com/fifa-world-cup-2022/did-cristiano-ronaldo-head-ball-vs-uruguay-in-world-cup-game-fifa-has-this-to-say-3563389')))
    
    
    