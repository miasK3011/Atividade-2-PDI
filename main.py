from PIL import Image
import numpy as npy


def aplicarSalPimenta(imagem):
    img_matriz = npy.array(imagem)
    img_ruido = salPimenta(img_matriz, 0.2)
    img_fim = npy.where(img_ruido == 0, img_matriz, img_ruido)
    resultado = Image.fromarray(img_fim)
    resultado.show()

    return resultado


def salPimenta(imagem, quant=0.5):
    img = npy.copy(imagem)
    mask = npy.random.random(imagem.shape) < quant

    img[mask] = npy.where(npy.random.random(npy.sum(mask)) < 0.5, 0, 255)

    return img

def kuwahara(imagem):
    mascara = npy.array([[0,  0,  0,  0,  0],
                      [0,  1,  1,  1,  0],
                      [0,  1, -2,  1,  0],
                      [0,  1,  1,  1,  0],
                      [0,  0,  0,  0,  0]])
    
    a, l = imagem.shape[:2]
    mascara_a, mascara_l = mascara.shape[:2]
    
    img_filtrada = imagem.copy()
    
    borda = int((mascara_a - 1) / 2)
    
    


def main():
    imagem = Image.open("image.jpg").convert("L")
    img_ruido = aplicarSalPimenta(imagem)
    
    kuwahara(imagem)

    # img_filtrada = aplicarMask(img_ruido, mascara)
    # img_filtrada.save("Exemplo.jpg")

    img_filtrada.show()


if __name__ == "__main__":
    main()
