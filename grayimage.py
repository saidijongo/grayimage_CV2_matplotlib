import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

image_path = "C:/Users/saidi/OneDrive/Desktop/damin/psp.jpeg"
jongo_img = cv2.imread(image_path)

if jongo_img is None:
    name = "Jongo"
    print(f"Go drink soju {name}")
else:
    plt.imshow(cv2.cvtColor(jongo_img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    gray_img = cv2.cvtColor(jongo_img, cv2.COLOR_BGR2GRAY)

    plt.imshow(gray_img, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()

    gray_image_path = os.path.join(
        "C:/Users/saidi/OneDrive/Desktop/damin", "psp_gray.jpeg")
    cv2.imwrite(gray_image_path, gray_img)
