from sklearn import tree
# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# storing the list of labels which is a gender.
# Each label is associated with a list of body metrics
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#initializing the decision tree classifier
clf = tree.DecisionTreeClassifier()

#using the fit method to train the decision tree on the dataset
clf = clf.fit(X,Y)

#testing the decision using a new list of body metrics
prediction = clf.predict([[190,70,43],[170,62,42]])

#print prediciton
print prediction
