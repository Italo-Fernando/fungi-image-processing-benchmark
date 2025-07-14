from PIL import Image
import cv2
import numpy as np

paths = [
    './defungi_dataset/BBH/H6_4b_4.jpg', './defungi_dataset/GMA/H3_3a_10.jpg', './defungi_dataset/SHC/H5_104a_2.jpg', './defungi_dataset/BBH/H6_52a_13.jpg', 
    './defungi_dataset/GMA/H3_25a_2.jpg', './defungi_dataset/BBH/H6_56b_2.jpg', './defungi_dataset/TSH/H1_116b_11.jpg' , './defungi_dataset/SHC/H5_36a_4.jpg'
]

size = 250
margin = 2

nrows = 2
ncols = 4

collage_size = (margin + (size + margin)*ncols, margin + (size + margin)*nrows)
collage = Image.new(mode='RGB', size=collage_size)

for i in range(nrows):
    for j in range(ncols):
        idx = i*ncols + j
        image = Image.open(paths[idx])
        image.thumbnail((size, size))

        img_pos = (margin + (size + margin)*j, margin + (size + margin)*i)
        collage.paste(image, box=img_pos)

collage.save('mosaico.jpg')

collage_cv = cv2.cvtColor(np.array(collage), cv2.COLOR_RGB2BGR)
inverted_image = cv2.bitwise_not(collage_cv)
cv2.imwrite('mosaico_invertido.jpg', inverted_image)