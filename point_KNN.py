def calcDist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def findLabels(labels):
    Labels = []
    for label in labels:
        counts = {}
        for classes in label:
            if classes in counts:
                counts[classes] += 1
            else:
                counts[classes] = 1
        sorted_counts = sorted(counts, key = counts.get, reverse=True)
        Labels.append(sorted_counts[0])
    return Labels

def KNN(data, labels, point, k):
    distances = []
    for i in range(data.shape[0]):
        d = calcDist(point, data[i])
        distances.append((d, i, labels[i]))
    neighbors = heapq.nsmallest(k, distances, key=lambda x: x[0])
    idxs = [x[2] for x in neighbors]
    label = findLabels([idxs])
    return label

p = [25, 40]
l = KNN(data, labels, p, 7)[0]
c = {0:'blue', 1:'red'}
class1 = np.array([data[i] for i in range(0, len(labels)) if labels[i] == 0])
class2 = np.array([data[i] for i in range(0, len(labels)) if labels[i] == 1])
l1 = [0]*labels.count(0)
l2 = [1]*labels.count(1)

plt.scatter(class1[:, 0], class1[:, 1], c = 'blue', label='0')
plt.scatter(class2[:, 0], class2[:, 1], c = 'red', label='1')
plt.scatter(p[0], p[1], c=c[l])
plt.scatter(p[0], p[1], facecolor = 'none', edgecolors='black', s=150, linewidths=1.5)
plt.legend()
plt.show()


