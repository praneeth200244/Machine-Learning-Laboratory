# Question 5
# Write a program to develop the Naive Bayes classifier on Titanic dataset.
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv('Titanic.csv')

df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Fare'].fillna(df['Fare'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

train1, test1 = train_test_split(df, test_size=0.2, random_state=41)

X_train1 = train1.drop('Survived', axis=1)
y_train1 = train1['Survived']
X_test1 = test1.drop('Survived', axis=1)
y_test1 = test1['Survived']


class NaiveBayesClassifier:
    def __init__(self):
        self.prior = {}
        self.conditional = {}

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)

        for c in self.classes:
            self.prior[c] = np.mean(y == c)

        for feature in X.columns:
            self.conditional[feature] = {}
            for c in self.classes:
                feature_values = X[feature][y == c]
                self.conditional[feature][c] = {
                    'mean': np.mean(feature_values),
                    'std': np.std(feature_values)
                }

    def predict(self, X):
        y_pred = []
        for _, sample in X.iterrows():
            probabilities = {}
            for c in self.classes:
                probabilities[c] = self.prior[c]
                for feature in X.columns:
                    mean = self.conditional[feature][c]['mean']
                    std = self.conditional[feature][c]['std']
                    x = sample[feature]
                    probabilities[c] *= self._gaussian_pdf(x, mean, std)
            y_pred.append(max(probabilities, key=probabilities.get))
        return y_pred

    @staticmethod
    def _gaussian_pdf(x, mean, std):
        exponent = np.exp(-((x-mean)**2)/(2*std**2))
        return (1/(np.sqrt(2*np.pi)*std))*exponent


classifier = NaiveBayesClassifier()
classifier.fit(X_train1, y_train1)
y_pred = classifier.predict(X_test1)
cm = confusion_matrix(y_test1, y_pred)
print("Confusion Matrix")
print(cm)
accuracy = np.mean(y_pred == y_test1)
print("Accuracy ", accuracy)
