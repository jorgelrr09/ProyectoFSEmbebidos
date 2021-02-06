#!/usr/bin/env python
#
# Fundamentos de Sistemas Embebdios - UNAM, FI, 2021-1
# Proyecto Final: Centro Multimedia
#
#Integrantes: Arias Pelayo Thomas.A, Monterrubio López Charlie R.,Jorge Luis Rivas Rodríguez
# Instructiones:
# Correr el código y poner el path correcto de los archivos en líneas 76-80
# Correr el código cada vez que se quiere seleccionar una nueva opción

import vlc
import time
import glob
import webbrowser

tiempoPorSlide = 4
def reproducirFotos(mymedia,tiempo):
#instancia del reproductor
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_list_player_new()#funcion para hacer slideshow
    Media = vlc_instance.media_list_new(mymedia)
    player.set_media_list(Media)

#cada elemento de la lista se reproduce en pantalla por 4 segundos
    for index, name in enumerate(mymedia):
        player.play_item_at_index(index)
        time.sleep(tiempo)#el tiempo de reproduccion de las fotos, videos o musica
#Media.close()#IMPORTANTE, debe cerrarse el reproductor

def reproducirMusicaVideo(file):
    while True:
        for f in file:
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new(f)
            player.set_media(media)
            player.play()
            time.sleep(1.5)
            duration = player.get_length() / 1000
            time.sleep(duration)
            player.stop()
    player.close()

def reproducirUSB():
    #se guardan los nombres de los archivos tipo png en una lista
    varPhotoFiles = glob.glob("Fotos/*.png")#En carpeta fotos
    #se guardan los nombres de los archivos tipo mp4 en una lista
    varVideoFiles = glob.glob("Videos/*.mp4")#EN carpeta videos
    #se guardan los nombres de los archivos tipo mp3 en una lista
    varMusicFiles = glob.glob("Musica/*.mp3")#EN carpeta musica
    
    if (varPhotoFiles and varVideoFiles) or (varPhotoFiles and varMusicFiles) or (varVideoFiles and varMusicFiles) :
        print("Elige que reproducir:\n1.-Fotos\n2.-Videos\n3.-Musica")
        opcionReproduccion = input()		
        if opcionReproduccion == '1':
            print(varPhotoFiles)
            reproducirFotos(varPhotoFiles,tiempoPorSlide)
        elif opcionReproduccion == '2':
            print(len(varVideoFiles))
            reproducirMusicaVideo(varVideoFiles)	
        elif opcionReproduccion == '3':
        #es olbigatorio poner un indice al llamar la funcion
            #for x in range(len(varMusicFiles)):
                #reproducirMusicaVideo(varMusicFiles[x])
            reproducirMusicaVideo(varMusicFiles)	
    elif not varVideoFiles and not varMusicFiles:#si no hay archivos de video se cargan fotos
        reproducirFotos(varPhotoFiles,tiempoPorSlide)
    elif not varPhotoFiles and not varMusicFiles:#si no hay archivos de fotos ni musica se cargan videos
        reproducirMusicaVideo(varVideoFiles[0])
    elif not varPhotoFiles and not varVideoFiles:#si no hay archivos de fotos ni musica se cargan videos
        reproducirMusicaVideo(varMusicFiles[0])

print("1.- Ver servicio de video online(Netlfix). \n2.- Reproducir musica(Spotify). \n3.- Reproducir contenido en USB")
opcion = input()
if opcion == '3':
    reproducirUSB()
elif opcion == '1':
    webbrowser.open("https://www.netflix.com/browse",new=2, autoraise=True)
elif opcion == '2':
    webbrowser.open("https://www.spotify.com/mx/",new=2, autoraise=True)
else:
    print("Slecciona una opción valida")
    print(opcion)


