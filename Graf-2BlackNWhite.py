import Image
import numpy as np

pic = Image.open('monalisa.png')
width, height = pic.size

a = np.array(pic)

# z pola 640x430 spravi viac poli po 3 elementoch (nechapem preco to vie ze 3, sak tam je minus 1)
# a to by malo spravit 1d vektor
rgb = a.reshape((width*height), -1)
# vynasobi kazdy element (teraz je to xpoli po 3 elementy) takym cislom aby to bolo ciernobiele
intensity = np.array(0.2989*rgb[:, 0] + 0.5870*rgb[:, 1] + 0.1140*rgb[:, 2], dtype=np.uint8)
# tu sa to naspat upravi na x*y , aby z toho bol 2d obrazok
pic2 = Image.fromarray(intensity.reshape((height, width)), 'L')
pic2.save('Graf-2mona.png')
