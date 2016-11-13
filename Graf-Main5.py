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

obrazok = Image.open('monalisa.jpg')
obrazok2 = obrazok.convert('L')

maska_r = 1

maska = [[1.0/((2*maska_r+1)*(2*maska_r+1))]*(2*maska_r+1) for i in range(2*maska_r+1)]

print(maska)

maska_gauss = [
    [1/16, 1/8, 1/16],
    [1/8,1/4,1/8],
    [1/16,1/8,1/16]
]

rozostreny = obrazok2.convert('L')
rozostreny = apply_mask(rozostreny, maska_r, maska_gauss)
rozostreny.save('monagauss.png')

Image.blend(rozostreny, obrazok2, 0.5).save('scitanie5.jpg')
sirka, vyska = rozostreny.size
for y in range(0, vyska):
    for x in range(0, sirka):
        print("neche sa mi!")
