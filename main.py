import cv2
from utils import get_limits
from PIL import Image

yellow = [0, 255, 255] # BGR format
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(yellow)
    
    masks = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    masks_ = Image.fromarray(masks)

    bbox = masks_.getbbox()
    
    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()

