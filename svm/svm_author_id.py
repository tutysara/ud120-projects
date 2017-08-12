#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
from sklearn import svm
c_values = [10000]
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
for c in c_values:
    clf = svm.SVC(kernel="rbf", C=c)
    t0 = time()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    t1 = time()
    print "time taken to train : " + str(t1-t0) + " sec"
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(labels_test, pred)
    print "c:", c, "accuracy", accuracy
    pred_indexs = [10, 26, 50]
    for pred_index in pred_indexs:
        print "prediction for", pred_index, pred[pred_index]
