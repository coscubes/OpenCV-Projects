import cv2
import numpy as np

cap = cv2.VideoCapture(0)
mk1 = [255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
mk2 = [255, 0, 0, 255, 0, 255, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255]
mk3 = [255, 0, 0, 255, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255]
mk4 = [255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 255]
mk5 = [255, 0, 0, 255, 0, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 255]
mk6 = [255, 0, 0, 255, 0, 255, 255, 0, 0, 0, 255, 0, 0, 0, 0, 255]
mk7 = [255, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255]
mk8 = [255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 255]
mk9 = [255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 0, 0, 0, 255]
mk10 = [255, 0, 0, 255, 0, 255, 255, 0, 0, 255, 0, 0, 0, 0, 0, 255]

while(1):
    _, img = cap.read()
    
    img = cv2.line(img,(150,167),(500,167),(255,0,0),1)
    img = cv2.line(img,(150,255),(500,255),(255,0,0),1)
    img = cv2.line(img,(150,342),(500,342),(255,0,0),1)
    img = cv2.line(img,(237,80),(237,430),(255,0,0),1)
    img = cv2.line(img,(325,80),(325,430),(255,0,0),1)
    img = cv2.line(img,(412,80),(412,430),(255,0,0),1)
    img = cv2.rectangle(img,(150,80),(500,430),(255,0,0),1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'MARKER DETECTION',(180,460), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    marker = img[83:427,153:497]
    
    temp = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(temp,(5,5),0)
    ret3,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    a = [thresh1[38,41],thresh1[128,40],thresh1[215,41],thresh1[302,41],
        thresh1[40,131],thresh1[133,132],thresh1[219,128],thresh1[302,129],
        thresh1[41,218],thresh1[125,215],thresh1[213,219],thresh1[301,216],
        thresh1[39,300],thresh1[129,300],thresh1[211,300],thresh1[300,300],]
    
    if a == mk1:
        cv2.putText(img,'MARKER 1',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk2:
        cv2.putText(img,'MARKER 2',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk3:
        cv2.putText(img,'MARKER 3',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk4:
        cv2.putText(img,'MARKER 4',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk5:
        cv2.putText(img,'MARKER 5',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk6:
        cv2.putText(img,'MARKER 6',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk7:
        cv2.putText(img,'MARKER 7',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk8:
        cv2.putText(img,'MARKER 8',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk9:
        cv2.putText(img,'MARKER 9',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif a == mk10:
        cv2.putText(img,'MARKER 10',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    else:
        cv2.putText(img,'NO MARKER',(180,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    cv2.imshow('test1', img)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
        
cv2.destroyAllWindows()
