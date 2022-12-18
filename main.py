import cv2 as cv

# Obraz

img = cv.imread('C:/Users/ahkha/OneDrive/Obrazy/dev/Photos/ludzie_2.jpg')

cv.imshow('Grupa', img)

# Rozpoznanie twarzy z użyciem Haar Cascades

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Grupa', gray)

haar_cascade = cv.CascadeClassifier('haar_fullbody.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Rozpoznane twarze w Grupa', img)

cv.waitKey(0)
