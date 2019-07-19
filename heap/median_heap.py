# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:47:55 2019

@author: qiuhao.zeng
"""
# trick: in low heap, all elements are minus
import heapq
def main():
    filepath = "H:\\Algo\\Part13\\median.txt"
    lowHeap = []
    highHeap = []
    count = 0
    midSum = 0
    with open(filepath,'r') as f:
        for line in f:
#            import ipdb
#            ipdb.set_trace()
            if line =='\n':
                continue
            count +=1


            num = int(line)
            if count ==1:
                first = num
                midSum += num
            elif count ==2:
                if first > num:
                    highHeap.append(first)
                    lowHeap.append(  -num)
                else:
                    highHeap.append(num)
                    lowHeap.append(-first)
                midSum += -lowHeap[0]
            else:
                if len(highHeap)>len(lowHeap): # add to low_heap
                    if num < - lowHeap[0]:
                        heapq.heappush(lowHeap,-num)
                    else:
                        if num < highHeap[0]:
                            heapq.heappush(lowHeap,-num)
                        else:
                            temp = heapq.heappop(highHeap)
                            heapq.heappush(highHeap, num)
                            heapq.heappush(lowHeap,-temp)
                    midSum += -lowHeap[0]
                    print(-lowHeap[0])
                    
                        
                else:
                    if num > highHeap[0]:
                        heapq.heappush(highHeap,num)
                    else:
                        if num > -lowHeap[0]:
                            heapq.heappush(highHeap,num)
                        else:
                            temp = -heapq.heappop(lowHeap)
                            heapq.heappush(lowHeap, -num)
                            heapq.heappush(highHeap,temp)
                    midSum += highHeap[0]
                    print(highHeap[0])
    print(midSum%10000)
                    
            
                

if __name__ == "__main__":
    main()