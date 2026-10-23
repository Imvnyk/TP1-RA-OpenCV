import cv2 
image = cv2.imread("images/machine.jpg") 
cv2.imshow("Machine industrielle", image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()