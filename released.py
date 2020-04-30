import numpy as np
import cv2

def mouse_event(event,x,y,flags,param):
    global rect_list
    global img
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.destroyWindow("widget")
        for x1,y1,w1,h1 in rect_list:
            if x >= x1 and x <= x1+w1 and y >= y1 and y <= y1+h1:   # 找到包含点击位置的矩形
                cropped = img[y1:y1+h1,x1:x1+w1]
                cv2.imshow("widget",cropped)
                break



cv2.namedWindow("rect",0)
cv2.resizeWindow("rect", 600, 1200)
cv2.setMouseCallback('rect',mouse_event)


img = cv2.imread("pictures/pic7.jpg")                       # 读取图片
img_height, img_width = img.shape[:2]
img_size = img_width * img_height

canny = cv2.Canny(img,100,150)

kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
for _ in range(3):
    canny = cv2.dilate(canny,kernal)
cv2.imwrite("Canny.jpg",canny)
    
_,contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
rect_list = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w * h > img_size * 0.16:                                     # 排除面积过大的矩形框
        continue
    rect_list.append((x,y,w,h))
    rect_list.sort(key=lambda rect:rect[2]*rect[3],reverse=False)    # 将矩形框按面积大小排序
cv2.imshow("rect",img)
cv2.waitKey(0)