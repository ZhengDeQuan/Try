#!/usr/bin/python
# -*- coding:UTF-8 -*-

import cPickle;
filenames = ["qids.pkl","que_idlized.pkl","aids.pkl","ans_idlized.pkl",
             "labels.pkl","wordco1.pkl","wordco2.pkl","Jaccard1.pkl","Jaccard2.pkl"]

for i in range(len(filenames)):
    a = cPickle.load(open(filenames[i],"rb"));
    print len(a);
    
def put_all_together(filenames):
    all_together = [];
    qids = cPickle.load(open("qids.pkl","rb"));
    que_idlized = cPickle.load(open("que_idlized.pkl","rb"));
    aids = cPickle.load(open("aids.pkl","rb"));
    ans_idlized= cPickle.load(open("ans_idlized.pkl","rb"));
    labels= cPickle.load(open("labels.pkl","rb"));
    wordco1= cPickle.load(open("wordco1.pkl","rb"));
    wordco2= cPickle.load(open("wordco2.pkl","rb"));
    Jaccard1= cPickle.load(open("Jaccard1.pkl","rb"));
    Jaccard2= cPickle.load(open("Jaccard2.pkl","rb"));
    for qid , que , aid ,ans , label , wco1 , wco2 , ja1 ,ja2 in zip(qids,que_idlized,aids,ans_idlized,labels,wordco1,wordco2,Jaccard1,Jaccard2):
        item = [qid , que , aid ,ans , label , wco1 , wco2 , ja1 ,ja2];
        all_together.append(item);
    
    return all_together;


if __name__ == "__main__":
    all_together = put_all_together(filenames);
    cPickle.dump(all_together,open("all_together2.pkl","wb"))
