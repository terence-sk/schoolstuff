import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open('monalisa.png')
width, height = pic.size

a = np.array(pic)

rgb = a.reshape((width*height), -1)
intensity = np.array(0.2989*rgb[:, 0] + 0.5870*rgb[:, 1] + 0.1140*rgb[:, 2], dtype=np.uint8)


hist = np.bincount(intensity)
# ak je pole mensie/vacsie ako 256, upravi ho na tu velkost
hist.resize(256)

for i in range(0, 256):
    print(i, "i: ", hist[i])

x = hist/(width*height)

# kumulovaná pravdepodobnosť je funkcia, ktorá udáva pravdepodobnosť,
# že je hodnota náhodnej premennej menšia ako (alebo menšia rovná ako) zadaná hodnota
cdf = np.round(hist.cumsum()*255).astype(np.uint8)
eq_a = cdf[a]
eq_hist = np.zeros(256)

#flat = iterator 1d pola
for p in eq_a.flat:
    eq_hist[p] += 1

eq_hist /= (height*width)

# counts, bin_edges = np.histogram(x, bins=257, normed=True)
# cdf = np.cumsum(counts)
# plt.plot(bin_edges[1:], cdf)
#
# plt.show()

plt.bar(range(len(eq_hist)), eq_hist, linewidth=0, width=1)
plt.xlim((0, 256))
plt.xticks(range(0, 257, 32))
plt.show()
