#!/usr/bin/python
# -*- coding:UTF-8 -*-


import json
import jieba
import os
import cPickle;
import chardet;
import sys
'''
#reload(sys)
#sys.setdefaultencoding('UTF-8')
#gbk,gb2312,gb18030
que_txt = open("que.txt","w");
filename = "train.2.json"
stopwords_list = cPickle.load(open("stopwords_list.pkl","rb"));
stopwords_list = set(stopwords_list);
if __name__ == "__main__":
   
    #s = cPickle.load(open("stopwords_list.pkl","rb"))
    with open(filename , "r") as json_file:
        json_data = json_file.read();
    
    json_data = json_data.split("\n");#转化为列表
    for line in json_data:
        #line现在是字符串
        if len(line) == 0 :
            continue;
        line = json.loads(line);#是dict. query_id ,query , passages
                                #passages是个列表一般有10个元素，至少有一个元素，
                                #每个元素都是一个字典：passage_id,url,passage_text,label
        qid = int(line["query_id"]);
        que = line["query"];
        que = que.strip(" ");
        que = " ".join(jieba.cut(que , cut_all = False));#分完词了，但是还是str每个词之间用空格分隔
        que = que.split(" ")
        for word in que:
            if len(word) > 0:
                word = word.encode("gbk")
                que_txt.write(word)
                que_txt.write(" ");
        que_txt.write("\n")
'''
#labels = cPickle.load(open("labels.pkl","rb"))
'''
filename = "all_train.json"
with open(filename , "r") as json_file:
    json_data = json_file.read();
json_data = json_data.split("\n");#转化为列表
print len(json_data);
filename = "train.2.json"
with open(filename , "r") as json_file:
    json_data = json_file.read();
json_data = json_data.split("\n");#转化为列表
print len(json_data)
'''
'''
#get train_temporary.pkl
t_t = cPickle.load(open("train_all_together2.pkl","rb"))
t_t = t_t[6*256:10*256];
cPickle.dump(t_t,open("train_temporary.pkl","wb"));

t_t = cPickle.load(open("valid_all_together2.pkl","rb"))
t_t = t_t[6*256:10*256];
cPickle.dump(t_t,open("valid_temporary.pkl","wb"));

t_t = cPickle.load(open("test_all_together2.pkl","rb"))
t_t = t_t[6*256:10*256];
cPickle.dump(t_t , open("test_temporary.pkl","wb"))
'''

with open("all_train.json","r") as f:
    json_data = f.read();
json_data = json_data.split("\n");
L = len(json_data)//60;
for i in range(59):
    J = json_data[i*L : (i+1)*L];
    cPickle.dump(J,open("J_%d.pkl"%(i),"wb"));

J = json_data[59*L:];
cPickle.dump(J,open("J_59.pkl","wb"));

'''
J = [];
for i in range(30):
    J1 = cPickle.load(open("J_%d.pkl"%(i),"rb"));
    J += J1;

print len(J);
cPickle.dump(J,open("J.pkl","wb"));
'''
