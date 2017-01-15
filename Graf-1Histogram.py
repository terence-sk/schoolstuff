import Image
import array
import numpy as np

im = Image.open('monalisa.png')
rgb_im = im.convert("RGB")

width, height = im.size
gs_im = Image.new('L', (width, height))

histogram = array.array('i', (0 for i in range(0, 256)))

for x in range(0, height):
    for y in range(0, width):
        r, g, b = rgb_im.getpixel((y, x))
        average_value = (0.2989*r + 0.5870*g + 0.1140*b) / 3
        average_value = int(average_value)
        histogram[average_value] += 1
        gs_im.putpixel((y, x), average_value)

gs_im.save('Graf-Mainmona.png')

bin_counts, bin_edges = np.histogram(gs_im, 'auto')
print(bin_counts)
for idx, x in enumerate(bin_counts):
    print(idx,  x)
