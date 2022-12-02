from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
port_stem = PorterStemmer()
with open('stopword', 'wb') as f2:
        pickle.dump(stopwords.words('english'), f2)
with open('stopword', 'rb') as f5:
        stopwords = pickle.load(f5)
