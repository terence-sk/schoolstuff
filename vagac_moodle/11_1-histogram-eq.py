#!/usr/bin/python3

"""11_1-histogram-eq.py: ekvalizacia histogramu"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# nacitaj obrazok a skonvertuj ho do odtienov sedej
obrazok = Image.open('monalisa.png').convert('L')
sirka, vyska = obrazok.size

# generuj normalizovany histogram
hist = np.bincount(np.array(obrazok).flat)
hist.resize(256)
hist = hist.astype(float) / (vyska * sirka)

# sprav ekvalizaciu (cdf je funkcia na prepocet)
cdf = np.round(hist.cumsum() * 255).astype(np.uint8)
obrazok_s_eq_hist = cdf[np.array(obrazok)]

# generuj normalizovany histogram obrazku s ekvalizovanym histogramom
equalized_hist = np.bincount(obrazok_s_eq_hist.flat)
equalized_hist.resize(256)
equalized_hist = equalized_hist.astype(float) / (vyska * sirka)

# vypis
for i in range(0, 256):
	print(i, ": ", equalized_hist[i])

# zobraz
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.bar(range(len(hist)), hist, linewidth=0, width=1)
ax1.set_xlim((0,256))
ax1.set_xticks(range(0,257,32))
ax1.set_xlabel('$intenzita$')
ax1.set_ylabel('$pocet$')
ax2 = fig.add_subplot(122)
#ax2.bar(range(len(cdf)), cdf, linewidth=0, width=1)
ax2.bar(range(len(equalized_hist)), equalized_hist, linewidth=0, width=1)
ax2.set_xlim((0,256))
ax2.set_xticks(range(0,257,32))
ax2.set_xlabel('$intenzita$')
plt.show()

# zobraz/uloz vysledok
novy = Image.fromarray(obrazok_s_eq_hist)
novy.show()
#novy.save('vysledok.png')

