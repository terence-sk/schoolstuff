#!/usr/bin/python3

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt


# priprav (generuj) data: hlavna frekvencia, na ktorej je namodulovana druha frekvencia
x = np.linspace(0.0, 300, 300)
xpi = 2.0*np.pi*x
fx = 10*np.cos(2.0*xpi) + np.sin(50.0*xpi)

# pocitaj FT
yf = fftpack.fft(fx)

# uprav frekvencnu domenu
yf2 = yf.copy()
#for i in range(45,55):
for i in range(0,10):
	yf2[i] = 0
#for i in range(245,255):
for i in range(290,300):
	yf2[i] = 0

# pocitaj IFT
fx2 = fftpack.ifft(yf2)

# zobraz
fig = plt.figure()
ax1 = fig.add_subplot(141)
ax1.plot(fx)
ax1.set_xlabel('casova domena')
ax2 = fig.add_subplot(142)
ax2.plot(fftpack.fftshift(np.abs(yf)))
#ax2.plot(np.abs(yf))
ax2.set_xlabel('frekvencna domena')
ax3 = fig.add_subplot(143)
ax3.plot(fftpack.fftshift(np.abs(yf2)))
ax3.set_xlabel('frekvencna domena po zmene')
ax4 = fig.add_subplot(144)
ax4.set_ylim((-15,15))
ax4.plot(fx2)
ax4.set_xlabel('casova domena po IFT')
plt.show()

