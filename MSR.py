import numpy as np
import cv2
import math

#定义分布矩阵大小
size=20

def getMatrix(ImgPath):

	img=cv2.imread(ImgPath)
	h, w = img.shape[:2]
	m=math.ceil(h/size)
	n=math.ceil(w/size) 
	matrix = np.zeros([m,n],dtype=int)
	print(m)
	print(n)


	#分布矩阵的求取
	surf = cv2.xfeatures2d.SURF_create(500) 
	key_query,desc_query = surf.detectAndCompute(img,None)
	img=cv2.drawKeypoints(img,key_query,img)
	cv2.imwrite("elmsurf.jpg",img)
	for k in key_query:
		(x,y)=k.pt
		matrix[math.ceil(y/size)-1][math.ceil(x/size)-1]+=1
	print("分布矩阵：")
	print(matrix)

	#适应矩阵matrix1求取
	#1计算K=k*average
	average =np.mean(matrix)#均值  
	sum=len(key_query) 
	k = math.sqrt(np.sum(pow(matrix/sum-1/(m*n),2)))
	K=math.ceil(k*average)
	# print("原始K值:")
	# print(k*average)
	# K=round(k*average) 
	# print("四舍五入后的K:")
	# print(K)
	matrix1=matrix-K
	print("适应矩阵：")
	print(matrix1)
	return matrix1,img


#求解matrix1最大子矩阵和
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

def maxSub(matrix):     
    matrix1=matrix.copy()
    #记录坐标
    bR=-1
    bC=-1
    eR=-1
    eC=-1
    #计算total[i][j]
 
    total = np.zeros([len(matrix),len(matrix[0])],dtype=int)
    total = matrix #注意这种赋值 maxtrix会随着total一起变
    for i in range(1,len(total)):#9
        for j in range(0,len(total[0])):#12
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
            # print(result)
            if maximal>maximum:
                bR=i
                eR=j
                bC=bc
                eC=ec
                maximum = maximal
    print("选取的区域：")       
    print(matrix1[bR:eR+1,bC:eC+1])
    # print("列")  
    # print(bC)
    # print(eC)
    # print("行")  
    # print(bR)
    # print(eR)
    # print(maximum)
    return bR,bC,eR,eC,matrix1[bR:eR+1,bC:eC+1]

#把特征点标记到图片上
ImgPath="elm.png"
img=cv2.imread(ImgPath)
matrix_min,surfImg=getMatrix(ImgPath)
bR,bC,eR,eC,matrix_max=maxSub(matrix_min)
#获取OP图片
if len(matrix_max)!=0:
	imgSub=img[bR*20:(eR+1)*20,bC*20:(eC+1)*20]
	cv2.imwrite("elmOP.jpg",imgSub)

	#显示截取的区域
	print([bR*20,bC*20,(eR+1)*20,(eC+1)*20])
	cv2.rectangle(surfImg, (bR*20,bC*20),((eR+1)*20,(eC+1)*20), (0,255,0), 6)
	cv2.imshow("sub",imgSub)

	#img=cv2.drawKeypoints(img,key_query,img)
	cv2.waitKey(0)
else:
	print("找不到显著区域")