from pydub import AudioSegment
 
video = "/home/alexis/Documentos/alexis/Python_Ejercicios/videos/mix_tonadas.mp4"
audioname = input('Ingrese el nombre de la cancion con extension: ')
AudioSegment.from_file(video).export('/home/alexis/Documentos/alexis/Python_Ejercicios/mp3/{audioname}'.format(audioname = audioname), format='mp3')
print('Done!!')