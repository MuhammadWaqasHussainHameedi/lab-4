import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu
from scipy.stats import linregress
import glob

time = 0
time_list = []
area_list = []

# Update the path and pattern based on your file structure
path = "C:\\Users\\ma\\project\\data\\Lab-4 Practice\\Lab-4\\*.*"

# Print the files returned by glob.glob() for debugging
files = glob.glob(path)
print("Files found:", files)

for file in files:
    img = io.imread(file)
    entropy_img = entropy(img, disk(3))
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == 1)
    print("time=", time, "hr  ", "Scratch area=", scratch_area, "pix²")
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(binary, cmap='gray')
    plt.title('Thresholded Image')
plt.show()