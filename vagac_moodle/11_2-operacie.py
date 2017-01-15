#!/usr/bin/python3

"""11_2-operacie.py: aritmeticke a logicke operacie s obrazkom"""
__author__ = "Michal Vagac"
__email__  = "michal.vagac@gmail.com"


from PIL import Image
import numpy as np

# nacitaj obrazok a skonvertuj ho do odtienov sedej
obrazok = Image.open('monalisa.png').convert('L')
sirka, vyska = obrazok.size
npobrazok = np.array(obrazok)

# aplikuj operaciu
limit = 170
#Returns a tuple of arrays, one for each dimension of a,
# containing the indices of the non-zero elements in that dimension
x, y = (npobrazok > limit).nonzero()
npobrazok[x, y] = 0
#a[a > limit] = 0

# zobraz/uloz vysledok
novy = Image.fromarray(npobrazok, 'L')
novy.show()
#novy.save('vysledok.png')

