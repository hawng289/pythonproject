import requests
from requests.exceptions import HTTPError
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
    try:
        res = requests.get(path)
        res.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print (errh)
    except requests.exceptions.ConnectionError as errc:
        print (errc)
    except requests.exceptions.Timeout as errt:
        print (errt)
    except requests.exceptions.RequestException as err:
        print (err)
    except requests.exceptions.URLRequired as erru:
        print(erru)
    except requests.exceptions.TooManyRedirects as e:
        print(e)
    else:
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




