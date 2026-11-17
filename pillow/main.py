import os, sys
from PIL import Image

for infile in sys.argv[1:]: # prend l'argument et l'affect a infile
    f, e = os.path.splitext(infile) # separe le /chemin/fichier du forma (.jpg)
    outfile = f + ".jpg"
    if infile != outfile: # verifie si le nom originel est comme le nouveau
        try:
            with Image.open(infile) as im:
                im.save(outfile)    # sauvegare le nouveau fichier
        except OSError:
            print("cannot convert", infile)
