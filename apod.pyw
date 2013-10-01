import os
import Image
import PIL
from exceptions import IOError
import Image
import platform
import urllib2
import urllib
from bs4 import BeautifulSoup
import datetime
import random
import time
import ctypes


rantod = ''
location = ''

def randurl():
    now = datetime.datetime.now()
    today = now.strftime("%y%m%d")
    randdate = randomDate("000101", today, random.random())
    randomurl = "http://apod.nasa.gov/apod/ap" + randdate + ".html"
    return randomurl

def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%y%m%d', prop)

def download(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    fi = open("url.jpg", 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        fi.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    fi.close()

def filesize(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open("url.jpg", 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    return file_size

    
def runProgram():
    try:
        todayurl = "http://apod.nasa.gov/apod/astropix.html"

        if rantod == 'r':
            useurl = randurl()
        else:
            useurl = todayurl

        url = urllib.urlopen(useurl)
        print url
        soup = BeautifulSoup(url)
        center = soup.center
        center.a.decompose()
        link = center.a
        link = link.get('href')
        link = "http://apod.nasa.gov/apod/" + link
        print link

        if rantod == 'r':
            while int(bsize)>filesize(link):
                if rantod == 'r':
                    useurl = randurl()
                else:
                    useurl = todayurl

                url = urllib.urlopen(useurl)
                print url
                soup = BeautifulSoup(url)
                center = soup.center
                center.a.decompose()
                link = center.a
                link = link.get('href')
                link = "http://apod.nasa.gov/apod/" + link
                print link

        os.chdir(location)
        download(link)
        
        if jbmp=='1':
            bgdir = location + "\\url.jpg"        
        else:
            img = PIL.Image.open("url.jpg")
            img.save("image.bmp", "bmp")
            bgdir = location + "\\image.bmp"


        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, bgdir, 3)
        return True
    except AttributeError:
        return False

version = "Version 0.0.1"
print version
cwd = os.getcwd()

fz = open("settings.txt",'r').read().split('\n')


jbmp = fz[1]
location = fz[2]

rantod = fz[3]
size = fz[4]
bsize = fz[5]
sleepingseconds = fz[6]
if sleepingseconds != 'n':
    sleepingseconds = float(sleepingseconds)
print "Jpg=1; BMP=0, Set to " + jbmp
print "Save location: " + location
print "(r)andom or (t)odays image: " + rantod
print "Minimum image size: " + size + "MB"
print "Minimum image size: " + bsize + " bytes"
print "If using python sleep, time will be " + str(sleepingseconds)


if sleepingseconds == 'n':
    print runProgram()
else:
    while(1):
        print runProgram()
        time.sleep(sleepingseconds)
