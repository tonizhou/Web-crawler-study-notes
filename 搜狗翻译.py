#搜狗翻译
import urllib.request
import urllib.parse
import json

while True:
    print('='*30)
    content = input('请输入需要翻译的内容：')
    url = 'http://fanyi.sogou.com/reventondc/translate'
    date = {}
    date['from'] = 'auto'
    date['to'] = 'zh-CHS'
    date['client'] = 'wap'
    date['text'] = content
    date['useDetect'] = 'on'
    date['useDetectResult'] = 'on'
    date['needQc'] = '1'
    date['uuid'] = 'dbabe546-a9e9-4ca4-af26-704e619f4b7d'

    date = urllib.parse.urlencode(date).encode('utf-8')
    response = urllib.request.urlopen(url, date)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print('翻译的内容为：%s' %(target['translate']['dit']))
    print('='*30)