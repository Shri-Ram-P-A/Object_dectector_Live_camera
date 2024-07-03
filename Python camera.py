import cv2
import winsound

cam = cv2.VideoCapture(0)
while True:
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    dif = cv2.absdiff(frame1,frame2)
    show = cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(show,(5,5),0)
    _,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
              continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(500,500)
        # winsound.PlaySound('Krishna flute bgm.mp3', 
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow('shri',frame1)
cam.release()
cv2.destroyAllWindows()