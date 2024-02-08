from flask import Flask, render_template, request
import os
import glob
import shutil
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_ubyte

def noise(source):
    img = cv2.imread(source, 0)

    if img is None:
        print(f"Error: Unable to open the image at '{source}'")
        return

    img = img / 255

    # uniform noise
    x, y = img.shape
    a = 0
    b = 0.2
    n = np.random.uniform(a, b, (x, y))

    # add noise to image
    noise_img = img + n
    noise_img = np.clip(noise_img, 0, 1)

    cv2.imwrite('noise_image.jpg', img_as_ubyte(noise_img))

# Use double backslashes or a raw string for the file path
    

noise(r'C:\Users\yashas\final_project\frames\frame_0001.jpg')

