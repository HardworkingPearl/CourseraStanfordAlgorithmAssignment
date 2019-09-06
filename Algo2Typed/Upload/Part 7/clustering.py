# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:49:50 2019

@author: 曾秋皓
"""
import heapq

def main():
    count = 0
    
    heap = []
    rank = {}
    parent = {}
    label = {}
    
    
    filepath = "D:\File\Algo2\Part 7-clustering\clustering.txt"
    with open(filepath,'r') as f:
        for line in f:
            if line =='\n':
                continue
            if count == 0:
                count+=1
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
            elif count != 0:
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                if temp[1] not in rank:
                    rank[temp[1]] = 0
                    parent[temp[1]] = temp[1]
                    label[temp[1]] = True
                    
                if temp[0] not in rank:
                    rank[temp[0]] = 0
                    parent[temp[0]] = temp[0]
                    label[temp[0]] = True
                heapq.heappush(heap,[temp[2], temp[0], temp[1]])
                
    k_cluster = UnionFind(parent, rank, label)          
    while True:
        cost, x, y = heapq.heappop(heap)
        if len(k_cluster.label) ==4 and k_cluster.find(x)!=k_cluster.find(y):
            # in some cases, the next x and y may be in the same group. 
            # we need them in separated group/clusters
            break
        s1 = k_cluster.find(x)
        s2 = k_cluster.find(y)
        if s1 != s2: 
            # in this case, they belong to different 
            # cluster. Then merge them
            k_cluster.union(x, y)
        
#    max_space, _, _ = heapq.heappop(heap)
    print("The maximun spacing would be: " + str(cost))
#                
            
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