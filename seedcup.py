import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

x_train = np.load('C:\\Users\\homily\\py\\keras\\x_train.npy')
y_train = np.load('C:\\Users\\homily\\py\\keras\\y_train.npy')
x_test = np.load('C:\\Users\\homily\\py\\keras\\x_test.npy')


model = Sequential()
model.add(Dense(8, input_dim=8, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

what=[]
for i in range(50):
    model.fit(x_train, y_train, epochs=10, batch_size=128)
    classes = model.predict(x_test)
    what.append(classes[0])

scores = model.evaluate(x_train, y_train)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
classes = model.predict(x_test)
print(classes[0])

np.savetxt('C:\\Users\\homily\\py\\keras\\y_test.txt',classes)
np.savetxt('C:\\Users\\homily\\py\\keras\\results\\y_test.txt',classes)


