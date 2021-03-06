
"""
Spyder Editor

This is a temporary script file.
"""

from keras.models import Sequential
from keras.layers import Dense

import numpy as np

np.random.seed(7)

dataset = np.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]

model = Sequential()

model.add(Dense(12, input_dim=8,init='uniform', activation='relu'))
model.add(Dense(8,init='uniform', activation='relu'))
model.add(Dense(1,init='uniform', activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X,Y, epochs=1500, batch_size=10)

scores = model.evaluate(X, Y)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


print("#"*100)
print("Doing some predictions")

predictions = model.predict(X)


rounded = [round(x[0]) for x in predictions]
print(rounded)
