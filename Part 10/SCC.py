# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:25:31 2019

@author: 曾秋皓
"""

# -*- coding: utf-8 -*-
"""
SCC = nodes with the same "leader"
"""


import sys
import threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)
def main():
    filepath = "D:\\File\\Algo\\Part 10\\_SCC.txt"
    graph = {}
    graph_rev = {}
    global n
    n = 0
    count_0 = 0
    with open(filepath,'r') as f:
        for line in f:
            temp = list(line.strip('\n').split(','))[0].split()
            temp = list(map(int,temp))
            if len(temp) != 0:
                count_0 +=1
                if temp[0] in graph:
                    graph[temp[0]].append(temp[1])
                else:
                    graph[temp[0]] = [temp[1]]
                if temp[1] in graph_rev:
                    graph_rev[temp[1]].append(temp[0])
                else:
                    graph_rev[temp[1]] = [temp[0]]
                if temp[0] >n:
                    n = temp[0]
                if temp[1]>n:
                    n = temp[1]
    
    import ipdb
    ipdb.set_trace()c
    print(count_0)
    # computer magical ordering of nodes
    scc = SCC(graph_rev)
    scc.DFS_Loop()
    
    f_0 = scc.f 
    del scc
#    import ipdb
#    ipdb.set_trace()    
    del graph_rev
    graph_0 = {}
    for i in graph:
        graph_0[f_0[i]] = []
        for j in graph[i]:
            graph_0[f_0[i]].append(f_0[j])
    del graph
    scc = SCC(graph_0)
    scc.DFS_Loop()
    leader_0 = scc.leader
    SCCs = []

    for i in leader_0:
        SCCs.append(len(leader_0[i]))
    SCCs = sorted(SCCs,reverse=True)[:5]
    print(SCCs)
    return 0
    
class SCC(object):
    def __init__(self,graph):
        self.G = graph
        
        # in the leader dict, key is the leader. 
        # Content is the nodes belonging to this leader
        self.leader = {} # changeable
        self.f = {}         # changeable
        self.explored = []# changeable
        self.t = 0# changeable
        self.s = None# changeable
        self.count = 0# changeable
        

    def DFS_Loop(self):
        for i in range(n,0,-1):
            if i not in self.explored:
                self.s = i
                self.DFS(i)
            
    def DFS(self,i):
        self.count += 1
        if self.count % 1000 == 0:
            print(self.count)
        self.explored.append(i)
        if self.s not in self.leader:
            self.leader[self.s] = [i]
        else:
            self.leader[self.s].append(i)
#        import ipdb
#        ipdb.set_trace()    
        try:
            if i in self.G:
                for j in self.G[i]:
                    if j not in self.explored:
                        self.DFS(j)
        except RecursionError:
            hhhh = 1
        self.t+=1
        self.f[i] = self.t
    
if __name__ == "__main__":
    thread = threading.Thread(target=main())
    thread.start()

    # sccs = main()
    # while len(sccs)!=5:
    #     sccs.append(0)
