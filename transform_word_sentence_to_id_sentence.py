#!/usr/bin/python
# -*- coding:UTF-8 -*-
#将que_cutted.pkl和ans_cutted.pkl；两个文件中的内容转换为id化的表示
import cPickle
import re
import os
in_files=["que_cutted.pkl","ans_cutted.pkl"]

out_files=["que_idlized.pkl","ans_idlized.pkl"]

word2id = cPickle.load(open("word2id.pkl","rb"))

def transform(filename):
    mf = cPickle.load(open(filename,"rb"));
    mf_out = [];
    
    new_line = [];
    for line in mf:
        new_line = [];
        for word in line:
            if word in word2id and word2id[word] < 184810:
                new_line.append(word2id[word])
            else:
                new_line.append(word2id["<unk>"])
        mf_out.append(new_line);
    return mf_out;

if __name__ == "__main__":
    for in_name , out_name in zip(in_files, out_files):
        mf_out = transform(in_name)
        cPickle.dump(mf_out,open(out_name,"wb"));

