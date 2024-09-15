import cv2

img = cv2.imread('../Images/challenger.jpg')

cv2.imshow('Loaded Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
