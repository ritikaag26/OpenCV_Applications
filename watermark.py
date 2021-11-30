import numpy as np
import cv2

image= cv2.imread('baby.jpeg')
#print(image.shape)
print(image.shape[1])
print(image.shape[0])

watermark_image= cv2.imread('RitikaLogo.jpg')
print(watermark_image.shape)

pos=40
new_width=int(image.shape[1]*pos/100)
new_height= int(image.shape[0]*pos/100)

new_dim=(new_width,new_height)
resized_img= cv2.resize(image,new_dim,interpolation=cv2.INTER_AREA)
print(resized_img.shape)
cv2.imshow("Resized Image",resized_img)


watermark_scale= 40
wm_width = int(watermark_image.shape[1] * watermark_scale/100)
wm_height = int(watermark_image.shape[0] * watermark_scale/100)
wm_dim = (wm_width, wm_height)
resized_wm = cv2.resize(watermark_image, wm_dim, interpolation=cv2.INTER_AREA)

print(resized_wm.shape)

cv2.imshow("Resized Watermark",resized_wm)

cv2.waitKey(0)

# Define the position of the logo according to the new dimensions of the resized input image

h_img, w_img, _ = resized_img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

roi = resized_img[top_y:bottom_y, left_x:right_x]

# Superimpose the resized watermark onto the ROI using cv2.addWeighted()
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)

resized_img[top_y:bottom_y, left_x:right_x] = result

filename = 'watermarked_img_baby.jpg'
cv2.imwrite(filename, resized_img)