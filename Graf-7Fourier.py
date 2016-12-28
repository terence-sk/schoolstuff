from PIL import Image
import cmath

origin = Image.open('typek.jpg')
blackwhite = origin.convert('L')


width, height = blackwhite.size

vys = [[0]*height]*height

for u in range(0, height):
    sum = 0
    for x in range(0, height):
        sum += blackwhite.getpixel((u, x)) * cmath.e ** ((-2j * cmath.pi * u * x)/height)
    vys[u] = sum
    print(sum)

# im2 = Image.new('L', (height, height))
#
# for x in range(0, height):
#     for y in range(0, height):
#         im2.putpixel((x, y), int(vys[x][y]))
#
# im2.save("Graf-7vystup.jpg")
