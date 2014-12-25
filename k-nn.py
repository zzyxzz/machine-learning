import numpy as np
import operator

'''
K-nearest neighbour

input:     inX: input vector for classification 1xN (N features)
           dataset(numpy array): existing and known vectors MxN (N features)
           labels: dataset labels 1xM
           k: number of neighbours (should be odd number)
return:    predicted class label
'''

def knn(inX, dataset, labels, k, norm = False):
    dataset_size = dataset.shape[0]
    if norm:
        dataset, ranges, min_values = normalisation(dataset)
        inX = (inX - min_values) / ranges

    #calculate distance
    diff_values = np.tile(inX, (dataset_size,1)) - dataset
    square_diff_values = diff_values**2
    distance = np.sqrt(square_diff_values.sum(axis=1))

    #return indices of sorted distance
    sorted_distance_indices = distance.argsort()
    class_count = { }
    for i in xrange(k):
        vote_label = labels[sorted_distance_indices[i]]
        class_count[vote_label] = class_count.get(vote_label,0) + 1
    
    #sort class_count by values (descending order)
    sorted_class_count = sorted(class_count.iteritems(),
                                key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def normalisation(dataset):
    #get minimum and maximum values of each column (feature)
    min_values = dataset.min(0)
    max_values = dataset.max(0)
    
    #normalised(e) = (e - e_min)/(e_max - e_min)
    dataset_size = dataset.shape[0]
    diff_dataset = dataset - np.tile(min_values, (dataset_size,1))
    feature_ranges = max_values - min_values
    norm_dataset = diff_dataset/np.tile(feature_ranges, (dataset_size,1))

    return norm_dataset, feature_ranges, min_values
    

#==============
if __name__ == '__main__':
    group = np.array([
            [1, 1.1],
            [1, 1],
            [0, 0],
            [0, 0.1]])
    labels = ['A','A','B','B']
    label = knn([0,0], group, labels, 3, True)
    data = normalisation(group)
    print data
    print label
