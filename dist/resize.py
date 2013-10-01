import glob
from exceptions import IOError
import PIL.Image, PIL.ImageFile

for infile in glob.glob("*.jpg"):
    img = PIL.Image.open(infile)
    if infile[0:4] != "small":
        destination = "" + infile
        try:
            img.save(destination, "JPEG", quality=1, optimize=False, progressive=True)
        except IOError:
            PIL.ImageFile.MAXBLOCK = img.size[0] * img.size[1]
            img.save(destination, "JPEG", quality=1, optimize=False, progressive=True)
        print "done " + infile

