
#importing all the libraries 

from flask import Flask, render_template, request
import os
import cv2
import glob
import shutil
import random
import numpy as np
from skimage import img_as_ubyte
from PIL import Image
from glitch_this import ImageGlitcher



app = Flask(__name__)

#defining the different type of noise functions

def normal_noise(source):
    img = cv2.imread(source, 0)
    if img is None:
        print(f"Error: Unable to open the image at '{source}'")
        return

    img = img / 255
    x, y = img.shape
    a = 0
    b = 0.2
    n = np.random.uniform(a, b, (x, y))
    noise_img = img + n
    noise_img = np.clip(noise_img, 0, 1)

    cv2.imwrite(source, img_as_ubyte(noise_img))

#salt and pepper noise
def add_salt_and_pepper_noise(file_path, pepper=0.1, salt=0.95):
    img = cv2.imread(file_path, 0)

    x, y = img.shape
    g = np.zeros((x, y), dtype=np.float32)

    for i in range(x):
        for j in range(y):
            rdn = np.random.random()
            if rdn < pepper:
                g[i][j] = 0
            elif rdn > salt:
                g[i][j] = 255
            else:
                g[i][j] = img[i][j]

    g_normalized = g / 255.0
    g_uint8 = img_as_ubyte(g_normalized)

    cv2.imwrite(file_path, g_uint8)    

#adding the blurred function
    
def apply_motion_blur(input_path, output_path='blurred_image.jpg', T=0.5, a=0.05, b=0):
    f = cv2.imread(input_path, 0)
    F = np.fft.fft2(f)

    M, N = F.shape
    H = np.zeros((M, N), dtype=np.complex128)

    for u in range(M):
        for v in range(N):
            s = np.pi * (u * a + v * b)
            H[u, v] = (T / s) * np.sin(s) * np.exp(-1j * s) if s != 0 else 0

    G = H * F
    g = np.fft.ifft2(G)
    g = np.abs(g)

    g_normalized = (g - np.min(g)) / (np.max(g) - np.min(g))
    g_uint8 = img_as_ubyte(g_normalized)

    cv2.imwrite(output_path, g_uint8, [int(cv2.IMWRITE_JPEG_QUALITY), 100])



# New function for glitching
    
def glitcher_lines(image_path):
    glitcher=ImageGlitcher()
    img = Image.open(image_path)
    glitch_img = glitcher.glitch_image(img, 2)
    glitch_img = glitch_img.convert('L')
    glitch_img.save('glitched_image.jpg')



#flask functions
    
@app.route('/', methods=['GET'])

def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def predict():
    videofile= request.files['videofile']
    image_path = "./images/" + videofile.filename
    videofile.save(image_path)
    print(image_path)
    video_path = image_path
    output_dir = 'frames/'
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_filename, frame)
        else:
            break
    

    #after extracting images into a folder that contains different frames
    folder_path = r'C:\Users\yashas\final_project\frames'
    output_folder_path = r'C:\Users\yashas\final_project\selected_frames'

    if os.path.exists(folder_path):
        image_files = glob.glob(os.path.join(folder_path, '*.jpg')) 
        percentage_to_move = 20
        num_images_to_move = int(len(image_files) * (percentage_to_move / 100))
        images_to_move = random.sample(image_files, num_images_to_move)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        for image_to_move in images_to_move:
            destination_path = os.path.join(output_folder_path, os.path.basename(image_to_move))
            # Handle existing files by adding a suffix or unique identifier
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(os.path.basename(image_to_move))
                destination_path = os.path.join(output_folder_path, f'{base}_duplicate{ext}')
            shutil.move(image_to_move, destination_path)
            # Call noise function for each moved image
            normal_noise(destination_path)
            add_salt_and_pepper_noise(destination_path)
            apply_motion_blur(destination_path)
            glitcher_lines(destination_path)

        
    cap.release()
    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
