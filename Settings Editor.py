import platform
import os


print "Welcome to the APOD Wallpaper Settings Editor\n"
print "Opening Settings"    
f = open("settings.txt", "w")
print "Settings file open"
platformv =  platform.release()
jbmp = 0
if platformv>=7:
    jbmp =1
    print "Windows 7+ is detected, using JPG file format\n"
else:
    jbmp=0
    print "Windows Vista or below is detected, using BMP file format\n"
print "Change settings in the settings.txt\n"
location = os.getcwd()
print "Current Directory: " + location
print "Enter location on harddrive to store images, or leave blank to save in current directory\n"
tmplocation =raw_input()
if tmplocation != "":
    location = tmplocation
print "Images will be saved to " + location + "\n"
print "Random image/todays image, type r or t"
rantod = 't'
rantod = raw_input()
size=0
if rantod == 'r':
     print "A random image will be found, do you wish to set the minimum picture size in mb, 0 for any size"
     size = raw_input()
     if size == '':
         size=0
     print "You selected " + str(size) + "mb minimum for your pictures"
     size = int(size)
else:
    rantod = 't'
    print "You have opted to get the newest photos"
print "You can use time.sleep() to download new photos, or use the Windows task sheduler... If you want to use time.sleep, time out the time in hours, or use n"
sleeper = raw_input()
secondsleeper='n'

if sleeper == '':
    secondsleeper = 'n'
else:
    secondsleeper = sleeper
    
    
bsize = size*1048576;
print bsize
f = open("settings.txt","w")
f.write("Settings are one per line in the following order: Bmp=0,jpg=1; Storage location; (r)andom or (t)odays image; minimum image size in mb, then bytes\n")     
f.write(str(jbmp)+"\n")
f.write(location + "\n")
f.write(rantod + "\n")
ssize = str(size)
f.write(ssize + "\n")
sbsize = str(bsize)
print sbsize
f.write(sbsize + "\n")
f.write(secondsleeper)
f.close()


