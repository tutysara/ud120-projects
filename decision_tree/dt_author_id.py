#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn import tree
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
sys.path.append("../choose_your_own/")
from email_preprocess import preprocess
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train, labels_train, features_test, labels_test = makeTerrainData()




#########################################################
### your code goes here ###


#########################################################

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
for samples in [40]:
    clf = tree.DecisionTreeClassifier(min_samples_split=samples)
    t0 = time()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    t1 = time()
    print "time taken to train : " + str(t1-t0) + " sec"
    accuracy = accuracy_score(labels_test, pred)
    print "min_samples_split", samples, "accuracy", accuracy

    #prettyPicture(clf, features_test, labels_test)
