import requests,os,time
from lxml import etree
url = "https://www.zanyiba.com/dongtaitupian/xieedongtaitu/8676.html"
image_urls=[]
def getimage(imageurl,i):
    inf = requests.get(imageurl).content
    str(i)
    with open('D:\项目文件\Python\GII\imageliufei\%s.jpg'%i,'ab') as f:
        f.write(inf)
        f.close()
# getimage('123')
# exit()
i=0
while url:
    i=i+1
    html = requests.get(url)
    html1 = etree.HTML(html.text)
    image_temp = html1.xpath('/html/body/div[3]/div[1]/div[2]/div[3]/a/img/@src')  # 图片链接
    next_url = html1.xpath('/html/body/div[3]/div[1]/div[2]/div[3]/a/@href')       # 下一页链接

    if image_temp:
        if image_temp[0].split('//')[0] == '':
            image_url = 'https:'+image_temp[0]
            getimage(image_url,i)
    print(i)
    if next_url:
        url = next_url[0]
    else:
        url=''
    #time.sleep(1)
