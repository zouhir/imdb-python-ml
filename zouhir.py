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
    
