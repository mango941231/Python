import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode
import re
import ast
import time

def front():
    url = 'https://author.baidu.com/pipe?context={%22app_id%22:%221572965562093298%22,%22from%22:%22favorite%22}&pagelets[]=article&reqID=1&ispeed=1'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie':'BAIDUID=C0F239571F90268C0A34B27A8A6A0B73:FG=1; BIDUPSID=C0F239571F90268C0A34B27A8A6A0B73; PSTM=1540373237; BDUSS=JLS1pISUl3bGFId3p-ZlNVLVNqUlBhRWcyc3VQUm9ZSUhRamlOb2pJRjhCZmxiQVFBQUFBJCQAAAAAAAAAAAEAAADNI9BUcGdiZXZjcm0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHx40Vt8eNFbWH; H_PS_PSSID=27442_1444_21080_18560; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2'
    }
    response = requests.get(url,headers=headers).text
    p1 = re.compile(r'[(](.*)[)]', re.S)
    html = re.findall(p1, response)
    html_dict = ast.literal_eval(html[0])
    doc = pq(html_dict['html'])
    items = doc('.c-news-text .mth-list-count').items()
    tupian = []
    for item in items:
        PostTitle = item.find('.text h2').text()            #文章标题
        PostUrl = item.find('.typeNews').attr('href')      #文章url
        PostPid = item.find('.typeNews').attr('data-event-data')      #文章ID
        imgdiv = item.find('.three-img')
        imgurl = pq(imgdiv)
        imgs = imgurl('.pt').items()
        for i in imgs:
            style = i.attr('style')
            p3 = re.compile(r'[(](.*)[)]',re.S)
            p4 = re.findall(p3,style)
            tupian.append(p4[0])
        PostThumbnail = tupian                                   #封面图
        del tupian[:]
        read = item.find('.text-extra .pv').text()[:-2]
        # totalCount = re.sub("\D", "", PostPv)
        if '万' in read:
            PostPv = int(float(read.replace('万',''))*10000)
            print(PostPv)                                       # 浏览量有’万‘字的乘以10000
        else:
            PostPv = read
            print(PostPv)
        subpage = requests.get(PostUrl,headers=headers).text
        docsub = pq(subpage)
        ActAid = docsub.find('.mod .authorName').text()      #账号ID
        CreatedAt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #采集时间
        PublishedAt = docsub.find('.mod .infoSet span').text()[4:]       #文章发表时间
        PostContent = str(docsub.find('.mainContent'))                     #文章内容


# def Last():








if __name__ == '__main__':
    front()