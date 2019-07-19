# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:35:44 2019

@author: qiuhao.zeng
"""

filepath = "D:\File\Algo\Part 16\sum2.txt"
    
_dict = {}
_dict_2 ={}
count = 0
max_num = 0
with open(filepath,'r') as f:
    for line in f:
        if line =='\n':
            continue
            
        num = int(line)+5000
        if num in _dict_2:
            _dict_2[num]+=1
        else:
            _dict_2[num]=1
        if num//20000 in _dict:
            _dict[num//20000].append(num)
            if len(_dict[num//20000])>max_num:
                max_num = len(_dict[num//20000])

        else:
#            import ipdb
#            ipdb.set_trace()
            _dict[num//20000]= [ num]
print(max_num)
_dict_4 = {}
for t in range(0,20001):
    _dict_4[t] = 0
    found = 0
pair_dict = {}
for i in _dict:
    if i >= 0:
        for j in range(-i-1,-i+1):
            if j in _dict:
                for _i in _dict[i]:
                    for _j in _dict[j]:
                        if _i+_j >=0 and _i+_j <=20000:        
                            if _dict_4[_i+_j]==0:
                                if _i != _j:
#                                    if (_i,_j) not in pair_dict and (_j,_i) not in pair_dict:
                                    pair_dict[(_i,_j)] = 1
                                    found =1
                                    _dict_4[_i+_j] = 1
                                    count +=1
                                    print(str(_i+_j-10000)+':'+str(_i-5000)+'+'+str(_j-5000))
                                else:
                                    if _dict_2[_i]>1:
                                        _dict_4[_i+_j] = 1
                                        found =1
                                        count +=1
                                        print(str(_i+_j-10000)+':'+str(_i-5000)+'+'+str(_j-5000))
#                        
#                        break
print(count)
#import ipdb
#ipdb.set_trace()
#print("load complete")
#count = 0  
#for i in range(0,5):
#    print(i)
#    for j in _dict:
#        if i-j in _dict:
#            count +=1
##            import ipdb
##            ipdb.set_trace()
#            print(count)
#            break
#print(count)