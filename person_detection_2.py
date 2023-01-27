import cv2 as cv
import imutils



    # Obraz
img = cv.imread('static/ludzie.jpg')
img = imutils.resize(img, width=min(600, img.shape[1]))
#cv.imshow('Grupa', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray Grupa', gray)

    # calssifier haarcascade_fullbody.xml
haar_cascade = cv.CascadeClassifier('haar_fuulbody.xml')

    # Wykrycie osoby
body_rect = haar_cascade.detectMultiScale(
     gray, scaleFactor=1.09, minNeighbors=1)

print(f'Number of people found = {len(body_rect)}')

for (x, y, w, h) in body_rect:
      cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Rozpoznane osoby w Grupa', img)
cv.imwrite(('static/upload/'), img)

cv.waitKey(0)

cv.destroyAllWindows()

