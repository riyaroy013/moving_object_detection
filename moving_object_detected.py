import cv2
import imutils
import time

cam=cv2.VideoCapture(0)
time.sleep(1) #1 second delay

firstframe=None #initializing there is no object
area = 500  #threshold

while True:
    _,img=cam.read()   #read frame from the camera
    text="Normal"  #initialize the text as Normal
    img=imutils.resize(img,width=500)

    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianimg=cv2.GaussianBlur(grayimg,(21,21),0)

    if firstframe is None:
        firstframe=gaussianimg
        continue
    imgdiff=cv2.absdiff(firstframe,gaussianimg)#subtracting current frame from firstframe

    thresimg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]

    thresimg=cv2.dilate(thresimg,None,iterations=2) #remove holes

    #contour=making boundary of object
    #syntax:
    #dst=cv2.findContours(srcimagecopy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cv2.findContours(thresimg.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #covering up the whole moving object as single area
    cnts=imutils.grab_contours (cnts)
    for c in cnts:
            if cv2.contourArea (c) < area:
                    continue
            (x,y,w,h)=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)#2=thickness of rect,(x,y)=start point of rect,(x+w,y+h)=end point
            #(0,255,0)=green colour
            text="Moving Object Detected"
    print(text)

    
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    #put text syntax: cv2.putText(source_image,text,position,font,fontSize,color,thickness)
    cv2.imshow("camerafeed",img)
    key=cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
