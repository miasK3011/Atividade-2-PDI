import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the image with openCV
image = cv2.imread('./Mascaras/ruido.jpg', cv2.IMREAD_GRAYSCALE) 
image_width = image.shape[0]
image_height = image.shape[1]

def kuwahara_filter(img):
    # Step 2: Criar uma matriz vazia com as mesmas dimensões da imagem
    result = np.zeros_like(img, dtype=np.float32)

    # Step 3: Iterar sobre cada pixel da imagem, exceto pelas bordas, aplicando a máscara de Tomita e Tsuji e armazenando o resultado na matriz criada no passo 2
    for i in range(2, img.shape[0]-2):
        for j in range(2, img.shape[1]-2):
            q1 = img[i-2:i+1, j-2:j+1].astype(np.float32)
            q2 = img[i-2:i+1, j:j+3].astype(np.float32)
            q3 = img[i:i+3, j-2:j+1].astype(np.float32)
            q4 = img[i:i+3, j:j+3].astype(np.float32)

            # Calcula as médias e os desvios padrão de cada quadrante
            m1, s1 = cv2.meanStdDev(q1)
            m2, s2 = cv2.meanStdDev(q2)
            m3, s3 = cv2.meanStdDev(q3)
            m4, s4 = cv2.meanStdDev(q4)
            # Escolhe o quadrante com a menor variação de intensidade
            vars = [s1, s2, s3, s4]
            idx = vars.index(min(vars))
            if idx == 0:
                reg = q1
            elif idx == 1:
                reg = q2
            elif idx == 2:
                reg = q3
            else:
                reg = q4
            # Calcula a média e a variância da região escolhida
            m, s = cv2.meanStdDev(reg)
            # Atualiza o pixel atual na imagem de resultado com a média da região escolhida
            result[i, j] = m[0][0]

    # Step 4: Normalizar a matriz de saída para garantir que os valores fiquem no intervalo [0, 255]
    result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255.0

    # Step 5: Converter a matriz de saída em uma imagem e salvá-la ou exibi-la na tela.
    result_img = np.uint8(result)
    return result_img

filtered_img = kuwahara_filter(image)

cv2.imshow('result', filtered_img)
k = cv2.waitKey(0) 

if k == ord("s"): # save the image
    cv2.imwrite("kuwahara_cama_ruido.jpg", filtered_img)