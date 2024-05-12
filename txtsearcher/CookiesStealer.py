import os
from os.path import isfile, join
import shutil


def makeBatFile(src, dst):
    with open(f"{src}/GoToFolder.bat", "w") as f:
        f.write("@ECHO OFF\n"
                f"explorer.exe /root,{dst}")


path = "./"
allFolders = os.listdir(path)

searchFor = input("Czego szukamy: ")

filename = input("Nazwa folder: ")

kutasek = open(filename + ".txt", "w", encoding="utf-8")
ilosc = 0

os.mkdir(f"./{filename}")
for folder in allFolders:
    print(f"\rIlość pasujących: {ilosc}", end="")
    niga = path + folder + "/Cookies"
    if os.path.exists(niga):

        files = [f for f in os.listdir(niga) if isfile(join(niga, f))]
        for file in files:
            with open(niga + "/" + file, "r", encoding="utf-8") as f:
                chuj = f.read()
                if searchFor in chuj:
                    if not os.path.exists(f"./{filename}/{ilosc}"):
                        os.mkdir(f"./{filename}/{ilosc}")
                    makeBatFile(f"./{filename}/{ilosc}", os.path.abspath(niga).split("\Cookies")[0])
                    with open(f"./{filename}/{ilosc}/{f.name.split('./')[1].split(' ')[1].split('/Cookies/')[1]}", "a+",
                              encoding="utf-8") as ss:
                        ss.write(chuj)
                    ilosc += 1

kutasek.close()