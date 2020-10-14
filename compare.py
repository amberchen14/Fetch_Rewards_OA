#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:18:06 2020

@author: amberchen
"""

from collections import Counter
from difflib import Differ, SequenceMatcher
 


def calculate_score(result):
    """
    This function reads input data and calculates the similarity ratio
    """
    sample1=result['Sample1']
    sample2=result['Sample2']
    string1=paragraph_to_list(sample1)
    string2=paragraph_to_list(sample2)
    
    return round( strings_similarity(string1, string2), 2)
    #method_dict=strings_count_compare(string1, string2)/ max(len(string1), len(string2))
    #return round(0.5*(method_difflab+method_dict), 2)

def paragraph_to_list(para):
    '''
    This function removes punctuations and split paragraph to list (ex. "I like cake." ==> ["I", "like", "cake"] 
    Ignore all punctuations.
    For example, "don't" ==> "dont"
    '''
    new_string=''
    pos = 0
    while pos <len(para):
        if para[pos].isalpha():
            new_string+=para[pos].lower()
        #elif para[pos]=='.':
        #    s_out.append(new_string)
        #    l_out.append(new_string.split(" "))
        #    new_string=''
        #    pos+=1
        #elif para[pos]=="'":
        #    new_string+=" "
        elif para[pos]==" ":
            new_string+=para[pos]
        pos+=1
    out=new_string.split(" ")
    return out   
    #return [s_out, l_out]


def strings_similarity(text1, text2):
    '''
    This function uses library difflib to compare word similarity in list.
    d.compare shows the different words in lists. 
    If text1 has unique word, show + before the word; 
    if text2 has unique word, show - before the word;
    otherwise, no sign before the word.
    This function concats each texts' unique words to calculate string similarity. 
    Two scores will calculate: similairty_score and total_score (number of words)
    Since numbers of words are different between two texts, 
    this function concats the words if facing same sign.
    For example, text1=["I", "do", "not", "like", "dog"], text2=["I", "don", "t", "like", "dog"]
    result=["I", "+ do", "+not", "-don", "- t", "like", "dog"]
    This function concats "+ do", "+not" => "do not"and "don", "t"=> "don t" to calculate score, 
    The number of words here is min(len(['do', not]), len('dont')) = 1 , and total_score = 4 ("I"=1, "like"=1, "dog"=1) 
    The similarity_score is 0.72 at "do not" and "don t", and the total score similarity is 3.72 ("I"=1, "like"=1, "dog"=1)
    The ratio = 3.72/4=0.93
    '''
    d = Differ() 
    total_score, similarity = 0, 0
    #Calculate the difference between the two texts
    result= list(d.compare(text1, text2))    
    plus, minus,= '', ''
    plus_num, minus_num = 0, 0
    for r in result:
        #print("r ", r[0])
        if r[0]==" ":
            similarity+=1
            total_score +=1
            if len(plus)==0 and len(minus)==0:
                continue
            else:
                score=SequenceMatcher(lambda x: x == " ", plus, minus).ratio()
                if plus_num>0 and minus_num>0:
                    similarity+=score/min(plus_num, minus_num)
                    total_score+=min(plus_num, minus_num)
                else:
                    similarity+=score/max(plus_num, minus_num)
                    total_score+=max(plus_num, minus_num)
            plus, minus='', ''
            plus_num, minus_num = 0, 0
            continue
        if r[0]=='+':
            if len(plus)!=0:
                plus+=" "
            plus+=r[2:]
            plus_num+=1
        elif r[0]=="-":
            if len(minus)!=0:
                minus+=" "      
            minus+=r[2:]
            minus_num+=1 
    return similarity/total_score

def strings_count_compare(string1, string2):
    """
    This function uses Counter to calculate similarity. 
    The performance is not as good as strings_similarity.
    """
    s1 = Counter(string1)
    s2 = Counter(string2)
    out = 0
    for word in s1:
        if word in s2:
           out+=min(s1[word], s2[word])
    return out
#sample1="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
#sample2="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
#sample2="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
#result=dict()
#result['Sample1']=sample1
#result['Sample2']=sample2
#calculate_score(result)



