#!/usr/bin/python
#-*-coding: UTF8-*-

#By BDeliers
#http://bdeliers.com
#http://github.com/BDeliers/

#CHANGELOG:
#1.0 = initial version
#1.0.1 = added alert for empty title

from tkinter import *
from tkinter import messagebox

class Interface:
    def __init__(self):

        fenetre=Tk()
        fenetre.title("HTMLGenerator")
        #fenetre.geometry("400x345")
        #fenetre.iconbitmap("./icon.ico")
        FrameH=Frame(fenetre)
        FrameB=Frame(fenetre)
        header=IntVar()
        footer=IntVar()
        actions=Actions()

        # Frame H

        LabelCreateur=Label(FrameH, text="Author")
        EntryCreateur=Entry(FrameH, width=40)
        EntryCreateur.insert(0,"Mr Smith")

        LabelTitre=Label(FrameH, text="Title")
        EntryTitre=Entry(FrameH, width=40)
        EntryTitre.insert(0,"Index")

        LabelCss=Label(FrameH, text="CSS's path")
        EntryCss=Entry(FrameH, width=40)
        EntryCss.insert(0,"./style/style.css")

        LabelScript=Label(FrameH, text="Script's path")
        EntryScript=Entry(FrameH, width=40)
        EntryScript.insert(0,"./script/script.js")

        LabelFav=Label(FrameH, text="Favicon's path")
        EntryFav=Entry(FrameH, width=40)
        EntryFav.insert(0,"./img/fav.png")

        LabelComm=Label(FrameH, text="Comment")
        TextComm=Text(FrameH, height=5, width=30)

        CheckHeader=Checkbutton(FrameH, text="Header", variable=header)
        CheckFooter=Checkbutton(FrameH, text="Footer", variable=footer)

        LabelSections=Label(FrameH, text="Number of sections")
        SpinSections=Spinbox(FrameH, from_=0, to=10)
        SpinSections.delete(0, last=END)
        SpinSections.insert(0, 0)

        LabelFichier=Label(FrameH, text="File's title")
        EntryFichier=Entry(FrameH, width=40)
        EntryFichier.insert(0,"index")

        # Referencement

        entry=[EntryCreateur, EntryTitre, EntryCss, EntryScript, EntryFav, EntryFichier]
        check=[CheckHeader, CheckFooter]
        spin=[SpinSections]
        txt=[TextComm]

        # Frame B

        def vider_btn():
            actions.vider(entry, check, spin, txt)
        def valider_btn():
            actions.valider(entry, [header, footer], spin, txt)

        BtnValider=Button(FrameB, text="Proceed", comman=valider_btn)
        BtnVider=Button(FrameB, text="Empty", command=vider_btn)

        # Grider

        FrameH.grid(row=0, column=0, padx=20, pady=(10,20))
        FrameB.grid(row=1, column=0, padx=20, pady=(0,10))

        LabelCreateur.grid(row=0, column=0, sticky=W)
        EntryCreateur.grid(row=0, column=1, pady =2)

        LabelTitre.grid(row=1, column=0, sticky=W)
        EntryTitre.grid(row=1, column=1, pady =2)

        LabelCss.grid(row=2, column=0, sticky=W)
        EntryCss.grid(row=2, column=1, pady =2)

        LabelScript.grid(row=3, column=0, sticky=W)
        EntryScript.grid(row=3, column=1, pady =2)

        LabelFav.grid(row=4, column=0, sticky=W)
        EntryFav.grid(row=4, column=1, pady =2)

        LabelComm.grid(row=5, column=0, sticky=W)
        TextComm.grid(row=5, column=1, pady =2)

        LabelFichier.grid(row=6, column=0, sticky=W)
        EntryFichier.grid(row=6, column=1)

        CheckHeader.grid(row=7, column=0)
        CheckFooter.grid(row=7, column=1)

        LabelSections.grid(row=8, column=0, sticky=W)
        SpinSections.grid(row=8, column=1)

        BtnValider.grid(row=0, column=1, padx=3)
        BtnVider.grid(row=0, column=0, padx=3)

class Actions:      
    def vider(self, entry, check, spin, txt):
        # Vide tous les champs
        for entry in entry:
            entry.delete(0,last=END)
        for check in check:
            check.deselect()
        for spin in spin:
            spin.delete(0, last=END)
            spin.insert(0, 0)
        for txt in txt:
            txt.delete(0.0, END)

    def recup(self, entry, check, spin, txt):
        valEntry=[]
        valCheck=[]
        valSpin=[]
        valTxt=[]
        for entry in entry:
            valEntry.append(entry.get())
        for check in check:
            valCheck.append(int(check.get()))
        for spin in spin:
            valSpin.append(int(spin.get()))
        for txt in txt:
            valTxt.append(txt.get(0.0, END).replace('\n', '')) 
        valeurs=[valEntry, valCheck, valSpin, valTxt]
        return valeurs
    
    def valider(self, entry, check, spin, txt):
        # Traitement des données
        valeurs=self.recup(entry, check, spin, txt)
        entry=valeurs[0]
        check=valeurs[1]
        spin=valeurs[2]
        txt=valeurs[3]
        sections=""

        if check[0]==1:
            header="        <header>\n\n        </header>"
        else:
            header=""
        if check[1]==1:
            footer="        <footer>\n\n        </footer>"
        else:
            footer=""
        for i in range(0,spin[0]):
            sections=sections+"        <section>\n\n        </section>\n"

        ligne1='<!--By '+entry[0]+'-->\n'
        ligne2='<!--'+txt[0]+'-->\n'
        ligne3='<!DOCTYPE html>\n'
        ligne4='<html lang="fr">\n'
        ligne5='    <head>\n'
        ligne6='        <title>'+entry[1]+'</title>\n'
        ligne7='        <link rel="stylesheet" type="text/css" href="'+entry[2]+'" />\n'
        ligne8='        <script type="text/javascript" src="'+entry[3]+'"></script>\n'
        ligne9='        <link rel="icon" type="image/png" href="'+entry[4]+'" />\n'
        ligne10='    </head>\n'
        ligne11='    <body>\n'
        ligne12=header+'\n'
        ligne13=sections+'\n'
        ligne14=footer+'\n'
        ligne15='    </body>\n'
        ligne16='</html>\n'

        if entry[5]!='':
            fichier=open(entry[5]+'.html', "w")
        
            for i in range(1,17):
                ligne=eval('ligne'+str(i))
                fichier.write(ligne)

            fichier.close()
            messagebox.showinfo('Done !', 'The file '+entry[5]+'.html was created !')
        else:
            messagebox.showerror('Error','Please name your file !')
            
# Programme Principal

interface = Interface()
mainloop()
