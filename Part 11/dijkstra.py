# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:27:26 2019

@author: qiuhao.zeng
"""
import sys
import heapq
def main():
    filepath = "H:\Algo\Part 11\\_dijkstraData.txt"

    global n
    n = 0

    edges = {} 
    edges_len = {}
    V_X_heap = []
    V_X_vertice = []
    vertice = 0
    import ipdb
    ipdb.set_trace()
    with open(filepath,'r') as f:
        for line in f:
            count = 0
            for x in line.split():
                count += 1

                if count == 1:
                    vertice = int(x)
                    edges[vertice] = []
#                    if vertice != 1:
                    if vertice not in V_X_vertice:
                        V_X_vertice.append(vertice)
                        heapq.heappush(V_X_heap, (sys.maxsize,vertice))

#                    V_X_vertice.append
                else:
                    temp = list(map(int,x.split(',')))
                    edges[vertice].append(temp[0])
                    edges_len[(vertice,temp[0])]=temp[1]
#                    if vertice == 1: 
#                        V_X_vertice.append(temp[0])
#                        heapq.heappush(V_X_heap, (temp[1],temp[0]))
#                    else:
                    if temp[0] not in V_X_vertice:
                        # intialize
                        V_X_vertice.append(temp[0])
                        heapq.heappush(V_X_heap, (sys.maxsize,temp[0]))
                        
#                        edges[vertice] = 
                    
    total_num = len(V_X_vertice)
    a = dijkstra(V_X_heap,edges,edges_len,V_X_vertice)
    b=a.main_Loop(total_num)
    return b
    
#            temp = list(line.strip('\n').split(','))[0].split()
#            temp = list(map(int,temp))
#            if len(temp) != 0:
#                print('')
                    
class dijkstra(object):
    def __init__(self, _heap, _edges, _edges_len, _V_X_vertice):
        self.X = [] # vertices processed so far
        self.A = {} # computed shortest path distances
        self.V_X_heap = _heap
        self.edges = _edges
        self.edges_len = _edges_len
        self.V_X_vertice = _V_X_vertice
        
    def main_Loop(self, Tnum):
        import ipdb
        ipdb.set_trace()
        while len(self.X) != Tnum:
            min_item = self.V_X_heap.heappop()
            if self.X == []:       # intialize to deal with the node 1
                self.X.append[1]
                self.A[1] = 0
                self.X.append(min_item[1])
                self.A[min_item[1]] = min_item[0]
            else:
                self.X.append(min_item[1])
                self.A[min_item[1]] = min_item[0]
        return self.A
                
    def heap_update(self,w):
        for v in self.edges[w]:
            if v in self.V_X_heap:
                new_A = self.A[w] + self.edges_len[(w,v)]
                if new_A < self.A[v]:
                    self.heap_del_insert(v,new_A)
                 
                
    def heap_del_insert(self, delete_item, value):
        for idx in range(len(self.V_X_heap)):
            if self.V_X_heap[idx][1] == delete_item:
                self.V_X_heap[idx] = (value,delete_item)
                heapq.heapify(self.V_X_heap)
                break
                 
        
if __name__ == "__main__":
    b = main()
