import wget
from os import remove
import tkinter
import tkinter.ttk

##Fonction de verification de la version installée et de recherche de mises à jour
def trouverMAJ():
    global label
    with open(file="version.txt",mode='r') as versionActuelle:
        versioninstallee = versionActuelle.read()
        wget.download('https://jrucvl.github.io/CAPalgorythm/version.txt', 'server-version.txt')
        with open(file="version.txt", mode="r") as versionServer:
            derniereversion = versionServer.read()
            if derniereversion == versioninstallee:
                remove(path='server-version.txt')
                quit()
            else:
                label = tkinter.Label(iug, text = "Mise à jour...")
                remove(path = 'main.py')
                wget.download("https://jrucvl.github.io/CAPalgorythm/main.py", 'main.py')
                with open(file='version.txt', mode = "w") as version:
                    version.writelines(derniereversion)
                    version.close()
                    remove("logo.png")
                wget.download("https://jrucvl.github.io/CAPalgorythm/logo.png", 'logo.png')
    remove(path='server-version.txt')
    quit()


iug = tkinter.Tk()
label = tkinter.Label(iug, text = "Vérification des mises à jours...")
progbar = tkinter.ttk.Progressbar(iug, mode="indeterminate", length=500)
label.pack()
progbar.start()
trouverMAJ()
progbar.stop()
progbar.pack()
iug.mainloop()