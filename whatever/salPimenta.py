import random

def salPimenta(imagem):
    row, col = imagem.shape
    inicio, fim = 100, 10000

    number_of_pixels = random.randint(inicio, fim)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        imagem[y_coord][x_coord] = 255

    number_of_pixels = random.randint(inicio, fim)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        imagem[y_coord][x_coord] = 0

    return imagem