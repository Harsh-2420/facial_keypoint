import numpy as np
import matplotlib.pyplot as plt


original_array = np.loadtxt("images.txt").reshape(96, 96, 1)
plt.imshow(original_array.reshape(96, 96), cmap='gray')
plt.savefig('image_1')
