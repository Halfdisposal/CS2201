# Necessary imports
import numpy as np
import matplotlib.pyplot as plt
import heapq

# Generate random training dataset
data1x = np.random.uniform(2,4,size=(50))
data1y = np.random.uniform(2,4,size=(50))
data2x = np.random.uniform(4,6,size=(50))
data2y = np.random.uniform(4,6,size=(50))
data3x = np.random.uniform(1,3,size=(50))
data3y = np.random.uniform(4,6,size=(50))

# Rearrange datasets into three arrays: x_data, y_data and classes
x_data = np.concatenate((data1x, data2x, data3x))
y_data = np.concatenate((data1y, data2y, data3y))
classes = np.concatenate((np.ones_like(data1x), 2*np.ones_like(data2x), 3*np.ones_like(data3x)))

test_point = [3.5,4.0]

# Plot training dataset
plt.scatter(data1x,data1y,c="red",label="Class1")
plt.scatter(data2x,data2y,c="blue",label="Class2")
plt.scatter(data3x,data3y,c="green",label="Class3")

# Plot test datapoint
# plt.scatter([3.5],[4.0],c="magenta",s=80,label="Test datapoint")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.title("Training dataset for classification")
plt.legend()
plt.show()


# Define functions
def distance(x, y, point):
    """calculates the Euclidean distance between point and coordinates (x,y)"""
    return np.sqrt((x-point[0])**2 + (y-point[1])**2)

def majority(classes):
    """calculates the class with the highest frequency in the array classes"""
    class_freq = {} # initializes a dictionary for storing class:frequency pairs
    for cl in classes: # iterates over the classes
        if cl not in class_freq: # checks if the class value is not already present in the dictionary
            class_freq[cl] = 1 # initializes the frequency at 1
        else: # this means the class value is already present in the dictionary
            class_freq[cl] = class_freq[cl] + 1 # increases the frequency by 1
        
    max_freq = -1 # placeholder value
    max_freq_label = -1 # placeholder value
    
    for cl in class_freq:    
        if class_freq[cl] > max_freq: # checks if frequency of current class is higher than max_freq
            max_freq = class_freq[cl] # updates max_freq
            max_freq_label = cl # updates max_freq_label
     
    # print results        
    print(f"The class with the highest frequency is {max_freq_label}, with a frequency of {max_freq}")        
    
    # returns max frequency from the classes array
    return max_freq_label
    
def kNN(x_data, y_data, classes, k, point):
    """assigns class to point (test data) for k nearest neighbors from training data of {class:(x,y)}"""
    
    # create a list with distances to each datapoint in every label from test datapoint, also store the index
    distances = []
    for i in range(len(classes)):
        dist = distance(x_data[i], y_data[i], point)
        distances.append((dist, classes[i], i))

    # use heapq to get the K smallest (distance, class, index) values
    k_smallest = heapq.nsmallest(k, distances, key=lambda x: x[0])
    neighbor_classes = [x[1] for x in k_smallest]
    neighbor_indices = [x[2] for x in k_smallest]

     # call majority function to find the class with the highest frequency among the k classes
    knn_class = majority(neighbor_classes)
    return knn_class, neighbor_indices

# Run kNN and get results
k = 20
predicted_class, neighbor_indices = kNN(x_data, y_data, classes, k, test_point)

print(f"\nThus, the test point is most likely to be in class {predicted_class}")

# Plot results
colors = ['red', 'blue', 'green']
labels = ['Class 1', 'Class 2', 'Class 3']

for i in range(3):
    mask = classes == (i + 1)
    plt.scatter(x_data[mask], y_data[mask], c=colors[i], label=labels[i])

# Plot test point
plt.scatter([test_point[0]], [test_point[1]], c='magenta', s=80, label='Test Point')

# Highlight the k nearest neighbors with black circles
plt.scatter(x_data[neighbor_indices], y_data[neighbor_indices], 
            facecolors='none', edgecolors='black', s=120, linewidths=1.5, label='k Nearest Neighbors')

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("kNN Classification and Nearest Neighbors")
plt.legend()
plt.show()
