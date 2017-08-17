import requests
from bs4 import BeautifulSoup
import re
import os


def get_text(url):
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'}
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    all_a = soup.find('div', {'class':'j-content'}).find_all('div', {'class':'j-r-list-c-desc'})
    all_text = []
    for text in all_a:
        all_text.append(text.text)

    with open('text.txt', 'a+') as f:
        for text_ in all_text:
            f.write(text_)
    return text_

def main():
    url = 'http://www.budejie.com/text/'
    endpage = int(input('你要下载多少页:'))
    print('正在下载，请稍等！')

    for i in range(1, endpage + 1):
        try:
            get_text(url + str(i))
        except:
            pass
    print('下载完成！请到程序根目录查看text.txt')
if __name__ == '__main__':
    main()