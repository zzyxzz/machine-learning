import numpy as np
from math import log
import operator

def cal_entropy(dataset):
    num = float(len(dataset))
    label_count = {}
    for entry in dataset:
        label = entry[-1]
        label_count[label] = label_count.get(label,0)+1
    entropy = 0.0
    for key in label_count:
        prob = label_count[key]/num
        entropy += -prob*log(prob,2)
    return entropy

def split_dataset(dataset, feature, value):
    new_dataset = []
    for entry in dataset:
        if int(entry[feature]) == value:
            reduced_vec = entry[:feature]
            reduced_vec.extend(entry[feature+1:])
            new_dataset.append(reduced_vec)
    return new_dataset

def best_to_split(dataset):
    num_features = len(dataset[0])-1
    base_entropy = cal_entropy(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feature_list = [ex[i] for ex in dataset]
        unique_vals = set(feature_list)
        new_entropy = 0.0
        for value in unique_vals:
            sub_dataset = split_dataset(dataset, i, value)
            prob = len(sub_dataset)/float(len(dataset))
            new_entropy += prob*cal_entropy(sub_dataset)
        info_gain = base_entropy - new_entropy
        if(info_gain > best_info_gain):
            best_info_gain = info_gain
            best_feature = i
    return best_feature

def majority_class(class_list):
    class_count = {}
    for vote in class_list:
        class_count[vote] = class_count.get(vote,0)+1
    sorted_class_count = sorted(class_count.iteritems(),
                                key=operator.itemgetter(1),reverse=True)
    return sorted_class_count[0][0]
        
def decision_tree_id3(dataset, labels):
    class_list = [ex[-1] for ex in dataset]
    if len(set(class_list))==1:
        return class_list[0]
    if len(dataset[0]) == 1:
        return majority_class(class_list)
    best_feature = best_to_split(dataset)
    best_feature_label = labels[best_feature]
    d_tree = {best_feature_label:{}}
    del(labels[best_feature])
    feature_vals = [ex[best_feature] for ex in dataset]
    unique_vals = set(feature_vals)
    for value in unique_vals:
        sub_labels = labels[:]
        d_tree[best_feature_label][value] = decision_tree_id3(
            split_dataset(dataset, best_feature, value),sub_labels)
    return d_tree

#=====================
if __name__ == '__main__':
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    feature_names = ['no surfacing', 'flippers']
    entropy = cal_entropy(dataset)
    f = decision_tree_id3(dataset,feature_names)
    print f
