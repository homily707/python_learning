import urllib2,urllib
import re

i=1
req=urllib2.Request('https://bbs.hupu.com/16308715.html')
html=urllib2.urlopen(req).read()
gif=re.compile(r'''https://i\w+.hoopchina.com.cn/.+?gif''')
list(set(re.findall(gif,html)))
for links in list(set(re.findall(gif,html))):
    print i,
    urllib.urlretrieve(links,'E:\code\gif\%s.gif' %i)
    i+=1
