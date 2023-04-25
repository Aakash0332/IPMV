from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
gnb = GaussianNB().fit(X_train, y_train)
accuracy = metrics.accuracy_score(y_test, gnb.predict(X_test)) * 100

print(f'Gaussian Naive Bayes model accuracy (in %): {accuracy:.2f}')
print(X)
print(y)
