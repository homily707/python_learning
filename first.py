import pandas as pd
import numpy as np

train_pre = pd.read_csv('train.csv')
train = train_pre.drop(['PassengerId','Name'],axis=1)
train.columns=train.columns.str.lower()

test_pre = pd.read_csv('test.csv')
test = test_pre.drop(['PassengerId','Name'],axis=1)
test.columns=test.columns.str.lower()

full_data = [train,test]

for i in train.columns:
    if train[i].isnull().sum() == 0:
        print('train:{}:no null'.format(i))
    else:
        print('train:{}:need fillna'.format(i))
#age,cabin,embarked need to fill
for i in test.columns:
    if test[i].isnull().sum() == 0:
        print('test:{}:no null'.format(i))
    else:
        print('test:{}:need fillna'.format(i))

train['sex'] = train['sex'].map({'male':0,'female':1})
test['sex'] = test['sex'].map({'male':0,'female':1})

for dataset in full_data:
    age_avg = dataset['age'].mean()
    age_std = dataset['age'].std()
    age_null_count = dataset['age'].isnull().sum()
    age_null_random_list = np.random.randint(age_avg - age_std, 
                                             age_avg + age_std, 
                                             size=age_null_count)
    dataset['age'][np.isnan(dataset['age'])] = age_null_random_list
    #dataset['age'] = pd.cut(dataset['age'], 5)
    dataset.loc[ dataset['age'] <= 16, 'age'] 					       = 0
    dataset.loc[(dataset['age'] > 16) & (dataset['age'] <= 32), 'age'] = 1
    dataset.loc[(dataset['age'] > 32) & (dataset['age'] <= 48), 'age'] = 2
    dataset.loc[(dataset['age'] > 48) & (dataset['age'] <= 64), 'age'] = 3
    dataset.loc[ dataset['age'] > 64, 'age'] = 4 

    dataset['fare'] = dataset['fare'].fillna(train['fare'].median())
    #dataset['fare'] = pd.qcut(train['fare'], 4)
    dataset.loc[ dataset['fare'] <= 7.91, 'fare'] 						        = 0
    dataset.loc[(dataset['fare'] > 7.91) & (dataset['fare'] <= 14.454), 'fare'] = 1
    dataset.loc[(dataset['fare'] > 14.454) & (dataset['fare'] <= 31), 'fare']   = 2
    dataset.loc[ dataset['fare'] > 31, 'fare'] 							        = 3
    dataset['fare'] = dataset['fare'].astype(int)

x_train = train.iloc[:,[1,2,3,7]]
y = train.iloc[:,0]
x_test = test.iloc[:,[0,1,2,6]]

from sklearn import svm
svc = svm.SVC(
              C = 1.0, # c is c 
              kernel = 'rbf', # inear poly sigmoid precomputed
              decision_function_shape = 'ovo' )# ovr

svc.fit(x_train,y)
result=svc.predict(x_test)



from sklearn import linear_model
log = linear_model.LogisticRegression()
log.fit(x_train,y)
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(x_train,y)
result2=knn.predict(x_test)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10)
rfc.fit(x_train,y)
result3=rfc.predict(x_test)

for i in range(len(result)):
    positive = 0
    for count in [result,result1,result2,result3]:
        if count[i] == 1:
            positive +=1
    if positive > 2:
        count[i]=1
 
result_file = pd.DataFrame({'PassengerId':test_pre['PassengerId'],
                            'Survived':result3})
result_file.to_csv('result.csv',index=False)           