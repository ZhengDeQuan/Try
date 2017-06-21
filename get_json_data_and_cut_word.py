#!/usr/bin/python
# -*- coding:UTF-8 -*-

import json
import jieba
import os
import cPickle;
filename = "all_train.json"
stopwords_list = cPickle.load(open("stopwords_list.pkl","rb"));
stopwords_list = set(stopwords_list);

def cal_wordco1(l1 , l2):
    return len(set(l1)&set(l2));

def cal_wordco2(l1 , l2):
    l3 = set(l1) & set(l2);
    return len(l3) - len(l3 & stopwords_list);

def cal_Jaccard1(l1, l2):
    l3 = set(l1) & set(l2)
    l4 = set(l1) | set(l2);
    return len(l3) * 1.0 / (len(l4) + 1.0);

def cal_Jaccard2(l1, l2):
    l3 = set(l1) & set(l2)
    l4 = set(l1) | set(l2);
    return (len(l3) - len(l3 & stopwords_list))* 1.0 / (len(l4) - len(l4 & stopwords_list) + 1.0);

def cal_4features(l1 , l2):
    return cal_wordco1(l1,l2) , cal_wordco2(l1,l2) , cal_Jaccard1(l1,l2) , cal_Jaccard2(l1 ,l2);


def read_json_file(filename):
    with open(filename , "r") as json_file:
        json_data = json_file.read();
    json_data = json_data.split("\n");#转化为列表
    que_cutted , ans_cutted , labels = [] , [] , [];#这里的que都还只是str的形式的，只不过分完词了
    qids ,aids  = [] , [] ;
    wordco1 , wordco2 = [] , [];
    Jaccard1 , Jaccard2 = [] , [];
    
    sentence_to_get_wordvec = [];#这是为了得到单词对应的词向量而存的问题和答案，每个问题只存储一次
    all_together = [];#qid que aid ans label(0,1,2) wordco1 wordco2 j1 j2
    item = [];#qid que aid ans label(0,1,2) wordco1 wordco2 j1 j2
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
        que = " ".join(jieba.cut(que , cut_all = False));#分完词了，不是str是unicode
        que = que.split(" ");
        new_que = [];
        for word in que:
            if len(word) > 0 :
                new_que.append(word);
        sentence_to_get_wordvec.append(new_que);
        for ans_line in line["passages"]:
            #ans_line是列表中的一个元素，也是字典
            aid = int(ans_line["passage_id"])
            ans = ans_line["passage_text"];
            ans = " ".join(jieba.cut(ans , cut_all = False));
            ans = ans.split(" ");
            new_ans = [];
            for word in ans:
                if len(word) > 0:
                    new_ans.append(word);
            sentence_to_get_wordvec.append(new_ans);
            label = int(ans_line["label"])
            qids.append(qid)
            que_cutted.append(new_que)
            aids.append(aid)
            ans_cutted.append(new_ans)
            labels.append(label)

            wco1,wco2,ja1,ja2 = cal_4features(new_que , new_ans);
            wordco1.append(wco1)
            wordco2.append(wco2)
            Jaccard1.append(ja1)
            Jaccard2.append(ja2)
            item = [qid ,new_que , aid ,new_ans , label , wco1 , wco2 , ja1 , ja2];
            all_together.append(item);
    return sentence_to_get_wordvec , qids , que_cutted , aids , ans_cutted , labels , wordco1 , wordco2 , Jaccard1 , Jaccard2, all_together;


if __name__ == "__main__":
    sentence_to_get_wordvec , qids , que_cutted , aids , ans_cutted , labels , wordco1 , wordco2 , Jaccard1 , Jaccard2 ,all_together = read_json_file(filename);
    cPickle.dump(sentence_to_get_wordvec , open("sentence_to_get_wordvec.pkl","wb"));
    cPickle.dump(qids , open("qids.pkl","wb"))
    cPickle.dump(que_cutted , open("que_cutted.pkl","wb"))
    cPickle.dump(aids , open("aids.pkl","wb"))
    cPickle.dump(ans_cutted , open("ans_cutted.pkl","wb"))
    cPickle.dump(labels , open("labels.pkl","wb"))
    cPickle.dump(wordco1, open("wordco1.pkl","wb"));
    cPickle.dump(wordco2, open("wordco2.pkl","wb"));
    cPickle.dump(Jaccard1,open("Jaccard1.pkl","wb"));
    cPickle.dump(Jaccard2,open("Jaccard2.pkl","wb"));
    cPickle.dump(all_together , open("all_together.pkl","wb"));

