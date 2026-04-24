import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Load image
dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(dir, "IMG_2031.jpeg")

# Image -> np array
img = Image.open(image_path).convert("RGB")
img_array = np.array(img)

h, w, _ = img_array.shape

# Create destination grid
y_dst, x_dst = np.indices((h, w))
coord_dst = np.stack([y_dst.flatten(), x_dst.flatten()])

# center of image
cx, cy = w // 2, h // 2

# shift origin to center
coord_centered = coord_dst.copy()
coord_centered[0] -= cx   # x shift
coord_centered[1] -= cy   # y shift

# rotation matrix
A = np.array([
    [2, 0],
    [0, 2]
])

# Inverse = transpose
A_inv = A.T

# apply inverse mapping
src_coord = A_inv @ coord_centered

# shift back
src_coord[0] += cx
src_coord[1] += cy

# reshape back to image grid
src_x = src_coord[0].reshape(h, w)
src_y = src_coord[1].reshape(h, w)

# clip to valid range
src_x = np.clip(src_x, 0, w - 1).astype(int)
src_y = np.clip(src_y, 0, h - 1).astype(int)

# sample pixels
new_img = img_array[src_y, src_x]
 #chalo result show karein
plt.style.use("dark_background")
plt.imshow(new_img)
plt.axis("off")
plt.show()