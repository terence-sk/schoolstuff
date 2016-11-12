import Image
import numpy as np

pic = Image.open('test.jpg')
width, height = pic.size

a = np.array(pic)

rgb = a.reshape((width*height), -1)

intensity = np.array(0.2989*rgb[:, 0] + 0.5870*rgb[:, 1] + 0.1140*rgb[:, 2], dtype=np.uint8)

pic2 = Image.fromarray(intensity.reshape((height, width)), 'L')
pic2.save('output2.png')
