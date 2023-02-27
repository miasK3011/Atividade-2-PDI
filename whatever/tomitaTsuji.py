from PIL import Image
import numpy as npy

def tomitaTsuji(img, window_size=5):
    if window_size % 2 == 0:
        window_size += 1

    filtered_img = npy.zeros(img.shape)

    half_size = window_size // 2

    for y in range(half_size, img.shape[0] - half_size):
        for x in range(half_size, img.shape[1] - half_size):
            window = img[y - half_size: y + half_size + 1, x - half_size: x + half_size + 1]

            median = npy.median(window)
            var = npy.var(window)

            if var == 0:
                a = 0
            else:
                a = 0.5 * var / (var + npy.square(median - img[y, x]))

            filtered_img[y, x] = median + a * (img[y, x] - median)

    filtered_img = filtered_img.astype(npy.uint8)
    return Image.fromarray(filtered_img[window_size // 2:-window_size // 2, window_size // 2:-window_size // 2])
