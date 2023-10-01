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

    scene = cv2.imread('../Images/school.jpg')

    cv2.imshow("Scene", scene)
    cv2.setMouseCallback('Scene', drawfunction)

    while True :
        if point_start is not None and point_end is not None:
            break
        cv2.waitKey(20)

    print('point_start =' + str(point_start))
    print('point_end =' + str(point_end))

    template = scene [point_start[1] : point_end[1],point_start[0] : point_end[0]]

    cv2.imshow('Template', template)
    cv2.waitKey(2)

    result = cv2.matchTemplate (scene, template, cv2.TM_CCOEFF_NORMED)

    _, value_max, _, max_loc = cv2.minMaxLoc(result)
    print(value_max)
    print(max_loc)

    h,w,_ = template.shape
    cv2.rectangle(scene, (max_loc[0], max_loc[1]),(max_loc[0]+w, max_loc[1]+h), (0 , 255 , 0),4)
    cv2.imshow('Search', scene)
    cv2.waitKey(0)
    exit(0)

if __name__ == "__main__":
    main()
