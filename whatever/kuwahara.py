from PIL import Image
import numpy as npy

def kuwahara(imagem):
    """Aplica o filtro de suavização kuwahara na imagem dada como paramêtro.

    Args:
        imagem (Image)
    """
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
                subregiao_mask = subregiao[submascara[0]:submascara[1]+1, submascara[2]:submascara[3]+1]
                m.append(npy.mean(subregiao_mask))
                variancias.append(npy.var(subregiao_mask))

            min_variancia_index = npy.argmin(variancias)
            min_variancia_submascara = submascaras[min_variancia_index]

            img_filtrada[i, j] = npy.mean(subregiao[min_variancia_submascara[0]:min_variancia_submascara[1] +
                                          1, min_variancia_submascara[2]:min_variancia_submascara[3]+1])

    img_filtrada = Image.fromarray(img_filtrada)
    return img_filtrada