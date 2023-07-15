import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def marks_prediction(marks):
  data=pd.read_csv("/content/train.csv")
  data.dropna(inplace=True)
  X=data['x']
  Y=data['y']
  X=X.reshape(-1,1)
  Y=Y.values.reshape(-1,1)

  model=LinearRegression()
  model.fit(X,Y)

  x_test=np.array(marks)
  x_test=x_test.reshape(-1,1)
  return model.predict(x_test)
