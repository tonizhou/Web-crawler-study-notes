#下载一张图片
import urllib.request
def get_image(url):
    response = urllib.request.urlopen(url)
    get_img = response.read()
    with open(r'.vscode\1.png', 'wb') as f:
        f.write(get_img)
    return get_image
url = 'https://b-ssl.duitang.com/uploads/item/201602/04/20160204221228_45QuF.png'
img = get_image(url)
print(img)