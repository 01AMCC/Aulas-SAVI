import cv2 as cv
import numpy as np

img = cv.imread("lake.jpg") #dar upload da imagem 

altura, largura, canais = img.shape #obter as dimensões da imagem (altura, largura e nº de cores)

metade_esquerda = img[:, :largura // 2] #dividir a imagem em 2 (esq e drt)
metade_direita = img[:, largura // 2:]

cv.namedWindow("Sequência de Imagens", cv.WINDOW_NORMAL)  #criar uma sequência de imagens # WINDOW_NORMAL permite redimensionar a janela

fourcc = cv.VideoWriter_fourcc(*"MJPG") #criação do vídeo
saida_video = cv.VideoWriter("saida_video.avi", fourcc, 10.0, (largura, altura))

# ciclo for para variar o fator de aumento
for fator_aumento in np.arange(1.0, 0.0, -0.1):  # Varia de 1.0 a 0.0 em decrementos de 0.1
    # intensidade dos pixels da metade direita
    metade_direita_aumentada = (metade_direita * fator_aumento).astype(np.uint8)

    # agrupar as duas imagens 
    imagem_resultante = np.hstack((metade_esquerda, metade_direita_aumentada))

    # guardar o video
    saida_video.write(imagem_resultante)

    # Atualização do conteúdo da janela com a nova imagem
    cv.imshow("Sequência de Imagens", imagem_resultante)

    # sequencia da imagem 
    key = cv.waitKey(1500)

    # Se a tecla 'q' for pressionada, fim do ciclo
    if key == ord('q'):
        break

saida_video.release()

cv.destroyAllWindows()
