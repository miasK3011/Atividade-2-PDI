from PIL import Image
import numpy as npy
import sys
from kuwahara import *
from tomitaTsuji import *
from salPimenta import *

def aplicarSalPimenta(imagem):
    img_matriz = npy.array(imagem)
    img_ruido = salPimenta(img_matriz)
    resultado = Image.fromarray(img_ruido)
    resultado.show("Imagem com Ruido Sal e Pimenta")

    return img_ruido

def main():
    imagem = None
    try:
        imagem = Image.open("image.jpg").convert("L")
    except:
        print("Imagem inválida")
        sys.exit(1)

    img_ruido = aplicarSalPimenta(imagem)

    # Filtro de Kuwahara
    img_kuwahara = kuwahara(img_ruido)
    img_kuwahara.show("Kuwahara: Imagem filtrada")

    # Filtro Tomita Tsuji
    img_tomitaTsuji = tomitaTsuji(img_ruido)
    img_tomitaTsuji.show()

if __name__ == "__main__":
    main()
