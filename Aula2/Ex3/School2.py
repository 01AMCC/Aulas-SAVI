#!/usr/bin/env python3
import copy
import cv2
import numpy


point_start = None
point_end = None
template = None
scene = None

def drawfunction(event, x, y, flags, param):
    global point_start, point_end, template, scene

    if event == cv2.EVENT_LBUTTONDOWN:
        point_start = (x, y)
        
    elif event == cv2.EVENT_LBUTTONUP:
        point_end = (x, y)

        # Recorte a região da imagem de cena que representa o template
        template = scene[point_start[1]:point_end[1], point_start[0]:point_end[0]]

        # Exiba a região do template na janela 'template' se o template não for None
        if template is not None:
            cv2.imshow('template', template)
            cv2.imwrite('Template.png', template)

def main():
    global scene, template  # Defina scene e template como variáveis globais

    scene = cv2.imread('../Images/school.jpg')

    cv2.namedWindow('scene')
    cv2.setMouseCallback('scene', drawfunction)

    while True:
        cv2.imshow("scene", scene)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # 27 é o código ASCII da tecla Esc
            break

    cv2.destroyAllWindows()

    # Após encerrar o loop de visualização, você pode continuar com a correspondência de padrões
    if template is not None:
        result = cv2.matchTemplate(scene, template, cv2.TM_CCOEFF_NORMED)
    
        _, value_max, _, max_loc = cv2.minMaxLoc(result)
        print(value_max)
        print(max_loc)

        h, w, _ = template.shape
        cv2.rectangle(scene, (max_loc[0], max_loc[1]), (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 4)
        cv2.imshow("scene", scene)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
