import numpy as np

img= np.random.rand(32, 32)
img_extended = np.expand_dims(img, axis=0)
print("shape", img_extended.shape)
print()