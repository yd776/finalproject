from PIL import Image
from glitch_this import ImageGlitcher
glitcher=ImageGlitcher()


def glitcher_lines(str):
    img=Image.open(str)
    glitch_img=glitcher.glitch_image(img,2)
    glitch_img = glitch_img.convert('L')
    glitch_img.save(r'glitched_plsy.jpg')

glitcher_lines(r'C:\Users\yashas\final_project\frames\frame_0001.jpg')
