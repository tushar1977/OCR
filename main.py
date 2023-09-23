import cv2
import pytesseract


#defining global variables
pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('2.png')

def pre_process(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
def detecting_words(img_new):

    himg, wimg, _ = img_new.shape
    boxes = pytesseract.image_to_boxes(img_new)

    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img_new, (x, himg - y), (w, himg - h), (0, 0, 255), 1)
        cv2.putText(img_new, b[0], (x, himg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))


img = pre_process(img)
detecting_words(img)


cv2.imshow('Result', img)
cv2.waitKey(0)