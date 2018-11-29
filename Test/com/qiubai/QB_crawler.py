# encoding:utf-8
import urllib,urllib2,re
'''
2018-11-29
干了11年的java开发，今天心血来潮试试 python
不得不说，python 写爬虫比代码量少，提供的工具包简单完善，效率也不错
'''

#设置一个开始页码
startpage_num=0

#设置一个结束参数
endpage_num=10

#定义爬取方法
def getC(startpage_num): 
    #爬取开始前，先把页码加1
    startpage_num = startpage_num+1
    
    #如果到达最大页码则结束
    if endpage_num>10:
        exit()
    
    #设定爬取糗百的链接地址    
    url = "https://www.qiushibaike.com/hot/page/"+str(startpage_num)
    
    #设定user_agent,header 用于欺骗服务器
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
     
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        
        #筛选内容html
        pattern = re.compile('<a href="/article.*</span>', re.S)
        items = re.findall(pattern,content)
        for item in items:
            #获取纯文本内容
            partter2 = re.compile('<span>.*?</span>',re.S)
            item2 = re.findall(partter2, item)
            for item_1 in item2:
                #过滤图片文章
                haveImg = re.search("img", item_1)
                #过滤掉无效的信息
                if not haveImg and len(item_1)>50:
                    print item_1.encode("utf-8").replace("\n","").replace("<span>","").replace("</span>","").replace("<br/>","")
        getC(startpage_num)
    except urllib2.URLError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


#调用爬取方法
getC(startpage_num)

'''
<a href="/article/117379780" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>
宝妈一枚，一不小心和娃一起进了男厕所，囧啊，现在提倡男女平等吗，为什么男厕所那么简单
</span>
'''