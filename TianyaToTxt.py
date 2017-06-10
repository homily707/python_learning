from pyquery import PyQuery as pq

f = open(r'\chairman.txt', 'a')
for page in range(1,10):
    a=pq(url='http://bbs.tianya.cn/post-no05-328974-%s.shtml' %page)
    #a("div[_host='红朝笑笑生']")
    #a("div[_host='红朝笑笑生']").find('.bbs-content')
    for data in a("div[_host='红朝笑笑生']").items('.bbs-content'):
        content=(data.text())
        f.write(content)
        f.write('\n********************************\n')
f.close()
