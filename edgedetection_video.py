import numpy as np
import cv2

# Turn on the primary webcam by using VideoCapture function and passed 0 to this function as I am using my primary webcam
video_cap= cv2.VideoCapture(0)
# Run through an infinite loop so as to keep the video feed live as per what the webcam reads.
while True:
    ret,image= video_cap.read()
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred_img= cv2.GaussianBlur(gray_image,(5,5),0)
    canny = cv2.Canny(blurred_img, 10, 70)
    sobelX= cv2.Sobel(gray_image, cv2.CV_64F, 1, 0)
    sobelY= cv2.Sobel(gray_image,cv2.CV_64F,0,1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        cv2.drawContours(image,[c],-1,(0,255,0),3)
    cv2.imshow("Frame",image)
    cv2.imshow('Video feed', mask)
    cv2.imshow("sobel combined",sobelCombined)
    # Enter key to exit out of the loop, where 13 is the key code for Enter button
    if cv2.waitKey(1) == 13:
        break
video_cap.release()
cv2.waitKey(0)
 


