# encoding:utf-8

import urllib2
import urllib
from pip.download import user_agent

'''
url = "http://www.baidu.com"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()
'''


url = "http://www.baidu.com"
values = {"username":"1016903103@qq.com","password":"XXX"}
data = urllib.urlencode(values)
#get\head\put\delete\post\options
request = urllib2.Request(url,data=data);
request.get_method = lambda:'GET' # or 'DELETE'
response = urllib2.urlopen(request)
print response.read()



'''
values = {"username":"1016903103@qq.com","password":"XXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
'''

'''
values = {}
values['username'] = "xingwangjian@126.com"
values['password'] = 'wangxing1987'
data = urllib.urlencode(values)
url = "https://passport.csdn.net/passport_fe/login.html"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent':user_agent}

geturl = url +"?"+data

request = urllib2.Request(geturl,data,header)
response = urllib2.urlopen(request)

print response.read()
'''

enable_proxy = True
proxy_handle = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handel = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(null_proxy_handel)
else:
    opener = urllib2.build_opener(null_proxy_handel)
urllib2.install_opener(opener)    

''' timeout
response = urllib2.urlopen("http://www.baidu.com",timeout=10)
response = urllib2.urlopen("http://www.baidu.com",data,10)
'''

