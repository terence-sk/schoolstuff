#!/usr/bin/python3

"""01_1-grayscale-np.py: prepocet RGB obrazku do odtienov sedej pomocou kniznice Numpy"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


import time
from PIL import Image
import numpy as np

# nacitaj obrazok
obrazok = Image.open('gaboboss.jpg')
sirka, vyska = obrazok.size

# vytvor jeho verziu v odtienoch sedej
l = time.time()

a = np.array(obrazok)
rgb = a.reshape((sirka*vyska), -1)

#intenzita = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
#intenzita = 0.2989*rgb[:,0] + 0.5870*rgb[:,1] + 0.1140*rgb[:,2]
intenzita = np.array(0.2989*rgb[:,0] + 0.5870*rgb[:,1] + 0.1140*rgb[:,2], dtype=np.uint8)

novy = Image.fromarray(intenzita.reshape((vyska, sirka)), 'L')

print("--- %s sekund ---" % (time.time() - l))

# zobraz/uloz vysledok
novy.show()
#novy.save('vysledok.png')

