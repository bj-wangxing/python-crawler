#coding=utf-8
from pip._vendor.distlib.locators import Page
__author__ = 'WX'
# encoding:utf-8
import urllib
import urllib2
import re

#处理页面标签
class Tool:
    #去除img标签，7位长空格
    removeImg = re.compile('<img.*?>') #'<img.*?>|{7}|'
    
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|{/a}')
    
    #把换行的标签换为\n
    removeLine = re.compile('<tr>|<div>|</div>|</p>')
    
    #将制<td>替换为\t
    removeTD = re.compile('<td>')
     
    #把段落开头换位\n加两个空格
    removePara = re.compile('<p.*?>')
    
    #将换行符或双换行符替换为\n
    removeBR = re.compile('<br><br>|<br>')
     
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    
    def repalce(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.removeLine,"\n",x)
        x = re.sub(self.removeTD,"\t",x)
        x = re.sub(self.removePara,"\n",x)
        x = re.sub(self.removeBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()
    
class BDTB:
    
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseUrl=baseUrl
        self.seeLZ='&see_lz'+str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor=1
        self.defaultTitle=u"百度贴吧"
        self.floorTag=floorTag
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ +'&pn=' + str(pageNum)
            request = urllib2.Request(url) 
            response = urllib2.urlopen(request,timeout=15)
            print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print u"链接百度贴吧失败，错误原因",e.reason
                return None
    
    def getTitle(self,page):
        page = self.getPage(1)
        pattern = re.compile('h1 calss="core_title_txt.*?">.*?</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1) #测试输出
            return result.group(1).strip()
        else:
            return None
        
    def getPageNum(self,page):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span.*?>(.*?)</span>"', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1) #测试输出
            return result.group(1).strip()
        else:
            return None
    
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>"', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = '\n' + self.tool.repalce(item)+'\n'
            #print content
            contents.append(content.encode('utf-8'))
            return contents
    
    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title+".txt","w+")
        else:
            self.file = open(self.defaultTitle+".txt","w+")
    
    def writeData(self,contents):
        for item in contents:
            if self.floorTag=='1':
                floorLine = "\n"+str(self.floor)+u'-------------------------\n'
                self.file.write(floorLine)
                self.file.write(item)
                self.floor+=1
                
    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum(indexPage)
        title=self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum==None:
            print "URL已失效，请重试"
            return 
        try:
            print "该帖子共有"+str(pageNum)+"页"
            for i in range(i,int(pageNum)):
                print "正在写入第"+str(i)+"页"
                page = self.getpage(i)
                contents=self.getContent(page)
                self.writeData(contents)
        except IOError,e:
             print "写入异常，原因"+e.message
        finally:
            print "写入完成"                   

print u"请输入帖子代号"             
baseUrl = 'https://tieba.baidu.com/p/3138733512?red_tag=3463203852'+str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input('是否只获取楼主发，是-1，否-0\n')
floorTag = raw_input('是否写入楼层信息，是-1，否-0\n')
dbtb = BDTB(baseUrl,seeLZ,floorTag)
dbtb.start()