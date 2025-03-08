import imutils
import cv2
img=cv2.imread("python.jpg")
resize=imutils.resize(img,width=50)
cv2.imwrite("resized_image.jpg",resize)#resize and save

#smoothening(gaussian blur)
#syntax:dst=cv2.GaussianBlur(src,(kernel),borderType)
gaussianBlur=cv2.GaussianBlur(img,(25,25),0)
cv2.imwrite("gaussianblur.jpg",gaussianBlur)

