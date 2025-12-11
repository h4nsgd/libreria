#Metodos utiles para manejar archivos

import os
from os import listdir, chdir
from os.path import isfile, join
# import eyed3 as e3
import shutil
import subprocess as sp
from pathlib import Path

def renameFiles(mypath):
    chdir(mypath)

    for i in [
            f for f in listdir(mypath)
            if (isfile(join(mypath, f)) and (".jpg" in f))
    ]:
        #audio = e3.load(i)
        #new = f"{audio.tag.track_num[0]:02d} - "+i
        new = "x"
        try:
            #os.rename(i,new)
            pass
        except PermissionError:
            print("Error de permiso: " + i)
        #print(f"{i:40s} -> {new}")
        print('"' + i + '",')


def reduceTo1k(mypath):
    chdir(mypath)
    for i in [f for f in listdir(mypath) if isfile(join(mypath, f))]:
        os.system(f"ffmpeg -i {i} -vf scale='1024:-1' {i[:-4]}-1k.jpg")


def convertTo128kbps(mypath):
    #Convierte todos los .mp3 y .flac dentro de "mypath" a 128kbps y los
    #guarda en una carpeta "128kbps" debajo de "mypath" conservando el arbol de archivos.

    newFolder = "128kbps"

    for i in [f for f in os.walk(mypath)]:
        path = i[0]
        newPath = path[:len(mypath)] + os.sep + newFolder + path[len(mypath):]
        try:
            os.mkdir(newPath)
        except FileExistsError:
            print(f"'{newFolder}' ya existe")
        for j in i[2]:
            file = join(path, j)
            if isfile(file):
                if (".mp3" in j) or (".flac" in j):
                    newFile = join(newPath, Path(j).stem+".mp3")
                    os.system(
                        f'ffmpeg -i "{file}" -codec:a libmp3lame -loglevel error -b:a 128k "{newFile}"'
                    )
                    print(f"Converted to\t{newFile}")
                # elif ".flac" in j:
                #     pass
                        # print(f"Converting \t{file}")
                        # os.system(
                        #     f'ffmpeg -y -i "{file}" -codec:a libmp3lame -b:a 128k -q:a 0 -map_metadata 0 -id3v2_version 3 -write_id3v1 1 "{newFile}"'
                        #     # f'ffmpeg -i "{file}" -codec:a libmp3lame -loglevel error -b:a 128k "{newFile}"'
                        # )
                        # print(f"Converted to\t{newFile}")
                        # return
                if (".jpg" in j) or (".png" in j) or (".jpeg" in j):
                    newFile = join(newPath, j)
                    shutil.copy(file.strip(), newFile.strip())
                    print(f"Copied to\t\t{newFile}")


def deleteUrlCover(mypath):
    for i in [f for f in os.walk(mypath)]:
        print(f"{i[0]}\n")
        for j in i[2]:
            if (".url" in j) or (j == "cover.jpg"):
                deleted = join(i[0], j)
                cmd = f'del "{deleted}"'
                print(f"Deleted: {j}")
                os.system(cmd)
        print("\n")


def pngjpg2jpg(mypath):
    chdir(mypath)
    c = 90
    for i in [
            f for f in listdir(mypath) if (isfile(join(mypath, f)) and (
                (".bmp" in f) or (".jpg" in f) or (".png" in f)))
    ]:
        os.system(f'ffmpeg -i "{i}" -loglevel error "{c}.jpg"')
        #os.system(f'ffmpeg -i "{i}" -loglevel error "{i[:-4]}-r.jpg"')
        print(i)
        c += 1

def encodeToWebp(mypath):
    chdir(mypath)
    c = 90
    for i in [
            f for f in listdir(mypath) if (isfile(join(mypath, f)) and (
                (".bmp" in f) or (".jpg" in f) or (".png" in f) or (".jpeg" in f)))
    ]:
        os.system(f'ffmpeg -i "{i}" -loglevel error -c:v libwebp "{Path(i).stem}.webp"')
        #os.system(f'ffmpeg -i "{i}" -loglevel error "{i[:-4]}-r.jpg"')
        print(i)
        c += 1

def unrarAll(mypath):
    pwrd = "oldmusic"
    pwrd = "www.discografiasmega.com"
    pwrd = "www.discogc.com"
    pwrd = "www.discografiascompletas.net"
    pwrd = "www.metalminos.net"

    chdir(mypath)
    for i in [
            f for f in listdir(mypath)
            if isfile(join(mypath, f)) and ".rar" in f
    ]:
        os.system(f'rar x -p{pwrd} "{i}"')


def deleteFolder(mypath):
    pass


def tile2Pictures(mypath,names):
    chdir(mypath)
    for a, b in names:
        cmd = f"ffmpeg -i {a}.jpg -i {b}.jpg -loglevel error -filter_complex hstack=inputs=2 {a}-{b}.jpg"
        print(f"{a}-{b}.jpg")
        os.system(cmd)
    pass

def name(path):
    for i in [f for f in os.walk(path)]:
        for c in i[2]:
            if ".mp3" in c:
                print(c)

def crop(mypath):
    chdir(mypath)
    c = 146220
    for i in [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ((".bmp" in f) or (".jpg" in f) or (".png" in f)))]:
        os.system(f'ffmpeg -i "{i}" -vf crop=1919:1080:241:0 "{c}.jpg"')
        #os.system(f'ffmpeg -i "{i}" -loglevel error "{i[:-4]}-r.jpg"')
        print(i)
        c += 1

def main():
    # renameFiles(r"")
    # pngjpg2jpg(r"C:\Users\Hans\Pictures\Screenshots")
    # unrarAll(r"E:\hello rar")
    # deleteUrlCover(r"E:\Nirvana")
    # tile2Pictures(r"G:\Mi unidad\LL\spam",[
    #         ("1", "2"),
    #     ("3", "4"),
    #     ("5", "6"),
    #     ("7", "8"),
    #     ])
    convertTo128kbps(r"C:\Users\mig_1\Music\Radiohead2-final")
    # encodeToWebp(r"C:\Users\hansg\Documents\git\interglick\public\img\home")
    # print("Terminado")
    # name(r"C:\Users\Hans\Music\LL\虹ヶ咲学園スクールアイドル同好会")
    # crop(r"G:\Mi unidad\LL\spam")

if __name__=="__main__":
    main()
