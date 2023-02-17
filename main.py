from PIL import Image
import numpy as npy
import sys

def aplicarSalPimenta(imagem, ruido):
    img_matriz = npy.array(imagem)
    img_ruido = salPimenta(img_matriz, ruido)
    img_fim = npy.where(img_ruido == 0, img_matriz, img_ruido)
    resultado = Image.fromarray(img_fim)
    resultado.show()

    return img_fim


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

    for i in range(borda, a - borda):
        for j in range(borda, l - borda):
            subregiao = imagem[i-borda:i+borda+1, j-borda:j+borda+1]

            submascaras = [(0, 2, 0, 2), (0, 2, 3, 4),
                           (3, 4, 3, 4), (3, 4, 0, 2)]
            m = []
            variancias = []

            for submascara in submascaras:
                subregiao_mask = subregiao[submascara[0]
                    :submascara[1]+1, submascara[2]:submascara[3]+1]
                m.append(npy.mean(subregiao_mask))
                variancias.append(npy.var(subregiao_mask))

            min_variancia_index = npy.argmin(variancias)
            min_variancia_submascara = submascaras[min_variancia_index]

            img_filtrada[i, j] = npy.mean(subregiao[min_variancia_submascara[0]:min_variancia_submascara[1] +
                                          1, min_variancia_submascara[2]:min_variancia_submascara[3]+1])

    img_filtrada = Image.fromarray(img_filtrada)
    img_filtrada.show()


def main():
    imagem = 0
    try:
        imagem = Image.open("image.jpg").convert("L")
    except:
        print("Imagem inválida")
        sys.exit(1)
    
    # Aplica ruido sal e pimenta e aplica o filtro de kuwahara
    img_ruido = aplicarSalPimenta(imagem, 0.6)    
    kuwahara(img_ruido)

    # img_filtrada = aplicarMask(img_ruido, mascara)
    # img_filtrada.save("Exemplo.jpg")

    # img_filtrada.show()


if __name__ == "__main__":
    main()
