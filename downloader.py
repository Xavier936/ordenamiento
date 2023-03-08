import os
import subprocess
import pytube

url = input("URL: ")

yt = pytube.YouTube(url)

vids = yt.streams.filter(file_extension= 'mp4')
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Ingrese vid num: "))

parent_dir = r"/home/alexis/Documentos/alexis/Python_Ejercicios/videos"
vids[vnum].download(parent_dir)


default_filename = vids[vnum].default_filename


print('done')



