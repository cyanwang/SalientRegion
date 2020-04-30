import numpy as np
import cv2
import math
import sys
m=8
n=8
matrix=[
 [-1 ,-1 ,-1 ,-1, -1 ,-1, -1 ,-1],
 [-1, -1, -1 ,-1 ,-1 , 0 ,-1 ,-1],
 [-1 ,-1, -1,  3 , 2 , 2 ,-1 ,-1],
 [-1 ,-1 ,-1  ,2 , 1 , 0 , 1 ,-1],
 [-1 , 4 , 4 , 6 , 0 , 0 ,-1 ,-1],
 [-1 , 0 , 5 , 2 ,-1 ,-1 ,-1 ,-1],
 [-1 ,-1 , 3 , 1 , 0 ,-1 ,-1 ,-1],
 [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1]]
def maxSubsequence(matrix):
    if len(matrix)==0:
        return 0;
    max=-1;
    maxSub=np.zeros(len(matrix))
    maxSub[0]=matrix[0]
    max_bc=-1
    max_ec=-1
    now_bc=0
    now_ec=0
    for i in range(1,len(matrix)):
        maxSub[i]=maxSub[i-1] + matrix[i] if maxSub[i-1] > 0 else matrix[i]
        #/*坐标获取
        if maxSub[i]>0 and maxSub[i-1]<0:
             now_bc=i
        #*/坐标获取
        if max<maxSub[i]:
            max=maxSub[i]
            now_ec=i
            max_bc=now_bc
            max_ec=now_ec
    return max,max_bc,max_ec
def maxSub():
    #记录坐标
    bR=-1
    bC=-1
    eR=-1
    eC=-1
    #计算total[i][j]
    total = np.zeros([m,n],dtype=int)
    total = matrix #
    for i in range(0,len(total[0])):
        for j in range(0,len(total)):
            total[i][j] += total[i-1][j]
    maximum=0
    print(len(total))
    print(len(total[0]))
    for i in range(0,len(total)):
        for j in range(i,len(total)):
            result=np.zeros(len(total[0]))
            for f in range(0,len(total[0])):
                if i==0:
                    result[f]=total[j][f]
                else:
                    result[f]=total[j][f]-total[i-1][f]
            maximal,bc,ec=maxSubsequence(result)#找到最大的矩阵和
            print(result)
            if maximal>maximum:
                bR=i
                eR=j
                bC=bc
                eC=ec
                maximum = maximal

    print(maximum)
    print(bR)
    print(bC)
    print(eR)
    print(eC)


maxSub()


