#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi = 0
for key in enron_data.keys():
    features = enron_data[key]
    print "processing recordd", key
    if features["poi"]:
        poi +=1
print poi

name = "James Prentice".upper()
name_tokens = name.split(" ")
for key in enron_data.keys():
    features = enron_data[key]
    print "processing recordd", key
    if sorted(name_tokens) == sorted(key.split(" ")):
        print "total stock value", features["total_stock_value"]
