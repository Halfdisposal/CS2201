import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import math
import heapq 
from sklearn.model_selection import train_test_split

data = load_digits()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

class KNN:
    def __init__(self, X, y, k = 3):
        self.X = X
        self.y = y 
        self.k = k
        self.X_test = []
        self.y_pred = []
        self.y_test = []
    def findDist(self, point):
        dist = []
        for p, l in zip(self.X, self.y):
            d = 0
            for ptrain, ptest in zip(p, point):
                d += (ptrain - ptest)**2
            d = d**0.5
            dist.append((d.item(), l.item()))
        return dist
    def findLabel(self, point):
        dists = self.findDist(point)
        min_dists = heapq.nsmallest(self.k, dists, key=lambda x: x[0])
        labels = [x[1] for x in min_dists]
        return min_dists, labels
    def predict(self, X_test, y_test = None):
        self.X_test = X_test
        self.y_test = y_test
        for point in X_test:
            dists, labels = self.findLabel(point)
            counts = {}
            for l in labels:
                if l in counts:
                    counts[l] += 1
                else:
                    counts[l] = 1
            
            label = sorted(counts, key = counts.get)[0]
            self.y_pred.append(label)
        return self.y_pred
    def score(self):
        scores = list(self.y_pred == self.y_test)
        counts = scores.count(np.True_)
        return counts/len(scores)
    def confusionMat(self):
        num_classes = len(np.unique(self.y_test))  # Determine the number of classes
        confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)  # Initialize matrix
        for i in range(len(self.y_pred)):
            confusion_matrix[self.y_test[i]][self.y_pred[i]] += 1
        return confusion_matrix





m ,n = 4, 2
knn = KNN(X_train, y_train, 4)
labels = knn.predict(X_test, y_test)
print(knn.score())
print(knn.confusionMat())


