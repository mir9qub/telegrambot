import requests
from bs4 import BeautifulSoup

mydict2 = {}
def get_url():
    src = 'https://tengrinews.kz'
    source = requests.get(src).text
    soup = BeautifulSoup(source, 'lxml')
    top = list(soup.select(".tn-tape-grid > div:nth-of-type(2) > div > a"))
    mydict = {}
    key = 1
    
    for i in top:
        title = (str(i).split('>'))[1][:-3]
        link = str(i).split('/')
        link = 'https://tengrinews.kz' + '/' + link[1] + '/' + link[2]
        mydict[title] = key
        mydict2[key] = link
        key += 1
    return mydict

def parse_news(key):
    
    if key not in mydict2:
        return 'Incorrect id'
    
    source = requests.get(mydict2[key]).text
    soup = BeautifulSoup(source, 'lxml')
    
    article = (soup.find_all('article'))
    ans = []
    
    for i in article:
        text = ' '.join(str(i.text).split())
        if text:
            ans.append(text+'\n')


    video = ''
    picture = ''
    try:
        picture = (str(soup.picture.source.img).split('src=')[-1].split()[0].split('/'))
        picture = 'tengrinews.kz/' + '/'.join(picture[1:-1]) + '/' + picture[-1][:-1]
    except:
        pass

    try:
        video = str(soup.video.source).split('/')
        video = 'tengrinews.kz/' + '/'.join(video[1:5]) + '/' + video[-2][:-4]
    except:
        pass


    ans = ' '.join(ans)

    return [ans, picture, video]
