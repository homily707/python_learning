import requests
import json
import pandas as pd
import re

def get_url():
    f1 = open('2.txt','r')
    data = f1.read()
    all_id = re.findall('(?<=u/)\d+',data)
    ad = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={0}&containerid=107603{0}'
    return [ad.format(x) for x in all_id]


def get_item(tag,d1):
    for d2 in d1:
        if 'mblog' in d2:
            yield d2['mblog'][tag]


def s(ad):
    r = requests.get(ad)
    d = json.loads(r.text)
    d1 = d['data']['cards']
    created_at = [x for x in get_item('created_at',d1)]   
    comments_count = [x for x in get_item('comments_count',d1)]
    attitudes_count = [x for x in get_item('attitudes_count',d1)]
    reposts_count = [x for x in get_item('reposts_count',d1)]
    df = pd.DataFrame({'time':created_at,
                       'comments':comments_count,
                       'attitude':attitudes_count,
                       'repost':reposts_count})
    name = d1[0]['mblog']['user']['screen_name']
    fans = d1[0]['mblog']['user']['followers_count']
    df.to_csv('{}.csv'.format(name),header=True)
    with open('fans_count.txt','a') as f:
        f.write(name+':'+str(fans)+'\n')
    f.close()

url = get_url()
for i in url:
    s(i)

