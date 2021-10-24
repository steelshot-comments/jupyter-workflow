import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("sports_data.csv")
#data.drop(columns=['sports'])
y = data['sports']
x = data.drop(columns = ['sports'])
#x = data['age','gender']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
#print(x)
#print(y)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

#result = model.predict([[26, 0], [33, 1]])
print(x_test)
res = model.predict(x_test)
res

score = accuracy_score(y_test, res)
score
