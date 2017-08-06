'''
目的：爬取百度贴吧制定帖子内的图片
时间：2017年08月06日19:28:24
'''


import os
import requests
from bs4 import BeautifulSoup

imgUrls =[]

def get_Html_ImgUrl(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')

    for i in soup.find_all('img', class_='BDE_Image'):
        imgUrls.append(i['src'])

def save_imgs():
    for i,url in enumerate(imgUrls):
        pic = requests.get(url).content
        with open('./'+str(i)+'.jpg', 'wb') as f:
             f.write(pic)
def main():
    url = 'http://tieba.baidu.com/p/3210271432?pn='
    for i in range(1,10):
        try:
            get_Html_ImgUrl(url+str(i))
        except:
            pass
    save_imgs()

print('爬取完毕')
if __name__ == '__main__':
    main()