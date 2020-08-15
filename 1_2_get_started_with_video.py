import numpy as np
import cv2 as cv

# cap = cv.VideoCapture(0)
cap = cv.VideoCapture('data/vtest.avi')
# cap = cv.VideoCapture('rtsp://192.168.10.20:8080/video/h264')

writer = None

while cap.isOpened():    
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # frame = cv.flip(frame, 0)
    # write the flipped frame

    frame = cv.line(frame, (0,0), (255,255), (147, 96, 44), 10) # 44, 96, 147
    frame = cv.arrowedLine(frame, (0,255), (255,255), (255, 0, 0), 10)
    frame = cv.rectangle(frame, (384, 0), (510, 128), (0, 0, 255), 10)
    frame = cv.circle(frame, (447, 63), 63, (0, 255, 0), -1)
       
    font = cv.FONT_HERSHEY_SIMPLEX
    frame = cv.putText(frame, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv.LINE_AA)
    frame = cv.ellipse(frame,(256,256),(100,50),0,0,180,(0,255,0),-1)
    
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    frame = cv.polylines(frame,[pts],True,(0,255,255))
    
    if writer is None:
          # initialize our video writer
        fourcc = cv.VideoWriter_fourcc(*"MJPG")
        writer = cv.VideoWriter('output.avi', fourcc, 30,
              (frame.shape[1], frame.shape[0]), True)

    # write the output frame to disk
    writer.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break
# Release everything if job is finished
cap.release()
writer.release()
cv.destroyAllWindows()

