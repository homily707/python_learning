from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.losses import categorical_crossentropy

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def decimal(x):
    x = x.astype('float32')
    x /= 255
    return x

x_train,x_test = map(decimal,[x_train,x_test])
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

dataset = Input(shape=(28,28,1))
conv = Conv2D(3,(5,5),activation='relu')(dataset)
pool = MaxPooling2D((2,2))(conv)
flat = Flatten()(pool)
result = Dense(10,activation='softmax')(flat)

model = Model(inputs=dataset,outputs=result)
model.compile(loss=categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])