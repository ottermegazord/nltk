#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from email_parser import parseOutText

"""
    dataset in pickle format
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

temp_counter = 0

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        temp_counter += 1 # samples 200 first
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            parsedEmail = parseOutText(email)

            list_rep = ["sara", "shackleton", "chris", "germani"]
            for i in list_rep:
                parsedEmail = parsedEmail.replace(i, "")

            word_data.append(parsedEmail)

            from_data.append(0 if name == "sara" else 1)


            #email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

print word_data[152]


from sklearn.feature_extraction.text import TfidfVectorizer

# remove english stop words
vectorizer = TfidfVectorizer(stop_words = 'english')
vectorizer.fit_transform(word_data)
print len(vectorizer.get_feature_names())
print vectorizer.get_feature_names()[34596]