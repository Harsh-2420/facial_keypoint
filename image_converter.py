import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img, img_to_array


img = load_img('image_1.png', target_size=(96, 96))
x = img_to_array(img)
# original_array = np.loadtxt("images.txt").reshape(96, 96, 1)
# plt.imshow(original_array.reshape(96, 96), cmap='gray')
# plt.savefig('image_2')
