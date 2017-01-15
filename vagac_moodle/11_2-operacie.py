#!/usr/bin/python3

"""11_2-operacie.py: aritmeticke a logicke operacie s obrazkom"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


from PIL import Image
import numpy as np

# nacitaj obrazok a skonvertuj ho do odtienov sedej
obrazok = Image.open('gaboboss.jpg').convert('L')
sirka, vyska = obrazok.size
npobrazok = np.array(obrazok)

# aplikuj operaciu
limit = 170
x, y = (npobrazok > limit).nonzero()
npobrazok[x, y] = 0
#a[a > limit] = 0

# zobraz/uloz vysledok
novy = Image.fromarray(npobrazok, 'L')
novy.show()
#novy.save('vysledok.png')

