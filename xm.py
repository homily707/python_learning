
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re

df = pd.read_csv('3.csv')
column_dict = dict(zip(df.columns,[str(i) for i in range(32)]))
c_dict2=dict(zip([str(i) for i in range(32)],df.columns))
df = df.rename(columns=column_dict,inplace=False)
df = df.drop(['0','1','2','7','8'],axis=1)
df = df.dropna()

{'检验日期': 0, '编号': 1, '病人ID': 2, '性别': 3, '年龄': 4, 
 '年龄单位': 5, '科室': 6, '组合项目': 7, '备注': 8, '病人类型': 9,
 '诊断': 10, '吸入性': 11, '螨': 12, '蟑螂': 13, '霉菌组合': 14, 
 '榆树': 15, '葎草': 16, '梧桐': 17, '艾蒿': 18, '豚草': 19,
 '狗毛': 20, '猫毛': 21, '小麦': 22, '花生': 23, '鸡蛋': 24, 
 '大豆': 25, '牛奶': 26, '西红柿': 27, '鳕鱼': 28, '虾': 29, 
 '蟹': 30, '坚果': 31}
dict3={
 '10': '诊断',
 '11': '吸入性',
 '12': '螨',
 '13': '蟑螂',
 '14': '霉菌组合',
 '15': '榆树',
 '16': '葎草',
 '17': '梧桐',
 '18': '艾蒿',
 '19': '豚草',
 '20': '狗毛',
 '21': '猫毛',
 '22': '小麦',
 '23': '花生',
 '24': '鸡蛋',
 '25': '大豆',
 '26': '牛奶',
 '27': '西红柿',
 '28': '鳕鱼',
 '29': '虾',
 '30': '蟹',
 '31': '坚果'}

'''
接下来请你把香门耳鼻咽喉科、香门内科和香门皮肤科进行下一步预处理：
1.将出现次数最多的表述进行筛选，这里我们可以多选一点，只要出现次数大于50的都留下来（从判断病症的多样化来考虑），或者前10类留下来（从模型的复杂程度来考虑）。
2.将特征进行文本到数值的转化。
3.寻找特征相同但表述不同的样本（一对多的情况）
'''
'''{'100-200 IU/mL': 2,
 '20-50': 0,
 '20-50 IU/ml': 0,
 '50-100': 1,
 '50-100 IU/ml': 1,
 '50-100IU/ml': 1}'''
d_xiru=dict(zip(df['11'].value_counts().index,[1,0,1,2,1,0]))
df['11']=df['11'].map(lambda x:d_xiru[x])

'''  阴性 0
     阳性 几个+号 就为几 例如 阳性+++++[99.15] 处理为 5'''
def plus_count(word):
    return len(re.findall(r'\+',word))

for i in range(12,32):
    l=str(i)
    df[l]=df[l].map(plus_count)


'''f=open('1.txt','w')
for i in range(12,32):
    content = str(df[str(i)].value_counts().index)
    f.write(content)
    f.write('\n')
'''

df1=df[df['6']=='香门皮肤科']
diag1=df1['10'].value_counts()
df1=df1[df1['10'].isin(diag1.index[0:6])]
df1=df1.drop(['3','4','5','6','9'],axis=1)
d=dict(zip(df1['10'].value_counts().index,range(6)))
df1['10']=df1['10'].map(lambda x:d[x])
l = [str(i) for i in range(11,32)]

def isonly(l):
    return max(l)-min(l)

g=df1.groupby(l).agg(isonly)
g1=df1.groupby(l).agg('mean')
df1=g1[g['10']==0]
df1.to_csv('temp.csv')
df1=pd.read_csv('temp.csv')
df1 = df1.rename(columns=dict3,inplace=False)
df1.to_csv('香门皮肤科.csv',index=False)

{'鼻炎': 0, '慢性鼻咽炎': 1, '鼻出血(鼻衄)': 2, '鼾症': 3, '鼻咽炎': 4, '鼻窦炎': 5, '中耳炎': 6, '鼾症待查': 7, '过敏性鼻炎(变应性鼻炎)': 8, '鼻炎鼻衄': 9}

{'喘息性支气管炎': 0, '支气管炎': 1, '慢性咳嗽': 2, '急性支气管炎': 3, '咳嗽': 4, '上呼吸道感染': 5, '呼吸道感染': 6, '肺炎': 7, '消化不良': 8, '过敏性紫癜': 9}
{'湿疹': 0, '荨麻疹': 1, '皮炎': 2, '痒疹': 3, '健康查体': 4, '丘疹性荨麻疹': 5}
