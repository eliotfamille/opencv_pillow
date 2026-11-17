from PIL import Image

im = Image.open("hello.png")    # image dans la dossier
print(im.format, im.size, im.mode)  # information
im.show()   # affiche l'image
