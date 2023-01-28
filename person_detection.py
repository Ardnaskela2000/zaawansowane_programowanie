import cv2 as cv
import imutils


def PersonDetection(img):
    # Obraz

    filename = img
    img = 'static/upload/' + filename

    img = cv.imread(img)
    #img = imutils.resize(img, width=600)

    # cv.imshow('Grupa', img)

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

    cv.imwrite(('static/upload/ludzie.jpg' + filename), img)

    cv.imshow('Rozpoznane osób ze zdjęcia', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


PersonDetection("static/ludzie.jpg")

PersonDetection("static/ludzie_2.jpg")

PersonDetection("static/ludzie_3.jpg")

PersonDetection("static/ludzie_5.jpg")
