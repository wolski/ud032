#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials at
the following link:
https://www.udacity.com/wiki/ud032
"""

from pymongo import MongoClient


def find_porsche(db, query):
    return db.myautos.find(query)


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    query = {u'manufacturer': u'Mazda'}
    p = db.myautos.find(query)

    #import pprint
    print p