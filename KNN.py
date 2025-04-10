import numpy as np
import matplotlib.pyplot as plt
import random

class KNN:
    def __init__(self, n_neighbors = 5):
        self.k = n_neighbors
        self.pred_labels = None
    
    def calcDist(self, point, points):
        dists = []
        for p in points:
            dists.append(((point[0] - p[0])**2 + (point[1] - p[1])**2)**0.5)
        return dists 
    def findFirstMin(self, dists):
        nearestn = []
        nearest_labels = []
        for i in range(dists.shape[0]):
            nearest_for_i = []
            i_label = []
            for j in range(min(self.k, self.n_points) + 1):
                dist_arr_for_i = dists[i]
                min_index = np.argmin(dist_arr_for_i)
                if min_index != i:
                    nearest_for_i.append(min_index.item())
                    i_label.append(self.y_train[min_index].item())
                dist_arr_for_i[min_index] = np.inf
            
            nearestn.append(nearest_for_i)
            nearest_labels.append(i_label)
            
        return nearestn, nearest_labels


    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        
        self.n_points = X.shape[0]
        dists = []
        for i in range(self.n_points):
            dists.append(self.calcDist(X[i], X))
        dists = np.array(dists)
        nearest_neighbors, labels = self.findFirstMin(dists)
        final_labels = []
        for i in range(len(labels)):
            label_count = {}
            for label in labels[i]:
                if label in label_count:
                    label_count[label] += 1
                else:
                    label_count[label] = 1
            final_labels.append(max(label_count, key=label_count.get))
            self.pred_labels = final_labels
        return final_labels

    def confusionMat(self):
        confusion_matrix = np.zeros((2, 2))
        for i in range(len(self.pred_labels)):
            confusion_matrix[self.y_train[i]][self.pred_labels[i]] += 1
        return confusion_matrix
    
    def score(self):
        correct = 0
        for i in range(len(self.pred_labels)):
            if self.pred_labels[i] == self.y_train[i]:
                correct += 1
        return correct / len(self.pred_labels)
