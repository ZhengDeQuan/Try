#!/usr/bin/python
# -*- coding:UTF-8 -*-

import gensim
import os
import cPickle
import numpy
model = gensim.models.Word2Vec();
sentence = cPickle.load(open("sentence_to_get_wordvec.pkl","rb"))
dimension_of_word_vector = 120;#词向量维度是120

def get_word2times(sentence):
    word2times = {};
    for sent in sentence:
        for word in sent:
            if (word not in word2times) and (len(word) > 0):
                word2times[word] = 0;
            else :
                word2times[word] += 1;
    #sorted(word2times.iteritems() , key = lambda a : a[1] , reverse = True);
    return word2times;

def get_word2id(sentence,word2times):
    word2id = {};
    idx = 0;
    word2id["<unk>"] = idx;
    idx += 1;
    new_sentence = [];
    new_sent = [];
    for sent in sentence:
        #sent是一个句子中单词的列表
        new_sent = [];
        for word in sent :
            if (len(word) > 0) and (word2times[word] > 5):
                new_sent.append(word);
                if word not in word2id:
                    word2id[word] = idx;
                    idx += 1;
            else :
                new_sent.append("<unk>");
        new_sentence.append(new_sent);
    return new_sentence , word2id;

def get_word2vec_and_id2vec(word2id):
    word2vec = {};
    id2vec = {};
    id2vec_array = [];
    '''
    for i in range(len(word2id)):
        id2vec_array.append(numpy.ones(dimension_of_word_vector)*0.01);
    '''
    for word , idx in word2id.items():#225367个item，但是下面的id2vec却只有184810
        #print idx;
        if idx == 0:
            word2vec[word]=numpy.ones(dimension_of_word_vector)*0.01;
            id2vec[idx]=numpy.ones(dimension_of_word_vector)*0.01;
            id2vec_array.append(numpy.ones(dimension_of_word_vector)*0.01);
            #id2vec_array[idx] = numpy.ones(dimension_of_word_vector)*0.01;
        else :
            word2vec[word]=model[word];
            id2vec[idx]=model[word];
            id2vec_array.append(model[word]);
            #id2vec_array[idx] = model[word];
    return word2vec , id2vec , id2vec_array;

if __name__ == "__main__":
    word2times = get_word2times(sentence);
    new_sentence , word2id = get_word2id(sentence,word2times);
    model = gensim.models.Word2Vec(sentence , min_count = 4 , size = dimension_of_word_vector);#词向量的维度是150
    word2vec , id2vec , id2vec_array= get_word2vec_and_id2vec(word2id)
    id2vec_array = numpy.array(id2vec);

    cPickle.dump(word2times , open("word2times.pkl","wb"));
    cPickle.dump(word2id , open("word2id.pkl","wb"));
    cPickle.dump(word2vec, open("word2vec.pkl","wb"));
    cPickle.dump(id2vec ,  open("id2vec.pkl","wb"));
    cPickle.dump(id2vec_array,open("id2vec.pkl","wb"));
    cPickle.dump(new_sentence , open("new_sentence.pkl","wb"));
