#!/usr/bin/python3

"""11_1-histogram.py: vypocet histogramu obrazku odtienov sedej"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


from PIL import Image
import matplotlib.pyplot as plt

# nacitaj obrazok a skonvertuj ho do odtienov sedej
obrazok = Image.open('monalisa.png').convert('L')
sirka, vyska = obrazok.size

# generuj histogram
hist = [0] * 256
for y in range(0, vyska):
	for x in range(0, sirka):
		intenzita = obrazok.getpixel((x, y))
		hist[intenzita] += 1

# vypis
for i in range(0, 256):
	print(i, ": ", hist[i])

# zobraz
plt.bar(range(len(hist)), hist, linewidth=0, width=1)
plt.xlim((0,256))
plt.xticks(range(0,257,32))
plt.show()

