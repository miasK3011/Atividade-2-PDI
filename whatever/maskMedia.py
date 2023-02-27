import numpy as npy
from PIL import Image

def maskMedia(imagem, mascara):
    img_matriz = npy.array(imagem)
    mask_matriz = npy.array(mascara)

    altura, largura = img_matriz.shape[:2]
    mask_altura, mask_largura = mask_matriz.shape[:2]
    
    img_saida = npy.zeros((altura-mask_altura+1, largura-mask_largura+1), dtype=npy.uint8)

    for y in range(img_saida.shape[0]):
        for x in range(img_saida.shape[1]):
            img_saida[y, x] = (img_matriz[y:y+mask_altura, x:x+mask_altura] * mask_matriz).sum()
            
    return Image.fromarray(img_saida)