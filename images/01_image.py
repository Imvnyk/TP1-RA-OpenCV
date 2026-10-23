import cv2 

image = cv2.imread("images/machine.jpg") 
print("Type :", type(image)) 
print("Dimensions :", image.shape)

cv2.imshow("Machine", image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()