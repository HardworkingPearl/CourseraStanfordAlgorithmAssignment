# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:25:31 2019

@author: 曾秋皓
"""

# -*- coding: utf-8 -*-
"""
SCC = nodes with the same "leader"
"""
def main():
    filepath = "H:\\Algo\\SCC\\_SCC.txt"
    graph = {}
    graph_rev = {}
    global n
    n = 0
    explored = {}
    with open(filepath,'r') as f:
        for line in f:
            temp = list(line.strip('\n').split(','))[0].split()
            temp = list(map(int,temp))
            if len(temp) != 0:
                explored[temp[0]] = 0
                explored[temp[1]] = 0
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
    


    # computer magical ordering of nodes
    scc = SCC(graph_rev,explored)
    scc.DFS_Loop()
    
    f_0 = scc.f 
    del scc
#    import ipdb
#    ipdb.set_trace()    
    del graph_rev
    graph_0 = {}
    explored_0 = {}
    for i in graph:
        graph_0[f_0[i]] = []
        explored_0[f_0[i]] = 0
        for j in graph[i]:
            graph_0[f_0[i]].append(f_0[j])
            explored_0[f_0[j]] = 0
    del graph
    scc = SCC(graph_0,explored_0)
    scc.DFS_Loop()
    leader_0 = scc.leader
    SCCs = []

    for i in leader_0:
        SCCs.append(leader_0[i])
    SCCs = sorted(SCCs,reverse=True)[:5]
    print(SCCs)
    return SCCs
    
class SCC(object):
    def __init__(self,graph,_explored):
        self.G = graph
        
        # in the leader dict, key is the leader. 
        # Content is the nodes belonging to this leader
        self.leader = {}
        self.f = {}
        self.explored = _explored
        self.t = 0
        self.s = None
        self.count = 0
        
        self.queue = [] 

    def DFS_Loop(self):
        for i in range(n,0,-1):
            if not self.explored[i]:
                self.s = i
                self.DFS(i)
            
    def DFS(self,i):   
        # loop
        while True:
            self.count += 1
            if self.count % 3000 == 0:
                print(self.count)
            

            # only execute in the first search trial
            if not self.explored[i]:
                self.explored[i] = 1
                self.queue.append(i)
                if self.s not in self.leader:
                    self.leader[self.s] = 1
                else:
                    self.leader[self.s]+=1

            all_explored = True
#            if i ==5:
#                import ipdb
#                ipdb.set_trace()
            # In the first case, it will explore all 
            if i in self.G:
                for j in self.G[i]:
                    if not self.explored[j]:
                        i = j
                        all_explored = False 
                    
            # in the other case, it will go back to find other direction 
            # if one node has not been explored yet need more loop to explore this node
#            import ipdb
#            ipdb.set_trace()
            if all_explored:
                
                self.queue.pop() # delete this one in the queue
                self.t+=1
                self.f[i]=self.t
                if self.queue == []:
                    break
                i = self.queue[-1]
            
            
                
if __name__ == "__main__":
     sccs = main()
     while len(sccs)!=5:
         sccs.append(0)
     print(sccs)