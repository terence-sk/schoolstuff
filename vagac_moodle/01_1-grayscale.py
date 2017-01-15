#!/usr/bin/python3

"""01_1-grayscale.py: prepocet RGB obrazku do grayscale (odtienov sedej) obrazku"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


import time
from PIL import Image

# nacitaj obrazok
obrazok = Image.open('gaboboss.jpg')
sirka, vyska = obrazok.size

# vytvor jeho verziu v odtienoch sedej
l = time.time()

novy = Image.new('L', (sirka, vyska))
for y in range(0, vyska):
	for x in range(0, sirka):
		r, g, b = obrazok.getpixel((x, y))
		intenzita = 0.2989*r + 0.5870*g + 0.1140*b
		novy.putpixel((x, y), int(intenzita))

print("--- %s sekund ---" % (time.time() - l))

# zobraz/uloz vysledok
novy.show()
#novy.save('vysledok.png')

