import cv2 as cv
import numpy as np

# Carregue a imagem original
img = cv.imread("lake.jpg")

# Obtenha as dimensões da imagem
altura, largura, canais = img.shape

# Divida a imagem em metade esquerda e metade direita
metade_esquerda = img[:, :largura // 2]
metade_direita = img[:, largura // 2:]

# Crie uma janela para exibir a sequência de imagens
cv.namedWindow("Sequência de Imagens", cv.WINDOW_NORMAL)  # WINDOW_NORMAL permite redimensionar a janela

# Crie um objeto VideoWriter para salvar o vídeo
fourcc = cv.VideoWriter_fourcc(*"XVID")
saida_video = cv.VideoWriter("saida_video.avi", fourcc, 10.0, (largura, altura))

# Crie um ciclo for para variar o fator de aumento
for fator_aumento in np.arange(1.0, 0.0, -0.1):  # Varia de 1.0 a 0.0 em decrementos de 0.1
    # Ajuste a intensidade dos pixels da metade direita
    metade_direita_aumentada = (metade_direita * fator_aumento).astype(np.uint8)

    # Reúna as duas metades em uma única imagem
    imagem_resultante = np.hstack((metade_esquerda, metade_direita_aumentada))

    # Escreva o quadro atual no vídeo
    saida_video.write(imagem_resultante)

    # Atualize o conteúdo da janela com a nova imagem
    cv.imshow("Sequência de Imagens", imagem_resultante)

    # Aguarde por um curto período de tempo (em milissegundos)
    # ou até que uma tecla seja pressionada (0 significa esperar indefinidamente)
    key = cv.waitKey(1000)

    # Se a tecla 'q' for pressionada, saia do ciclo
    if key == ord('q'):
        break

# Libere o objeto VideoWriter
saida_video.release()

# Feche a janela
cv.destroyAllWindows()
