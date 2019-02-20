import numpy as np
from PIL import Image

im = Image.open("./goat.jpeg")
arr = np.asarray(im)
print(arr)
