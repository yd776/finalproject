import cv2
import numpy as np
from skimage import img_as_ubyte

def add_salt_and_pepper_noise(file_path, pepper=0.1, salt=0.95):
    # Read the original image
    img = cv2.imread(file_path, 0)

    # Display the original image
   
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create a blank image
    x, y = img.shape
    g = np.zeros((x, y), dtype=np.float32)

    # Create salt and pepper noise in the image
    for i in range(x):
        for j in range(y):
            rdn = np.random.random()
            if rdn < pepper:
                g[i][j] = 0
            elif rdn > salt:
                g[i][j] = 255
            else:
                g[i][j] = img[i][j]

    # Display the image with salt and pepper noise
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Normalize the values in the range [0, 1]
    g_normalized = g / 255.0

    # Convert to uint8 using img_as_ubyte
    g_uint8 = img_as_ubyte(g_normalized)

    # Save the image
    cv2.imwrite('salt_and_pepper_output.jpg', g_uint8)

# Example usage:
file_path = 'C:\\Users\\yashas\\final_project\\frames\\frame_0001.jpg'
add_salt_and_pepper_noise(file_path)

