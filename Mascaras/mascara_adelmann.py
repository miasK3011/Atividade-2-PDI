import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the image with openCV
image = cv2.imread('./Mascaras/ruido.jpg', cv2.IMREAD_GRAYSCALE) 
image_width = image.shape[0]

def somboon_matsuyama_filter(img):
    result = np.zeros_like(img, dtype=np.float32)

    for i in range(2, img.shape[0]-2):
        for j in range(2, img.shape[1]-2):

            # Teste inicial
            # 1. horizontal
            q1 = img[i-1:i+2, j-2:j+3].astype(np.float32)
            mask_x1 = np.zeros((3, 5), dtype=bool)
            mask_x1[[0,0,0,0,0],[0,1,2,3,4]] = True
            x1 = q1[mask_x1]
            mask_x2 = np.zeros((3, 5), dtype=bool)
            mask_x2[[2,2,2,2,2],[0,1,2,3,4]] = True
            x2 = q1[mask_x2]

            mean_x1 = (np.mean(x1) * -1)
            mean_x2 = np.mean(x2)

            dif_q1 = abs(mean_x1 - mean_x2)


            q2 = img[i-2:i+3, j-1:j+2].astype(np.float32)
            mask_x1 = np.zeros((5, 3), dtype=bool)
            mask_x1[[0,1,2,3,4],[0,0,0,0,0]] = True
            x1 = q2[mask_x1]
            mask_x2 = np.zeros((5, 3), dtype=bool)
            mask_x2[[0,1,2,3,4],[2,2,2,2,2]] = True
            x2 = q2[mask_x2]

            mean_x1 = (np.mean(x1) * -1)
            mean_x2 = np.mean(x2)

            dif_q2 = abs(mean_x1 - mean_x2)

            q3 = img[i-2:i+3, j-2:j+3].astype(np.float32)
            mask_x1 = np.zeros((5, 5), dtype=bool)
            mask_x1[[0,1,2,3],[1,2,3,4]] = True
            x1 = q3[mask_x1]
            mask_x2 = np.zeros((5, 5), dtype=bool)
            mask_x2[[1,2,3,4],[0,1,2,3]] = True
            x2 = q3[mask_x2]

            mean_x1 = (np.mean(x1) * -1)
            mean_x2 = np.mean(x2)

            dif_q3 = abs(mean_x1 - mean_x2)

            q4 = img[i-2:i+3, j-2:j+3].astype(np.float32)
            mask_x1 = np.zeros((5, 5), dtype=bool)
            mask_x1[[3,2,1,0],[0,1,2,3]] = True
            x1 = q4[mask_x1]
            mask_x2 = np.zeros((5, 5), dtype=bool)
            mask_x2[[4,3,2,1],[1,2,3,4]] = True
            x2 = q4[mask_x2]

            mean_x1 = (np.mean(x1) * -1)
            mean_x2 = np.mean(x2)

            dif_q4 = abs(mean_x1 - mean_x2)

            difs = [dif_q1, dif_q2, dif_q3, dif_q4]
            idx = difs.index(max(difs))

            mean = 0
            threshold = 10
            if idx == 0 and dif_q1 > threshold:
                a = img[i, j-1:j+2].astype(np.float32)
                mean = int(np.mean(a))
            elif idx == 1 and dif_q2 > threshold:
                b = img[i-1:i+2, j].astype(np.float32)
                mean = int(np.mean(b))
            elif idx == 2 and dif_q3 > threshold:
                c = img[i-1:i+2, j-1:j+2].astype(np.float32)
                mask = np.zeros((3, 3), dtype=bool)
                mask[[0,1,2],[0,1,2]] = True
                c = c[mask]
                mean = int(np.mean(c))
            elif idx == 3 and dif_q4 > threshold:
                d = img[i-1:i+2, j-1:j+2].astype(np.float32)
                mask = np.zeros((3, 3), dtype=bool)
                mask[[2,1,0],[0,1,2]] = True
                d = d[mask]
                mean = int(np.mean(d))
            else:
                e = img[i-1:i+2, j-1:j+2].astype(np.float32)
                mask = np.zeros((3, 3), dtype=bool)
                mask[[0,1,1,1,2],[1,0,1,2,1]] = True
                e = e[mask]
                mean = int(np.mean(e))

            result[i, j] = mean

    # Step 4: Normalizar a matriz de saída para garantir que os valores fiquem no intervalo [0, 255]
    result = (result - np.min(result)) / (np.max(result) - np.min(result)) * 255.0

    # Step 5: Converter a matriz de saída em uma imagem e salvá-la ou exibi-la na tela.
    result_img = np.uint8(result)
    return result_img

filtered_img = somboon_matsuyama_filter(image)

cv2.imshow('result', filtered_img)
k = cv2.waitKey(0) 

if k == ord("s"): # save the image
    cv2.imwrite("adelmann-filter.jpg", filtered_img)