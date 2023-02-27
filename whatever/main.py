from PIL import Image
import numpy as npy
import sys
from kuwahara import *
from tomitaTsuji import *
from salPimenta import *
from nagaoMatsuyama import *
from maskMedia import *

def aplicarSalPimenta(imagem):
    img_matriz = npy.array(imagem)
    img_ruido = salPimenta(img_matriz)
    resultado = Image.fromarray(img_ruido)
    #resultado.show("Imagem com Ruido Sal e Pimenta")
    resultado.save("ruido.jpg")

    return img_ruido

def main():
    
    mascara = npy.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]) / 9
    
    imagem = None
    try:
        imagem = Image.open("./whatever/image.jpg").convert("L")
    except:
        print("Imagem inválida")
        sys.exit(1)

    img_ruido = aplicarSalPimenta(imagem)
    
    img_media = maskMedia(img_ruido, mascara)
    img_media.show()
    img_media.save("media-filter.jpg")

    # # Filtro de Kuwahara
    # img_kuwahara = kuwahara(img_ruido)
    # img_kuwahara.show("Kuwahara: Imagem filtrada")
    # img_kuwahara.save("kuwahara-filter.jpg")

    # # Filtro Tomita Tsuji
    # img_tomitaTsuji = tomitaTsuji(img_ruido)
    # img_tomitaTsuji.show()
    # img_tomitaTsuji.save("tomita-filter.jpg")
    
    # Nagao Matsuyama
    # img_nagao_matsuyama = nagaoMatsuyama(img_ruido)
    # img_nagao_matsuyama.show()

if __name__ == "__main__":
    main()