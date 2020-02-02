import cv2
import pytesseract
import numpy as np



def get_code(path):
    data = []
    originalImage = cv2.imread(path)

    slicedImage = originalImage[140:400, 800:1500]
    gray = cv2.cvtColor(slicedImage, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((2, 1), np.uint8)
    img = cv2.cvtColor(slicedImage, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 5)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("image",img)

    res = pytesseract.image_to_string(img)
    data.append(res)
    return data




res=get_code('ocr.jpg')
print(" L'erreur:", res[0])
cv2.waitKey(0)
cv2.destroyAllWindows()