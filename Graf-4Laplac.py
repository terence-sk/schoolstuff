from PIL import Image


def apply_mask(input_pic, maska_r, maska):
    sirka, vyska = input_pic.size
    novy = Image.new('L', (sirka, vyska))
    for y in range(0, vyska):
        for x in range(0, sirka):
            suma = 0
            for t in range(-maska_r, maska_r+1):
                if 0 <= y+t < vyska:
                    for s in range(-maska_r, maska_r+1):
                        if 0 <= x+s < sirka:
                            suma += input_pic.getpixel((x + s, y + t)) * maska[s][t]
            novy.putpixel((x, y), int(suma))
    return novy

obrazok = Image.open('monalisa.png')
obrazok2 = obrazok.convert('L')

maska_r = 1

maska = [[1.0/((2*maska_r+1)*(2*maska_r+1))]*(2*maska_r+1) for i in range(2*maska_r+1)]

print(maska)

maska_laplac = [
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
]

obrazok_laplac = obrazok2.convert('L')
obrazok_laplac = apply_mask(obrazok_laplac, maska_r, maska_laplac)
obrazok2 = apply_mask(obrazok2, maska_r, maska)
obrazok_laplac.save('Graf-4mona1.png')
obrazok2.save('Graf-4mona2.png')

Image.blend(obrazok_laplac,obrazok2,0.5).save('Graf-4mona3.png')
