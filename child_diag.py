# -*- coding: utf-8 -*-
'''
接下来请你把香门耳鼻咽喉科、香门内科和香门皮肤科进行下一步预处理：
1.将出现次数最多的表述进行筛选，这里我们可以多选一点，只要出现次数大于50的都留下来（从判断病症的多样化来考虑），或者前10类留下来（从模型的复杂程度来考虑）。
2.将特征进行文本到数值的转化。
3.寻找特征相同但表述不同的样本（一对多的情况）
'''
import pandas as pd
df = pd.read_excel('3.xls')

column_dict = dict(zip(df.columns,[str(i) for i in range(32)]))
df.rename(columns=column_dict,inplace=True)

{'检验日期': 0, '编号': 1, '病人ID': 2, '性别': 3, '年龄': 4, 
 '年龄单位': 5, '科室': 6, '组合项目': 7, '备注': 8, '病人类型': 9,
 '诊断': 10, '吸入性': 11, '螨': 12, '蟑螂': 13, '霉菌组合': 14, 
 '榆树': 15, '葎草': 16, '梧桐': 17, '艾蒿': 18, '豚草': 19,
 '狗毛': 20, '猫毛': 21, '小麦': 22, '花生': 23, '鸡蛋': 24, 
 '大豆': 25, '牛奶': 26, '西红柿': 27, '鳕鱼': 28, '虾': 29, 
 '蟹': 30, '坚果': 31}

df = df.drop('8',axis=1)
df = df.dropna()

def info2num(label,df):
    sub = df[label].value_counts() # subject
    sub_dict = dict((zip(sub.index,[i for i in range(len(sub))])))
    df[label]=df[label].map(lambda x:sub_dict[x])
    return [df,sub_dict]

#df1,dig = info2num('6',df)
sub = df['6'].value_counts()
s=[]
for i in range(len(sub)):
    dise = df[df['6']==sub.index[i]]['10'].value_counts()
    col='%d'%i
    dise.rename(columns={'10':col},inplace=True)
    s.append(dise)

a=pd.concat(s,axis=1)
ke_name_dict=dict(zip([i for i in range(len(sub))],sub.index))
#a.rename(columns=ke_name_dict,inplace=True)
with open('dis_sub.txt','w') as f:
    for i in range(len(s)):
        f.write(sub.index[i]+'\n')
        for j in range(len(s[i])): 
            f.write('    '+s[i].index[j]+':'+str(s[i][j]))
            f.write('\n')
        f.write('\n')
