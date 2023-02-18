from PIL import Image
import numpy as npy

def tomitaTsuji(img, window_size=5):

    if window_size % 2 == 0:
        window_size += 1

    filtered_img = npy.zeros(img.shape)

    for y in range(window_size // 2, img.shape[0] - window_size // 2):
        for x in range(window_size // 2, img.shape[1] - window_size // 2):

            window = img[y - window_size // 2: y + window_size // 2 + 1,
                         x - window_size // 2: x + window_size // 2 + 1]

            median = npy.median(window)
            var = npy.var(window)
            if var == 0:
                a = 0
            else:
                a = 0.5 * var / (var + npy.square(median - img[y, x]))

            filtered_img[y, x] = median + a * (img[y, x] - median)

    return Image.fromarray(filtered_img.astype(npy.uint8))
