from envtest import rand_array
from scipy.ndimage import gaussian_filter
from scipy import misc
from scipy import misc
import matplotlib.pyplot as plt

shape = (3, 3)

print(rand_array(shape))




__all__ = ['rand_array', 'smooth_image']

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)




image = misc.ascent()
sigma = 5

smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
f.add_subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.show(block=True)