# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:02:14 2019

@author: qiuhao.zeng
"""
def main():
    filepath = "H:\Algo\greedy\jobs.txt"
    time = 0
    count = 0
    weiCompTime = 0
    jobList = []
    with open(filepath,'r') as f:
        for line in f:
#            import ipdb
#            ipdb.set_trace()
            if line =='\n':
                continue
            if count == 0:
                num = int(line)
            else:
                temp = list(line.strip('\n').split(','))[0].split()
                temp = list(map(int,temp))
                jobList.append([temp[0]/temp[1],temp[0],temp[1]]) #temp[0]-temp[1]
            count+=1
                
    jobList.sort(reverse=True)
    for i in range(num):
        time+=jobList[0][2]
        weiCompTime += (jobList[0][1])*time
        del(jobList[0])
    print(weiCompTime)
        
if __name__ == "__main__":
    main()