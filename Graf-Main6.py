import Image
import numpy as np

image = Image.open("monalisa.png")
image2 = image.convert('L')

sirka, vyska = image2.size

maska_r = 2
#rozostrenie
maska = ((1, 4, 7, 4 , 1),(4, 16, 26, 16, 4),(7, 26, 41, 26, 7),(4, 16, 26, 16, 4),(1, 4, 7, 4, 1))


novy = Image.new('L', (sirka, vyska))
novy2 = Image.new('L', (sirka, vyska))

for y in range(0,vyska):
    for x in range(0,sirka):
        sum = 0
        for t in range(-maska_r,(maska_r+1)):
            if y+t >= 0 and y+t < vyska:
                for s in range(-maska_r,(maska_r+1)):
                    if x+s >= 0 and x+s < sirka:
                        sum += image2.getpixel((x+s,y+t))*maska[s][t]

        novy.putpixel((x,y), int(sum/273))

#povodny ciernobiely obrazok
image2.save('Graf-Main6mona1.png')
#rozostreny obrazok
novy.save('Graf-Main6mona2.png')

for y in range(0,vyska):
    for x in range(0,sirka):
        novy2.putpixel((x,y), int(image2.getpixel((x,y)) + (image2.getpixel((x,y))-novy.getpixel((x,y)))))

#zaostreny obrazok
novy2.save('Graf-Main6mona3.png')

