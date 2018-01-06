import struct
import numpy as np

with open('train-images.idx3-ubyte','rb') as trainfile:
    buf = trainfile.read()

index = 0
magic, numImages , numRows , numColumns = struct.unpack_from(
        '>IIII' , buf , index)

index += 16
train = []
for i in range(numImages):
    train += struct.unpack_from('>784B',buf,index)
    index += 784
    print ('%d'%i,end=' ')
train = np.array(train).reshape(-1,784)

with open('train-labels.idx1-ubyte','rb') as f:
    buf = f.read()

index = 8
train_label=[]
for i in range(60000):
    train_label += struct.unpack_from('B',buf,index)
    index += 1
    if (i%10000 == 0):
        print(i)
train_label = np.array(train_label)

np.save('train',train)
np.save('train_l',train_label)