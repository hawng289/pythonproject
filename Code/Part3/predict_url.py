import requests
from bs4 import BeautifulSoup
from predict_text import predict

def get_testdata(path) :
    try:
        res = requests.get(path)
        res.raise_for_status()
    except requests.exceptions.URLRequired as erru:
        return erru
    except requests.exceptions.TooManyRedirects as e:
        return e
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err
   
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

result = predict(get_testdata("https://www.whitehouse.gov/about-the-white-house/presidents/donald-j-trump/"))
if (isinstance(result,str)):
    print(result)
else:
    print("ERROR:" + str(result))

