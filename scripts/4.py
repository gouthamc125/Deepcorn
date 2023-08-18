import cv2


# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\17.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find bounding box
x,y,w,h = cv2.boundingRect(thresh)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

cv2.imshow("thresh", thresh)
cv2.imshow("image", image)
cv2.waitKey(0)

kernels = len(thresh)

print("No of Kernels : ", kernels)