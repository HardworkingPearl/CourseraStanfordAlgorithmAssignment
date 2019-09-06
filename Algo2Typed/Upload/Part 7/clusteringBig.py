# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:49:50 2019

@author: 曾秋皓
"""

def n_spacing(x, n, _x, bits):
    '''
    search all num using a generator
    x: input  (list of int)
    _x: the positions of bits have already been changed
    n: how many changes left
    bits: total num of bits of input
    '''
    if n == 0:
        yield x
    else:
        for i in range(bits):
            x_copy = x.copy()
            if i not in _x:
                x_copy[i] = 1 - x[i]    
            _x_copy = _x.copy()
            _x_copy.append(i)
            yield from n_spacing(x_copy, n-1, _x_copy, bits )
    
    

def main():
    count = 0
    
    count_bit = {}
    bit_count = {}
    
    rank = {}
    parent = {}
    label = {}
    
    ############## read data ####################
    filepath = "D:\File\Algo2\Part 7-clustering\clustering_big.txt"
    with open(filepath,'r') as f:
        for line in f:
            if line =='\n':
                continue
            if count == 0:
                
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                total = temp[0]
                bits = temp[1]
                count+=1
            elif count != 0:
                
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                rank[count] = 0
                parent[count] = count
                label[count] = True
                if ''.join(str(x) for x in temp) in bit_count:
                    bit_count[''.join(str(x) for x in temp)].append(count)
                else:
                    bit_count[''.join(str(x) for x in temp)] = [count]
                count_bit[count] = temp
                count += 1

    
    # because the spacing are intergers,
    # merge them from 0 to an integer we need
    
    ############## K_Clusterings ####################
    k_cluster = UnionFind(parent, rank, label)          
    
    n = 0
    while n <3:
        for count in range(1,total+1,1):
            print(count, " - " , n)
            for num in n_spacing(count_bit[count], n, [], bits):
                x = count
                string_y = ''.join(str(x) for x in num)
                if string_y in bit_count:
                    y_group = bit_count[string_y] # list
                    for y in y_group:
                        s1 = k_cluster.find(x)
                        s2 = k_cluster.find(y)
                        if s1 != s2: 
                            # in this case, they belong to different 
                            # cluster. Then merge them
                            k_cluster.union(x, y)
        n+=1
    print("The number of clusters would be: " ,len(k_cluster.label))
                
            
class UnionFind():
    def __init__(self, parent, rank, label):
        self.parent = parent
        self.rank = rank
        self.label = label
        
    def find(self, x):
        '''
        Find the root
        
        '''
        while x is not self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        
        s1 = self.find(x)
        s2 = self.find(y)
        
        if self.rank[s1] > self.rank[s2]:
            self.parent[s2] = s1
            self.label.pop(s2, None)
        elif self.rank[s1] < self.rank[s2]:
            self.parent[s1] = s2
            self.label.pop(s1, None)
        else:
            self.parent[s2] = s1
            self.rank[s1] += 1
            self.label.pop(s2, None)
                
        
        
        
    
if __name__ == "__main__":  
    main()