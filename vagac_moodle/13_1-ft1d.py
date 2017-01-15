#!/usr/bin/python3

"""13_1-ft1d.py: jednorozmerna fourierova transformacia"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


import time
import cmath
import math
import matplotlib.pyplot as plt

def DFT_manual(fx, centruj = False):
	"""Vypocitaj jednorozmernu diskretnu fourierovu transformaciu pola fx"""
	M = len(fx)
	fx2 = list(fx)
	if centruj:
		for x in range(0, M):
			fx2[x] = math.pow(-1, x) * fx2[x]
	Fu = [0] * M
	for u in range(0, M):
		sum = 0
		for x in range(0, M):
			sum += fx2[x] * cmath.exp(-2j * cmath.pi * u * x / M)
		Fu[u] = sum
	return Fu

def FFT_manual(fx):
	"""Rekurzivne vypocitaj jednorozmernu rychlu fourierovu transformaciu pola fx"""
	n = len(fx)
	w = cmath.exp(-2*cmath.pi*1j/n)
	if n > 1:
		fx = FFT_manual(fx[::2]) + FFT_manual(fx[1::2])
		for k in range(int(n/2)):
			xk = fx[k]
			fx[k] = xk + w**k*fx[int(k+n/2)]
			fx[int(k+n/2)] = xk - w**k*fx[int(k+n/2)]
	return fx


# priprav (generuj) data #1: 1 schod
fx = []
for i in range(0, 700):
	if i < 40:
		fx.append(30);
	else:
		fx.append(00);
# priprav (generuj) data #2: sinus
#fx = []
#for i in range(0, 300):
#	j = float(i)/300*2*math.pi
#	fx.append(math.sin(3.0*j))
# priprav (generuj) data #3: hlavna frekvencia, na ktorej je namodulovana druha frekvencia
#fx = []
#for i in range(0, 300):
#	j = float(i)/300*2*math.pi
#	fx.append(10*math.cos(2.0*j)+math.sin(50.0*j))

# pocitaj DFT
l = time.time()
Fu = DFT_manual(fx, True)
print("--- %s sekund ---" % (time.time() - l))

# pre zobrazenie nas zaujima magnituda (amplitudove spektrum); ktore sa vypocita ako obsolutna hodnota komplexneho cisla
for x in range(0, len(Fu)):
	Fu[x] = abs(Fu[x])

# zobraz
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(fx)
ax1.set_xlabel('casova domena')
ax1.set_ylim((0,50))
ax2 = fig.add_subplot(122)
ax2.plot(range(int(-len(Fu)/2), int(len(Fu)/2)), Fu)
ax2.set_xlabel('frekvencna domena')
plt.show()

