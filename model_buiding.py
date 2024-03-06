import pickle

# Load the Iris dataset
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25)

# Train a Support Vector Machine (SVM) classifier
from sklearn.svm import SVC
clf = SVC()
clf.fit(X_train, y_train)

# Pickle the trained model
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(clf, f)