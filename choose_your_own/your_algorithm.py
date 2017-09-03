#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.clf()
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary


from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC


# clf = KNeighborsClassifier(n_neighbors=25)
# for split in range(2, 50, 5):
#     clf = RandomForestClassifier(min_samples_split=2, n_estimators=split)
#     clf.fit(features_train, labels_train)
#     pred = clf.predict(features_test)
#     print "kmeans classifier", "split", split, "accuracy", accuracy_score(labels_test, pred)
# clf = RandomForestClassifier(min_samples_split=12)
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)
# print "kmeans classifier", "accuracy", accuracy_score(labels_test, pred)


# for split in range(1):
#      clf = AdaBoostClassifier(DecisionTreeClassifier())
#      clf.fit(features_train, labels_train)
#      pred = clf.predict(features_test)
#      print "adaboost", "split", split, "accuracy", accuracy_score(labels_test, pred)

clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), learning_rate=0.1)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "adaboost", "accuracy", accuracy_score(labels_test, pred)

# clf = SVC()
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)
# print "svc", "accuracy", accuracy_score(labels_test, pred)

try:
    prettyPicture(clf, features_test, labels_test)
    print "completed pretty picture"
except NameError:
    pass
