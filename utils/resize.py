import PIL
from PIL.Image import Image
from PIL import Image



from PIL import Image

im = Image.open("test.png")
rgb_im = im.convert('RGB')
rgb_im.save('test.jpg')
# Image.open() can also open other image types
img = Image.open("test.jpg")
# WIDTH and HEIGHT are integers
resized_img = img.resize((100, 120))
resized_img.save("resized_test.jpg")