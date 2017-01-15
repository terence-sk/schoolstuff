#!/usr/bin/python3

"""13_3-fft2d-img.py: dvojrozmerna fourierova transformacia nacitanych obrazkov pomocou implementacie z kniznice Numpy"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


import time
from PIL import Image
import math
import numpy as np
import pylab as py
import matplotlib.pyplot as plt

# nacitaj obrazok a skonvertuj ho do odtienov sedej
fxy = Image.open('monalisa.png').convert('L')
sirka, vyska = fxy.size
ds = 20
dv = 20

# pocitaj FT
l = time.time()
Fuv = np.fft.fft2(fxy)
print("--- %s sekund ---" % (time.time() - l))
Fuv[0, 0] = 0				# odstran DC koli vizualizacii
PSD = np.abs(Fuv)**2			# 2D power spectrum

# zobraz
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.imshow(fxy, cmap='gray')
ax1.set_xlabel('priestorova domena')
ax2 = fig.add_subplot(222)
ax2.imshow(np.fft.fftshift(PSD), cmap='gray')
ax2.set_xlabel('frekvencna domena')
ax3 = fig.add_subplot(223)
ax3.imshow(np.log10(np.fft.fftshift(PSD)), cmap='gray')
ax3.set_xlabel('frekvencna domena (log10)')
ax4 = fig.add_subplot(224)
ax4.imshow(np.fft.fftshift(PSD)[int(vyska/2-dv):int(vyska/2+dv), int(sirka/2-ds):int(sirka/2+ds)], cmap='gray')
ax4.set_xlabel('frekvencna domena (detail)')
plt.show()

