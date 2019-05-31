# encoding:utf-8
import urllib,urllib2,re
'''
2019-03-29
小说老是弹广告，自己爬取吧
'''

#设置一个开始页码
startUrl="http://www.xbiquge.la/10/10489/"

#设置一个结束参数
endpage_num=10

#定义爬取方法
def getTitle(startUrl): 

    #设定user_agent,header 用于欺骗服务器
    #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #headers = {'User-Agent':user_agent}
     
    try:
        request = urllib2.Request(startUrl)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        #print content
        #筛选内容html
        #pattern = re.compile('<a href="/article.*</span>', re.S)
        
        pattern = re.compile("<dd><a href='/10/10489/.*?.html' >.*?</a></dd>", re.S)
        
        items = re.findall(pattern,content)
        for item in items:
            #获取纯文本内容
            url = item[item.find("\'")+11:item.rfind("\'")]
            
            title = item.replace(" ","")
            title = title[title.find("html'>")+6:title.find("</a>")]
            print startUrl+url
            getContent(startUrl+url);
        #getC(startpage_num)
    except urllib2.URLError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

#定义爬取方法
def getContent(startUrl): 

    #设定user_agent,header 用于欺骗服务器
    #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #headers = {'User-Agent':user_agent}
     
    try:
        request = urllib2.Request(startUrl)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        
        pattern = re.compile('<div id="content">.*?</div>', re.S)
        items = re.findall(pattern,content)
        for item in items:
            #获取纯文本内容
            tmp = item.replace("<br />","").replace("&nbsp;","")
            tmp = tmp.replace("<p>","")
            print tmp
    except urllib2.URLError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

getTitle(startUrl)