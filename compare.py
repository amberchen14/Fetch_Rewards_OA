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
    1. Removes punctuations. For example, "don't" ==> "dont"
    2. Lower the capital.
    3. Split the words with space.
    For example,
    (ex. "I don't like cake." ==> ["i", "dont", "like", "cake"] 
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
    For example, text1=["I", "do", "not", "like", "dog"], text2=["I", "dont", "like", "dog"]
    result=[" I", "+ do", "+ not", "- dont", " like", " dog"]
    To calculate total_score:
    - If no sign before the word: +1
    - Two signs are between the words with space: + minimum words. For example, ["+ do", "+not", "-dont"] has two signs 
    between "I" and "like". sign + has two words and sign - only has one word, then min(2, 1)=1
    - Only one sign between the words with space: the number of the word with the sign. 
    To calculate string_similarity:
    - If no sign before the word: +1
    - Two signs are between the words with space: concats the words with the same sign and call difflib's SequenceMatcher function.
      For example, ["+ do", "+not", "-dont"] has two signs between "I" and "like". 
      SequenceMatcher(lambda x: x == " ", "do not", "dont").ratio()=0.8
    - If only one sign before the word: + 0
    The output is 3.8/4= 0.95 when comparing these texts.
    '''
    d = Differ() 
    total_score, similarity = 0, 0
    #Calculate the difference between the two texts
    result= list(d.compare(text1, text2))    
    plus, minus,= '', ''
    plus_num, minus_num = 0, 0
    for pos, r in enumerate(result):
        #print("r ", r[0])
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
            
        if r[0]==" " or pos ==len(result)-1: # No sign before the word. 
            similarity+=1
            total_score +=1
            if len(plus)==0 and len(minus)==0:
                continue
            else:     
                print(plus, minus)
                score=SequenceMatcher(lambda  x: x == " ", plus, minus).ratio()
                if plus_num>0 and minus_num>0: # '+' and '-' both show between the words with space. 
                    similarity+=score
                    total_score+=min(plus_num, minus_num)
                else:
                    similarity+=score
                    total_score+=max(plus_num, minus_num)
            plus, minus='', ''
            plus_num, minus_num = 0, 0
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
sample1="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
sample2="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
#sample2="We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
result=dict()
result['Sample1']=sample1
result['Sample2']=sample2
calculate_score(result)



