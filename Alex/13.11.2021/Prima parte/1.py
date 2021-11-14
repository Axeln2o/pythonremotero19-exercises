import numpy as np
from PIL import Image

img = Image.open('Colorat.jpg')

arr = np.array(img)


arr[50, 70]


print(arr)
