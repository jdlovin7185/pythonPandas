import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# importing and fitting the model on training set
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# if we run this program with this file, we will get negative coef and intercept
# df = pd.read_csv('auto-mpg.csv')
# if we run the program with this file, we will get more accurate data because of the origins of column
df = pd.read_csv('auto_mpg.csv')

# dropping null-values
df.dropna(inplace=True)

# df.info()

# creating a matrix of predictors
x = df.iloc[:, 1:8]

# creating a target
y = df.iloc[:, 0]

x = pd.get_dummies(x)
# print(x)

# test_size is equal to the percentage, in this case its 20% hence 0.2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# applying standard scaler on the data
scale = StandardScaler()
scale.fit_transform(x_train)
scale.transform(x_test)

reg = LinearRegression()

# fitting the model on training data
reg.fit(x_train, y_train)

# checking the coefficient and intercept
# 'm' represents the coefficient and 'c' represents the intercept
m = reg.coef_
c = reg.intercept_
# print(m, c)

# predicting the target: mpg against the predictors in the training data set
# predicted data store in y_pred_train
y_pred_train = reg.predict(x_train)

# predicting the target: mpg against the predictor in the testing data set
# predicted data stored in y_pred_test
y_pred_test = reg.predict(x_test)

# prediction accuracy in terms of how close si the predicted value of target: mpg
# to the real value in training data set
# r2_s = r2_score(y_train, y_pred_train)
# returned -> 0.9060446973140711
# returned -> 0.8194239716903474, new file
r2_s = r2_score(y_test, y_pred_test)
# returned -> -2.812096220463178e+17
# returned -> 0.8387519287083123, new file
print(r2_s)

