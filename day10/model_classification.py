from sklearn.linear_model import LogisticRegression

# Create a logistic regression classifier
classifier = LogisticRegression()

# Training data
X_train = [[2, 4], [1, 2], [4, 6], [5, 2]]
y_train = [0, 1, 1, 1]

# Train the classifier
classifier.fit(X_train, y_train)

# Test data
X_test = [[3, 5], [7, 2]]

# Make predictions
predictions = classifier.predict(X_test)
print(predictions)
