from PIL import Image
import matplotlib.pyplot as plt
 
img1 = Image.open("./left.jpg")
img2 = Image.open("./right.jpg")
result = Image.new(img1.mode, (640*2, 480 ))
result.paste(img1, box=(0, 0))
result.paste(img2, box=(640, 0))
result.save("./new_image.jpg")
plt.imshow(result)
plt.show()