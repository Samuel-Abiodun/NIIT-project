import cv2
img = cv2.imread("C:\\Users\\udanb\\Pictures\\iphone\\101APPLE\\bart.jpg")
h, w = img.shape[:2]
new_h, new_w = int(1000 / 2), int(1000 / 2)
resizeImg = cv2.resize(img, (new_w, new_h))
cv2.imshow('Original', img)
cv2.imshow('Resizing', resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
