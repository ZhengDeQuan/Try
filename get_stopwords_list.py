#!/usr/bin/python
# -*- coding:UTF-8 -*-

import cPickle
import re

filename = "stopwords.txt"
with open(filename,"r") as stopf:
    stopwords_list = stopf.read();
#stopwords_list = re.split(' |\n',stopwords_list)
stopwords_list = stopwords_list.decode("utf-8");
stopwords_list = stopwords_list.split(" ")
cPickle.dump(stopwords_list , open("stopwords_list.pkl","wb"))
