from sklearn.linear_model import LinearRegression

#----- Training Set
X = [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y = [[7], [9], [13], [17.5], [18]]


model = LinearRegression()
model.fit(X, y)

#------ Test Set

X_test = [[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]]
y_test = [[11], [8.5], [15], [18], [11]]

#------------- run the model against test set
predictions = model.predict(X_test)
 
#---- Print Predicted Value and Output

for i, prediction in enumerate(predictions):
	print 'Predicted: %s, Target: %s' % (prediction, y_test[i])
	print 'R-squared: %.2f' % model.score(X_test, y_test)