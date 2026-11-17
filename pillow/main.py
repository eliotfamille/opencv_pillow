import os, sys
from PIL import Image

def roll(im: Image.Image, delta: int) -> Image.Image:   # return une image
    xsize, ysize = im.size  #taille de l'image

    delta = delta % xsize   # decoupe l'image selon delta
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    #   cree une taille en additionnant les 2 image
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    # y colle les deux image
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
            #roll(im,50).save("roll.jpg")    # sauvegarde l'image roll
            merge(im,im).save("merge.jpg") # sauvegarde l'image merge

    except OSError:
        pass
