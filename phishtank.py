#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#2020/11/10/
# Marmot
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#2020/11/10/
# Marmot

import requests
from lxml import etree

def file(w):
    f = open('url.txt','a', encoding='utf-8')
    f.writelines(w + '\n')
    f.close()
    return

headers = {
    #Fill in your information
}

for i in range(0,2):
    for x in range(2,22):
        url = 'https://www.phishtank.com/phish_search.php?page='+ str(i) + '&active=y&valid=y'
        r = requests.get(url,headers=headers).content
        topic = etree.HTML(r)
        eid = topic.xpath("/html/body/div[@id='canvas']/div[@id='main']/div[@id='widecol']/div[@class='padded']/table[@class='data']/tr[" + str(x) + "]/td[@class='value'][1]/a/text()")
        eurl = topic.xpath("/html/body/div[@id='canvas']/div[@id='main']/div[@id='widecol']/div[@class='padded']/table[@class='data']/tr[" + str(x) + "]/td[@class='value'][2]/text()")#/text()")[0]
        value = str(eid) + '  ' + str(eurl)
        value = value.replace('[','').replace(']','').replace('\'','').replace('...','')
        print(value)
        file(value)
print('over!')
