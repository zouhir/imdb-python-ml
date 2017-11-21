#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:04:43 2017

@author: zouhir
"""

import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;


# importing dataset
# convert delimiter from comma to tab
# ignore double quotes: quoting: 3
dataset = pd.read_csv('~/Projects/Py/Natural_Language_Processing/imdb.tsv', delimiter = '\t', quoting = 3);

# cleaning the text
import re



import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# in NLP corpus is collection of text
corpus = []

for i in range(0, 2000):
    # step1: we remove everything that is not a-z and A-Z
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    
    # step2: all lower case
    review = review.lower()
    review = review.split()
    # step3: remove non significant word
    # step4: stemming 
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review= ' '.join(review);
    corpus.append(review)
    
# bag of words
# Helps creating sprce matrix and reduce amount of words
# by hand it will be thousands of word and take us forver

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 5000)

# sparce matrix
X = cv.fit_transform(corpus).toarray()

#include the independent varibale so our machine can undertsan the corlelation
y = dataset.iloc[:, 1].values
 

"""

Naive Bayes implementation as in Weka it was the most accurate

"""

# split the dataset into training set and test set

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Add Naive Bayes to the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting results against test data
y_pred = classifier.predict(X_test)

# Make the confusion matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# accuracy
(131+132)/400