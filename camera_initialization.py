import cv2
vs=cv2.VideoCapture(0) #initialize camera

while True:
    _,img=vs.read()#reading the frame of camera
    cv2.imshow("VideoStream",img)

    key=cv2.waitKey(1) & 0xFF #record the key press
    if key==ord("q"):  #if the pressed key is q
        break
vs.release() #release the camera
cv2.destroyAllWindows()
#every opened output window will be closed
