import requests
from bs4 import BeautifulSoup


def get_url(name):
    src = 'https://tengrinews.kz'
    source = requests.get(src).text
    soup = BeautifulSoup(source, 'lxml')
    top = list(soup.select(".tn-tape-grid > div:nth-of-type(2) > div > a"))
    mydict = {}
    mydictkey = {}
    key = 1
    for i in top:
        title = (str(i).split('>'))[1][:-3]
        link = str(i).split('/')
        link = 'https://tengrinews.kz' + '/' + link[1] + '/' + link[2]
        mydict[title] = key
        mydictkey[key] = link
        key += 1
    if name == 'get_title':
        return mydict
    return mydictkey

def parse_news(key):
    mydict = get_url('get_link')
    if key not in mydict:
        return 'Incorrect id'
    source = requests.get(mydict[key]).text
    soup = BeautifulSoup(source, 'lxml')
    #extra = len("""Мы открыли еще один Telegram-канал. О деньгах и казахстанском бизнесе. Подписывайтесь на Tengri Деньги! 
#Өзекті жаңалықтарды сілтемесіз оқу үшін Telegram желісінде парақшамызға тіркеліңіз!""")

    article = (soup.find_all('article'))
    ans = []
    for i in article:
        text = ' '.join(str(i.text).split())
        if text:
            ans.append(text+'\n')



    #picture = soup.select("picture")

    ans = ' '.join(ans)
    return ans[:]
