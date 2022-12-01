import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



def stemming(content):  
    stemmed_content = re.sub('[^a-zA-Z]',' ', str(content))
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    port_stem = PorterStemmer()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
def get_testdata(path) :
    res = requests.get(path)
    obj = BeautifulSoup(res.text, 'html.parser')
    list_title = []
    for i in range(1, 7):
        h = obj.find_all('h' + str(i))
        if (h == []):
            break
        list_title.append(h) 
    content = ""
    for item in list_title:
        for i in item:
            title_text = i.get_text()
            content += title_text
    list_text = obj.find_all('p')
    for item in list_text:
        text = item.get_text()
        if (len(text) > 50):
            content += text
    return content


