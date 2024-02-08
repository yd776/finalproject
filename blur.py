import numpy as np
import cv2
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

def apply_motion_blur(input_path, output_path='blurred_image.jpg', T=0.5, a=0.05, b=0):
    # Read the input image
    f = cv2.imread(input_path, 0)

    # F(u,v), image in frequency domain
    F = np.fft.fft2(f)

    plt.imshow(np.log1p(np.abs(F)), cmap='gray')
    plt.axis('off')
   

    # H(u,v), motion blur function in frequency domain
    # Create matrix H (motion blur function H(u,v))
    M, N = F.shape
    H = np.zeros((M, N), dtype=np.complex128)

    # Fill matrix H
    for u in range(M):
        for v in range(N):
            s = np.pi * (u * a + v * b)
            # Avoid division by zero
            H[u, v] = (T / s) * np.sin(s) * np.exp(-1j * s) if s != 0 else 0

    plt.imshow(np.log1p(np.abs(H)), cmap='gray')
    plt.axis('off')


    # G(u,v), blurred image in frequency domain
    G = H * F

    plt.imshow(np.log1p(np.abs(G)), cmap='gray')
    plt.axis('off')


    # g(x,y), blurred image in spatial domain
    g = np.fft.ifft2(G)
    g = np.abs(g)

    # Normalize the values in the range [0, 1]
    g_normalized = (g - np.min(g)) / (np.max(g) - np.min(g))

    g_uint8 = img_as_ubyte(g_normalized)  # if you want to save the image

    # Display images using cv2.imshow

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the blurred image
    cv2.imwrite(output_path, g_uint8)



# Example usage:


input_image_path = 'C:\\Users\\yashas\\final_project\\frames\\frame_0001.jpg'
apply_motion_blur(input_image_path)