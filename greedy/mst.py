# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:31:17 2019

@author: qiuhao.zeng
"""

import heapq
import random
def main():
    filepath = "H:\Algo\greedy\edges.txt"
    count = 0
    edges ={}
    vertice = {}
    with open(filepath,'r') as f:
        for line in f:
#            import ipdb
#            ipdb.set_trace()
            if line =='\n':
                continue
            if count == 0:
                count+=1
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                nVert = temp[0]
                mEdge = temp[1]
            else:
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                edges[str(temp[0])+','+str(temp[1])] = temp[2]
                edges[str(temp[1])+','+str(temp[0])] = temp[2]
                if temp[0] in vertice:
                    vertice[temp[0]].append(temp[1])
                else:
                    vertice[temp[0]] =  [temp[1]]
#                    X = [vertice[temp[1]]] = 0
                if temp[1] in vertice:
                    vertice[temp[1]].append(temp[0])
                else:
                    vertice[temp[1]] = [temp[0]]
    
    cost = 0
    heap = []
    X = {}
    while len(X)!= nVert:
        if heap == []:
            newVertice = random.choice(list(vertice.keys()))
            X[newVertice]=1
        else:
            
            choice = heapq.heappop(heap)
            newVertice = choice[1]
            cost += choice[0]
            X[newVertice] = 1
        for w in vertice[newVertice]:
            if w not in X:
                wInHeap = 0
                for item in heap:
                    if item[1] == w:
                        wInHeap = 1
                        if item[0] > edges[str(newVertice)+','+str(w)]:
                            heap.remove(item)
                            heap.append([edges[str(newVertice)+','+str(w)],w])
                            heapq.heapify(heap)
                            break
                if wInHeap == 0:
                    heapq.heappush(heap,[edges[str(newVertice)+','+str(w)],w])
    print(cost)
if __name__ == "__main__":
    main()