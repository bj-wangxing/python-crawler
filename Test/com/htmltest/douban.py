#encoding=utf8
import urllib2
from HTMLParser import HTMLParser
 
class MYPARSER(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
 
    def handle_starttag(self,tag,attrs):
        def _attr(attrlist,attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None
 
        if tag == 'li' and _attr(attrs,'data-title'):
            movie = {}
            movie['actors'] = _attr(attrs,'data-actors')
            movie['director'] = _attr(attrs,'data-director')
            movie['duration'] = _attr(attrs,'data-dutation')
            movie['title'] = _attr(attrs,'data-title')
            movie['rate'] = _attr(attrs,'data-rate')
            self.movies.append(movie)
 
def movieparser(url):
    headers = {}
    req = urllib2.Request(url,headers)
    s = urllib2.urlopen(req)
    myparser = MYPARSER()
    myparser.feed(s.read())
    myparser.close()
    return myparser.movies
 
 
if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = movieparser(url)
    for each in movies:
        print('%(title)s|%(rate)s|%(actors)s|%(director)s|%(duration)s' % each)