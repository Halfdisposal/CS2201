import numpy as np
import matplotlib.pyplot as plt
import random



def calcDist( point, points):
    dists = []
    for p in points:
        dists.append(((point[0] - p[0])**2 + (point[1] - p[1])**2)**0.5)
    return dists 
def findFirstMin(X, y_train, dists, k):
    n_points = X.shape[0]
    nearestn = []
    nearest_labels = []
    for i in range(dists.shape[0]):
        nearest_for_i = []
        i_label = []
        for j in range(min(k, n_points) + 1):
            dist_arr_for_i = dists[i]
            min_index = np.argmin(dist_arr_for_i)
            if min_index != i:
                nearest_for_i.append(min_index)
                i_label.append(y_train[min_index])
            dist_arr_for_i[min_index] = np.inf
        
        nearestn.append(nearest_for_i)
        nearest_labels.append(i_label)
        
    return nearestn, nearest_labels


def fit( X, y, k):
    n_points = X.shape[0]
    dists = []
    for i in range(n_points):
        dists.append(calcDist(X[i], X))
    dists = np.array(dists)
    nearest_neighbors, labels = findFirstMin(X, y, dists, k)
    final_labels = []
    for i in range(len(labels)):
        label_count = {}
        for label in labels[i]:
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1
        final_labels.append(max(label_count, key=label_count.get))
    return final_labels

def confusionMat(X, y, pred_labels):
    confusion_matrix = np.zeros((2, 2))
    for i in range(len(pred_labels)):
        confusion_matrix[y[i]][pred_labels[i]] += 1
    return confusion_matrix

def score(X, y, pred_labels):
    correct = 0
    for i in range(len(pred_labels)):
        if pred_labels[i] == y[i]:
            correct += 1
    return correct / len(pred_labels)
