#!/usr/bin/python
# -*- coding:UTF-8 -*-
import cPickle
import numpy



def make_3_file(filename):
    #将输入的文件分成3分，分别是train,valid,test;
    data = cPickle.load(open(filename,"rb"))
    tot_len = len(data);
    train_len = int(0.7 * tot_len);
    valid_len = int(0.1 * tot_len);
    test_len = tot_len - train_len - valid_len;
    train_data = data[:train_len];
    valid_data = data[train_len:train_len+valid_len];
    test_data = data[train_len+valid_len:];
    cPickle.dump(train_data,open("train_%s"%(filename),"wb"));
    cPickle.dump(valid_data,open("valid_%s"%(filename),"wb"));
    cPickle.dump(test_data ,open("test_%s"%(filename),"wb"));
    

if __name__ == "__main__":
    make_3_file("all_together2.pkl");
   
