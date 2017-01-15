from PIL import Image
import time
import numpy as np
import matplotlib.pyplot as plt

fxy = Image.open("monalisa.png").convert('L')
sirka, vyska = fxy.size
ds = 20
dv = 20
D=30
l=time.time()
Fuv=np.fft.fft2(fxy)
print("---%s sekund" % (time.time()-1))
Fuv[0,0]=0
PSD=np.abs(Fuv)**2

fig = plt.figure()
ax1 = fig.add_subplot(231)
ax1.imshow(fxy,cmap='gray')
ax1.set_xlabel('priestorova domena')
ax2=fig.add_subplot(234)
ax2.imshow(np.log10(np.fft.fftshift(PSDF)), cmap='gray')
ax2.set_xlabel('frekvencna domena')
ax3=fig.add_subplot(233)
ax3.set_xlabel('frekvencna domena(log 10)')
ax3.imshow(hxy, cmap='gray')
ax4 = fig.add_subplot(236)
ax4.imshow(np.log10(PSDG), cmap='gray')
ax4.set_xlabel('frekvencna domena')
ax5 = fig.add_subplot(235, projection='3d')
x, y = np.ngrid[:vyska, :sirka]
ax5.plot_surface(x, y, Huv, rstride=30, cstride=30, cmap=plt.cm.gray, linewidth=0, antialiased=False)
plt.show()
