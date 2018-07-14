# -*- coding: utf-8 -*-
import random
import json
import codecs

"""
construct validation set: use original validation set, but remove those sample that exists in training data
so that training and validation set will not overlap.
"""
def construct_validation_set(valid_file_path,training_file_path,target_valid_file_path):
    # 1. read training/validation, get a id for each line from training
    valid_file_object = codecs.open(valid_file_path, mode='r', encoding='utf-8')
    valid_lines=valid_file_object.readlines()
    training_object = codecs.open(training_file_path, mode='r', encoding='utf-8')
    train_lines=training_object.readlines()
    target_valid_file_path = codecs.open(target_valid_file_path, mode='a', encoding='utf-8')

    # 2. loop each validation, remove those line exist in training, save to file system.
    dict_meta_id={}
    # training
    for j,linee in enumerate(train_lines):
        json_string = json.loads(linee.strip())
        accusation_list = json_string['meta']['accusation']
        article_list = json_string['meta']['relevant_articles']
        fact = json_string['fact'].strip()
        dict_meta_id[fact]=fact

    count=0
    count_add=0
    for i,line in enumerate(valid_lines):
        json_stringg = json.loads(line.strip())
        accusation_listt = json_stringg['meta']['accusation']
        article_listt = json_stringg['meta']['relevant_articles']
        factt = json_stringg['fact'].strip()
        if factt not in dict_meta_id: #save
            target_valid_file_path.write(line) #todo you need use this line
            count_add=count_add+1
        else: # print info for debug
            print(count,line)
            count=count+1

    target_valid_file_path.close()
    training_object.close()
    valid_file_object.close()
    #print("count_add:",count_add)

valid_file_path='../data/data_valid_checked.json' #TODO here should be: 'data_valid_checked.json'
training_file_path='../data_big/cail2018_big_downsmapled.json' #TODO here should be: 'cail2018_big.json'
target_valid_file_path='../data/data_valid_checked2.json' #data_valid_checked_tobedeleted
construct_validation_set(valid_file_path,training_file_path,target_valid_file_path)