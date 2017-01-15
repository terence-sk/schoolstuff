import Image
import numpy as np

image = Image.open("monalisa.png")
image2 = image.convert('L')

sirka, vyska = image2.size

maska_r = 1
#laplacian
maska = ((0, 1, 0),(1, -4, 1),(0, 1, 0))
maska2 = ((1/9, 1/9, 1/9),(1/9, 1/9, 1/9),(1/9, 1/9, 1/9))


novy = Image.new('L', (sirka, vyska))
novy2 = Image.new('L', (sirka, vyska))

for y in range(0,vyska):
    for x in range(0,sirka):
        sum = 0
        sum2=0
        for t in range(-maska_r,(maska_r+1)):
            if y+t >= 0 and y+t < vyska:
                for s in range(-maska_r,(maska_r+1)):
                    if x+s >= 0 and x+s < sirka:
                        sum += image2.getpixel((x+s,y+t))*maska[s][t]
                        sum2 += image2.getpixel((x+s,y+t))*maska2[s][t]

        novy.putpixel((x,y), int(sum))
        novy2.putpixel((x,y), int(sum2))


image2.save('Graf-Main7mona1.png')
novy.save('Graf-Main7mona2.png')
novy2.save('Graf-Main7mona3.png')

for y in range(0,vyska):
    for x in range(0,sirka):
        novy2.putpixel((x,y), int(image2.getpixel((x,y)) + (image2.getpixel((x,y))-novy.getpixel((x,y)))))

#zaostreny obrazok
novy2.save('mona5.png')

