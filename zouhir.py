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
# step1: we remove everything that is not a-z and A-Z
import re
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])

# step2: all lower case
review = review.lower()

# step3: remove non significant word
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

review = review.split()
# step4: stemming 
ps = PorterStemmer()

review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]

review= ' '.join(review);