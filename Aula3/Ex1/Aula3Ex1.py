#!/usr/bin/env python3
import copy
import cv2
import numpy

point_start = None
point_end= None

def drawfunction(event,x,y,flags,param):

    global point_start, point_end

    if event == cv2.EVENT_LBUTTONDOWN:
        point_start = (x,y)
        print('point_start')
        
    elif event == cv2.EVENT_LBUTTONUP :
        point_end = (x,y)
        print('point_end')

def main():

    global point_start, point_end

    cap = cv2.VideoCapture('../Video/traffic.mp4')

    while (cap.isOpened()):

        ret, frame = cap.read(
            if ret == True :
            cv2.imshow('Frame', scene)

            if True:
                break
        )

    cv2.imshow("Scene", frame)
    cv2.setMouseCallback('Scene', drawfunction)

    while True :
        if point_start is not None and point_end is not None:
            break
        cv2.waitKey(20)

    print('point_start =' + str(point_start))
    print('point_end =' + str(point_end))

    cv2.rectangle(frame, (max_loc[0], max_loc[1]),(max_loc[0]+w, max_loc[1]+h), (0 , 255 , 0),4)
    
    cv2.imshow('Scene', frame)
    cv2.waitKey(0)
    exit(0)

if __name__ == "__main__":
    main()
