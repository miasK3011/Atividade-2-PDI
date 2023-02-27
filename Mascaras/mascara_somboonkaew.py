import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the image with openCV
image = cv2.imread('./Mascaras/ruido.jpg', cv2.IMREAD_GRAYSCALE) 
image_width = image.shape[0]

def somboon_matsuyama_filter(img):
    # Step 2: Criar uma matriz vazia com as mesmas dimensões da imagem
    result = np.zeros_like(img, dtype=np.float32)

    # Step 3: Iterar sobre cada pixel da imagem, exceto pelas bordas, aplicando a máscara de somboonkaew e armazenando o resultado na matriz criada no passo 2
    for i in range(2, img.shape[0]-2):
        for j in range(2, img.shape[1]-2):
            q1 = img[i-2:i+3, j-2:j+3].astype(np.float32)
            mask = np.zeros((5, 5), dtype=bool)
            mask[[0,1,2,3,4],[0,1,2,3,4]] = True
            mask[[3, 1], [1, 3]] = True
            #print("q1",mask)
            q1 = q1[mask]


            q2 = img[i-2:i+3, j-2:j+3].astype(np.float32)
            mask = np.zeros((5, 5), dtype=bool)
            mask[[1,3],[1,3]] = True #diagonal principal
            mask[[4, 3, 2, 1, 0], [0, 1, 2, 3, 4]] = True #secundaria
            #print("q2",mask)
            q2 = q2[mask]

            q3 = img[i-1:i+2, j-2:j+3].astype(np.float32)
            mask = np.zeros((3, 5), dtype=bool)
            mask[[0,1,1,1,1,1,2],[2,0,1,2,3,4,2]] = True 
            #print("q3",mask)
            q3 = q3[mask]

            q4 = img[i-2:i+3, j-1:j+2].astype(np.float32)
            mask = np.zeros((5, 3), dtype=bool)
            mask[[0, 1, 2, 3, 4, 2, 2],[1, 1, 1, 1, 1, 0, 2]] = True 
            #print("q4",mask)
            q4 = q4[mask]


            q5 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[1, 1],[0, 2]] = False
            #print("q5",mask)
            q5 = q5[mask]

            q6 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 2],[1, 1]] = False
            #print("q6",mask)
            q6 = q6[mask]

            q7 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 2],[2, 0]] = False
            #print("q7",mask)
            q7 = q7[mask]

            q8 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 2],[0, 2]] = False
            #print("q8",mask)
            q8 = q8[mask]

            q9 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 0],[0, 2]] = False
            #print("q9",mask)
            q9 = q9[mask]

            q10 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 2],[2, 2]] = False
            #print("q10",mask)
            q10 = q10[mask]

            q11 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[2, 2],[0, 2]] = False
            #print("q11",mask)
            q11 = q11[mask]

            q12 = img[i-1:i+2, j-1:j+2].astype(np.float32)
            mask = np.ones((3, 3), dtype=bool)
            mask[[0, 2],[0, 0]] = False
            #print("q12",mask)
            q12 = q12[mask]


            # Calcula as médias e os desvios padrão de cada quadrante
            m1, s1 = cv2.meanStdDev(q1)
            m2, s2 = cv2.meanStdDev(q2)
            m3, s3 = cv2.meanStdDev(q3)
            m4, s4 = cv2.meanStdDev(q4)
            m5, s5 = cv2.meanStdDev(q5)
            m6, s6 = cv2.meanStdDev(q6)
            m7, s7 = cv2.meanStdDev(q7)
            m8, s8 = cv2.meanStdDev(q8)
            m9, s9 = cv2.meanStdDev(q9)
            m10, s10 = cv2.meanStdDev(q10)
            m11, s11 = cv2.meanStdDev(q11)
            m12, s12 = cv2.meanStdDev(q12)


            # Escolhe o quadrante com a menor variação de intensidade
            vars = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
            idx = vars.index(min(vars))
            if idx == 0:
                reg = q1
            elif idx == 1:
                reg = q2
            elif idx == 2:
                reg = q3
            elif idx == 3:
                reg = q4
            elif idx == 4:
                reg = q5
            elif idx == 5:
                reg = q6
            elif idx == 6:
                reg = q7
            elif idx == 7:
                reg = q8
            elif idx == 8:
                reg = q9
            elif idx == 9:
                reg = q10
            elif idx == 10:
                reg = q11
            else:
                reg = q12
            # Calcula a média e a variância da região escolhida
            m, s = cv2.meanStdDev(reg)
            # Atualiza o pixel atual na imagem de resultado com a média da região escolhida
            result[i, j] = m[0][0]

    # Step 4: Normalizar a matriz de saída para garantir que os valores fiquem no intervalo [0, 255]
    result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255.0

    # Step 5: Converter a matriz de saída em uma imagem e salvá-la ou exibi-la na tela.
    result_img = np.uint8(result)
    return result_img

filtered_img = somboon_matsuyama_filter(image)

cv2.imshow('result', filtered_img)
k = cv2.waitKey(0) 

if k == ord("s"): # save the image
    cv2.imwrite("somboonkaew-filter.jpg", filtered_img)