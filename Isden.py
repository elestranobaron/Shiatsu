
# -*- coding: utf-8 -*-
from Tkinter import*
from tkentrycomplete import *
import gadfly
import os
import inspect
import threading
import Pmw
import time
import inspect
import subprocess as sp
import Tkinter as tk
import sys
import shutil
import tarfile
def Save():  
    class BackUp(object):
        def __init__(self):
            self.source = os.path.join(os.path.dirname(__file__), "..", "shiatsu")#"/dossier/source"
            self.target = os.path.join(os.path.dirname(__file__), "..", "Sauvegardeshiatsu")#"/dossier/destination"
            if os.path.isdir(self.source):
                fld_name = self.get_target_name()
                print fld_name
                self.save_archiv(fld_name)

        def get_target_name(self):
            tl = time.localtime()
            return "save_%s-%s_%s-%s-%s.tar.gz" % (tl.tm_hour, tl.tm_min, 
                                                                     tl.tm_year, tl.tm_mon, tl.tm_mday)

        def save_archiv(self, fld):
            target = os.path.join(self.target, fld)
            if os.path.isdir(target):
                print "Un dossier du même nom existe déjà"
                return
            os.chdir(os.path.dirname(self.source))
            tar = tarfile.open(target, "w:gz")
            tar.add(os.path.basename(self.source))
            tar.close()

            
    if __name__ == "__main__":
        bckp = BackUp()
        print "Done"
KONTEUR = 0
tetra=-1
chaines = ""
radiTest = 0 ##bad window path name
antiBoutonDoublon = 0
thunder = 0
pr = 0
su = -1
enreMod=0
__file__ = inspect.currentframe().f_code.co_filename
### MALGRE LE IF NOT...
try:
    if  not os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "Sauvegardeshiatsu")):
        os.mkdir(os.path.join(os.path.dirname(__file__), "..", "Sauvegardeshiatsu"))
except:# WindowsError:
        pass
if  not os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients","rsdetails")):
    try:
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu"))
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients"))
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients", "Suivis"))
                    open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients","clients"),"w") 

    except:# WindowsError:
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients"))
    open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients","rsdetails"),"w")
if not os.path.isfile(os.path.join(os.path.dirname(__file__),"..", "shiatsu", "Clients","rsdetails2")):
    open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients","rsdetails2"),"w")
symbolsfile = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients", "clients"),'r')
symbols = []
try:
    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients", "Suivis"))
except:# WindowsError:
    pass
for line in symbolsfile.readlines():
    symbols.append(line.strip())
#GUI
win=Tk()
win.title('Bases de données')
win.configure(background = 'royal blue')

Frame(win,width=50,height=150).pack()#wid 200 hei 150

temps = time.strftime('%y%m%d', time.localtime())
kems = time.strftime('%d%m%y', time.localtime())  


def go():
    #print entry
    a = combo.get()
    print a
    filename = "%s" % a#os.system("a")#"tmp%d" % os.getpid()
    #fichier = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients", a+".docx"),'w')
    global enreMod
    no = a#"OKok"
    txt = no
    enreMod = 0
    def majuscule(car):
       "renvoie <vrai> si car est une majuscule"
       if car >= "A" and car <= "Z":
          return 1
       else:
          return 0
    print 'hello'
    def minuscule(car):
       "renvoie <vrai> si car est une minuscule"
       if car >= "a" and car <= "z":
          return 1
       else:
          return 0
    def alphab(car):
       "renvoie <vrai> si car est un caractère alphabétique"
       if majuscule(car) or minuscule(car):
          return 1
       else:
          return 0
    print 'hello'
    def chaineListe(ch):
       "convertit la chaîne ch en une liste de mots"
       liste, ct = [], "" # ct est une chaîne temporaire
       for c in ch:
          if c == " ":
             liste.append(ct) # ajouter la ch. temporaire à la liste
             ct = "" # ré-initialiser la ch. temporaire
          else:
             ct = ct + c
       if ct != "":
          liste.append(ct) # ne pas oublier le dernier mot
       return liste
    # Test :
    print 'hello'
    print chaineListe("Une hirondelle ne fait pas le printemps")
    print chaineListe("")
    c = 0 
    #txt = "Le nom de ce Monsieur est Alphonse"
    lst = chaineListe(txt) # convertir la phrase en une liste de mots
    for mot in lst: # analyser chacun des mots de la liste
       while majuscule(mot[c]): # tester le premier caractère du mot WHILE plutot que IF sinon ct que les deux premiers
          c = c+1
          print mot[0:c+1]
          name = mot[0:c]# jusqu-a c et non pas c+1
          surname = mot[c:]#idem
    fen1 = Toplevel() # instead of Tk()
    fen1.title(no) # je me trompe je met = il me detecte pas d erreur #mais ca ne fonctionne pas
    fen1.config(bg='forest green')
    # création de widgets 'Label' et 'Entry' :
    txt1 = Label(fen1, text ='Sexe :')
    txt2 = Label(fen1, text ='Date de naissance :')
    txt3 = Label(fen1, text ='Adresse (N° et rue) :')
    txt4 = Label(fen1, text ='Code Postal :')
    txt5 = Label(fen1, text ='Localité :')
    txt6 = Label(fen1, text ='Téléphone :')
    txt7 = Label(fen1, text ='Signe(s) Particulier(s) :')
    entr1 = Entry(fen1)
    entr2 = Entry(fen1)
    entr3 = Entry(fen1)
    entr4 = Entry(fen1)
    entr5 = Entry(fen1)
    entr6 = Entry(fen1)
    entr7 = Entry(fen1)
    # création d'un widget 'Canvas' contenant une image bitmap :
    can1 = Canvas(fen1, width =160, height =160, bg ='white')
    photo = PhotoImage(file ='f.gif')#Martin_P.gif')
    item = can1.create_image(80, 80, image =photo)## c bon BUG DESORMAIS RAISON NON ENCORE SUE
    # Mise en page à l'aide de la méthode 'grid' :
    txt1.grid(row =1, sticky =E)
    txt2.grid(row =2, sticky =E)
    txt3.grid(row =3, sticky =E)
    txt4.grid(row =4, sticky =E)
    txt5.grid(row =5, sticky =E)
    txt6.grid(row =6, sticky =E)
    txt7.grid(row =7, sticky =E)
    entr1.grid(row =1, column =2)
    entr2.grid(row =2, column =2)
    entr3.grid(row =3, column =2)
    entr4.grid(row =4, column =2)
    entr5.grid(row =5, column =2)
    entr6.grid(row =6, column =2)
    entr7.grid(row =7, column =2)
    ##def filtrer(src, dst):##
    """Fonction de traitement."""
    src = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients", "rsdetails"),'r')
    #Lit et traite ligne par ligne le fichier source (src).
    #Le résultat est écrit au fur et à mesure dans le
    #fichier destination (dst). 
    """
    # Lit l'en-tête"""#finalement non"""
    """entete = src.readline().rstrip('\n\r')"""
    ##############################################""
    def traduire(ch):
        "convertir une ligne du fichier source en liste de données"
        dn = "" # chaîne temporaire pour extraire les données
        tt = [] # la liste à produire
        i = 0
        while i < len(ch):
            if ch[i] == "#":
                tt.append(dn) # on ajoute la donnée à la liste, et
                dn ="" # on réinitialise la chaine temporaire
            else:
                dn = dn + ch[i]
                i = i + 1
        return tt#return tt# cepaassage n est pas trop repéré par le programme
#####################################################"
    # Lit l'en-tête
    #ok = traduire(src.readlines())
    #print ok ces lignes transformaient src readlines en []
    global chaines
    #ligne = src.readline() RIEN QUE LE FAIT DE DEGAGER CETTE LIGNE CA REMARCHE COMME PAR MAGIE (1ERE LIGNE NON PRISE EN COMPTE)
    for ligne in src.readlines():####print src.readlines ou ca 
        #print ligne##### c la seule ligne qui fonctionne pour l'instant####### print utile et qui ralentit
        "convertir une ligne du fichier source en liste de données"
        dn = "" # chaîne temporaire pour extraire les données
        tt = [] # la liste à produire
        i = 0
        #try:
        #    print ligne.index('PYTHON')
        #except ValueError:
        #    pass#print 'ok'
        #print ligne[1:3]
        while i < len(ligne):
            if ligne[i] == "#":
                tt.append(dn) # on ajoute la donnée à la liste, et
                dn ="" # on réinitialise la chaine temporaire
            else:
                dn = dn + ligne[i]
            i = i + 1
        #print tt       ###############" print utile et qui ralentit
        # Affichage des données déjà présentes dans la liste :
        i = 0
        while i < len(tt):
        #    print tt[i],  ############### print utile et ?
            i = i +1
            c =0
            for mot in tt:
                try:
                    while majuscule (mot[c]):
                        c=c+1
                        #print mot[0:c] ####### print utile et qui ralentit 
                except IndexError:
                    #print mot[0:c]+"index"   ######## pareil
                    break
            if mot[0:c] == name and tt[1] == surname:## AND surname 
                ##entr2 = name+'coucou'## ## ( pas de doublons)
                txt8 = Label(fen1, text = name)
                txt8.grid(row=0, column = 3, sticky = 'N')
                txt10 = Label(fen1, text = tt[2])
                txt10.grid(row=2, column = 3, sticky = 'N')
                txt12 = Label(fen1, text = tt[3])
                txt12.grid(row=3, column = 3, sticky = 'N')
                txt14 = Label(fen1, text = tt[4])
                txt14.grid(row=4, column = 3, sticky = 'N')
                txt16 = Label(fen1, text = tt[5])
                txt16.grid(row=5, column = 3, sticky = 'N')
                txt18 = Label(fen1, text = tt[6])
                txt18.grid(row=6, column = 3, sticky = 'N')
                txt20 = Label(fen1, text = tt[7])
                txt20.grid(row=7, column = 3, sticky = 'N')
                def open_url(url):
                    pass #Open the url in a browser
                txt22 = Label(fen1, text = tt[8])
                #print tt[8]+"check"
                txt22.grid(row=8, column = 3, sticky = 'N')
                txt22.bind("<Button-1>",lambda e,url=tt[8]:open_url(tt[8]))
                global enreMod
                enreMod = enreMod +1
            else:
                #print mot [0:c] pareil pareil et pareil et enfin pareil.
                #print name
                #print 'coucou'
                txt9 = Label(fen1, text = surname)
                txt9.grid(row=1, column = 3, sticky = 'N')
            #print tt[1]########### va savoir pourquoi mais maintenant il me simplifie la vie avec ca, avant il ne selectionnait que les caracteres et non la chaine   ... !?
        try:
            if mot[0:c] == name and tt[1] == surname:        
                entr1.insert(END,tt[2])      # AJOUTS POUR MODIFICATION INSTANTAN2E
                entr2.insert(END,tt[3])
                entr3.insert(END,tt[4])
                entr4.insert(END,tt[5])
                entr5.insert(END,tt[6])
                entr6.insert(END,tt[7])
                entr7.insert(END,tt[8])     ###
                chaines = name + "#" + surname + "#"#tt[2] + "#" + tt[3] + "#" + tt[4] + "#" + tt[5] + "#" + tt[6] + "#" + tt[7] + "#" + tt[8] + "#"
                print chaines
        except IndexError:
            pass
    print 'infinity 3'
    global tetra
    tetra =-1
    KONTEUR=0
    def LePackage():
       bou.configure(state='disabled')
       print 'infinity 4'
       global chaines#chaine = r"c:\windows" #Texte à rechercher
       contenu = ""
       contenant=""
       chaines = name + "#" + surname + "#" #global KONT
       global KONTEUR
       KONTEUR=0
       global tetra
       tetra = -1
       KONT=0
       of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails2"),"r")#("mod.txt","r")
       for ligne in of:
           try:
               if not(chaines in ligne):## lN 144 RSDETAILS 41 252 RSDETAILS 41 261 RSDETAILS 42 327 RSDETAILS41
                   if tetra==1:
                       KONT=1
                       print "chaininligne"
                       contenu += ligne
                   else:
                       tetra=1#+tetra
                       contenu+=ligne
               else:
                   if KONT==1:
                       contenant+=ligne
                       tetra=1
                   else:
                       KONTEUR = KONTEUR +1
                       contenant+=ligne
                       print "notinligne"
                       tetra = 0#+tetra
                       print tetra
           except TypeError:
               print "GYUGYU"
               #tetra = 1
               pass
       of.close()
       print KONTEUR
       print tetra
       print "pak"
       if tetra == 0 and KONTEUR !=0:
           of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails"),'w')#('mod2.txt', 'w')
           of.write(contenu)
           of.close()#### dans cztte se quence de suppression des anciennes données  je ne sais pas les confusions qui peuvent etre provoquees
           of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails"),'a')#('mod2.txt', 'w')
           of.write(contenant)
           of.close()### SOLUTION ,?
       #elif tetra == 0 and KONTEUR ==0:
       #    of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails41.txt"),'a')#('mod2.txt', 'w')
       #    of.write(contenant)
       #    of.close()### SOLUTION ,?
       else:
           of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails"),'w')#('mod2.txt', 'w')##fonctionne pour modifier
           of.write(contenu)#CORRIGER LES FICHES A PARTIR DE 3 ENTREES, AUPARAVANT PLACER SUR 'A'
           of.close()
           #of = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails41.txt"),'a')#('mod2.txt', 'w')
           #of.write(contenant)
           #of.close()### SOLUTION ,?
       def encodage():
          print 'infinity 7 '
          j=0
          #while j ==0:
          #   j=j+1
          
          "renvoie la liste des valeurs entrées, ou une liste vide"
          print "*** Veuillez entrer les données (ou <Enter> pour terminer) :"# si les donnes sont entrees et correctes elles sont gardees mais elles ne sont ecrites qu une fois que l on a valide terminer
          e1 = entr1.get()
          e2 = entr2.get()
          e3 = entr3.get()
          e4 = entr4.get()
          e5 = entr5.get()
          e6 = entr6.get()
          e7 = entr7.get()
          #while e1 != 0 and j<2:
          #   print 'keke'
          #   j = j+1
          #   continue
          #while j<2 and e1!= "":
           #  j = j+1
            # continue
          while 1:
             nom = e1#raw_input("Sexe : ")
             print 'hello'
             print j
             print e1
             ################""
             prenom = e2#raw_input("Date de naissance : ")
             rueNum = e3#raw_input("Adresse (N° et rue) : ")
             cPost = e4#raw_input("Code postal : ")
             local = e5#raw_input("Localité : ")
             tel = e6#raw_input("N° de téléphone : ")
             signP = e7#raw_input("Signe(s) Particulier(s) : ")
             
             #########################################
             if e1 == "":#== "" and j ==2: #and e1 != "":#ici ecriture dans le fichier#nom == "":# indispensable sinon boucle infinie ---> planting
                #if e1 != "":
                print "mesciuuilles"
                return []
             if j ==0:#1
                #j=j+1
                try:
                   if k in globals():#e1 !=""and j ==3:
                      print "here"
                      return[]
                except UnboundLocalError:
                   print "there"
                   pass
                except NameError:
                   print "overhere"
                   pass
                   return[name, surname, nom, prenom, rueNum, cPost, local, tel, signP]
                   
       def enregistrer(liste):
          print 'l'
          "enregistre les données de la liste en les séparant par des <#>"
          i = 0
          while i < len(liste):
             print " JEAN REGISTRE"
             of.write((liste[i]).encode('utf8') + "#")
             i = i + 1
          of.write("\n") # caractère de fin de ligne
          of.close()
          contenuS=""
          ofS = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails"),"r")#("mod.txt","r")
          for ligne in ofS:
           try:
                   print "SAMBA"
                   contenuS += ligne
           except TypeError:
               print "?"
               pass
          ofS.close()
 
          ofS = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails2"),'w')#('mod2.txt', 'w')
          ofS.write(contenuS)
          ofS.close()
       nomF = os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients","rsdetails")#raw_input('Nom du fichier destinataire : ')
       of = open(nomF, 'a')  

       while 1:
          print "JESUISLA"
          tt = encodage()
          if tt == []:
                print 'beak'
                break
          print ' sprint break'
          enregistrer(tt)
          break# LE SEUL TRUC QUI FAIT TOUTE LA DIFFERENCE PAS LOIN DE 8H de misere
       print "SALUT"
       of.close()
       print 'infinity1'
       
    ##################################################################################################################
    if enreMod ==0:
        can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
        bou = Button(fen1, text="Valider", command = LePackage)
        bou.grid(sticky = 'SE')
    else:
        can1.grid(row =1, column = 4, rowspan =3, padx =10, pady = 5)
        bou = Button(fen1, text="Modifier", command = LePackage )
        bou.grid(sticky = 'SE')
    #bou = Button(fen1, text="Nerehistrer", command = enregistrer)
    #bou.grid(sticky = 'SE')
    print 'infinity8'
    fen1.mainloop()
    print 'infinity9'

#########################################################################################################################

############################################################################################################################
def soin():
    l1 = combo.get()
    __file__ = inspect.currentframe().f_code.co_filename
    ##commentaires = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients", "Suivis", "%s" % (combo.get())),"w")
    temps = time.strftime('%y%m%d', time.localtime())

    connex = gadfly.gadfly()
    if not os.path.isdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients")):
                try:
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu"))
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients"))

                except:# WindowsError:
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients"))
    if not os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients", "clients")):  
                    try:      # ntpath for windows
                        fichier = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients", "clients"),"w")
                    except:# WindowsError:
                        fichier = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu","Clients", "clients"),"w")
    if not os.path.isdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps)):
                try:    
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu"))   # ntpath for windows
                except:# WindowsError:
                    os.mkdir(os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps))
    fechier = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients","clients"),"r")# gtest enlever guillemet a gauche C clients
    text = fechier.read()
    #print "e"
    #print text le nom le plus recemment ajouté en haut de la liste
    fechier.close
    fichier = open(os.path.join(os.path.dirname(__file__), "..", "shiatsu", "Clients", "clients"),"w")#pareil en fin du mot
    ###### ici traitement doublons##########
    if text =="":
        fichier.write(l1+'\n')
        fichier.close()
    #fichier.write(l+'\n'+text)
    #print l
    #print text
    chaine = l1
    #print text.strip()
    n=-1
    m=0
    epzylon = text.split('\n') 
    #print epzylon[8]
    ############################
    if l1 in text:
            ############################################################################print text.split('\n')
                #for indice in epzylon:
                try:
                    for mot in epzylon:
                        print n
                        print m
                        print len(epzylon)
                        if m!=0 and n== len(epzylon)-2:###### profiter du continue en l esquivant
                            print "recherche2"
                            fichier.write(l1+'\n'+text)
                            fichier.close()
                        print "WHERE3"
                        n = n+1
                        #print n
                        if l1 == epzylon[n]:
                            print "doublon"
                            fichier.write(text)
                            fichier.close()########## toujours close sinon on enregistre pas plusieurs noms d 'affilée
                            break
                        elif l1!=epzylon[n] and n<len(epzylon):
                            m=m+1
                            print "recherche1"
                            continue
                        
                except IndexError:
                    print"ici?"
                    pass
                    #print "ok"
                    #fichier.write(l+'\n'+text)
    else:
                try:
                    if epzylon[0]:
                        print " t ou"
                        fichier.write(l1+'\n'+text)
                        fichier.close()
                except IndexError:
                    print " je te vois pas"
                    fichier.write(l1+'\n'+text)##### l1 au lieu de l a changé quelquechose dans nouveau soin ?
                    fichier.close()
###########################################################################################""

    def Save(event =None):
        global antiBoutonDoublon
        antiBoutonDoublon = 0
        global pr
        global su ### les reinitialiser a chaque lancement de cette fonction
        pr = 0#-1
        su = 0
        b=combo.get()
        a = Entry(Mafenetre)
        a.insert(END,b)
        a.focus_set()
        a.grid()
        a.config(state="disabled")
        global pro
        global prp##### si on annonce pas global ici il ne dit rien mais il conserve les valeurs acquises dans les fonctions suivangtes
        global thunder##### sans tenir compte / cas des assignations sici-ssisi dessous dessous
        pro = 0
        prp = 0
        thunder = 0
        def callback():
            while ListeItemCercles != []:
                    item2 = ListeItemCercles[-1]
                    #Efface le cercle
                    Canevas.delete(item2)
                    #Suppression de l'item de la liste
                    del ListeItemCercles[-1]
            l1 = a.get()
            
                    #Canevas.postscript(file ="/home/python/Bureau/test/"+ l +".eps")
            connex.startup(l1, os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps)) 
            cur = connex.cursor()
            requete = "create table %s (item integer, bulle varchar, raycercle integer,\
            xcercle integer, ycercle integer, police integer)" % (l1)
            cur.execute(requete)
            connex.commit()
            
            b1.config(state="disabled")#b etant partage par l option derneirs soins, c ce bouton qui etaait grise a la place magie des bugs
          
        b1 = Button(Mafenetre, text='Nouveau Soin', width=12, command=callback)
        b1.grid()
            
        def recherche():
            b1.config(state="disabled")
            b.config(state="disabled")
            while ListeItemCercles != []:
                    item2 = ListeItemCercles[-1]
                    #Efface le cercle
                    Canevas.delete(item2)
                    #Suppression de l'item de la liste
                    del ListeItemCercles[-1]
           # def __init__(self, boss =None):    
            #Créer le ballon
            balloon = Pmw.Balloon(initwait = 0, label_background = 'ivory', relmouse = 'both', xoffset=-66, label_foreground = 'black')# valeur a 0 affichage -> immédiat
            balloon.wm_attributes('-alpha', 0.5)
            #PAR LA
            #print 'FOO'
            def cherchefichier(fichier, rep): 
                print ('DA') # la il print 14000 DA je dois chercher a comprendre pourquoi
    # recherche du contenu du répertoire rep (fichiers et sous-répertoires)
                entrees = os.listdir(rep)  
                # traitement des fichiers du répertoire
                for entree in entrees:
                    if (not os.path.isdir(os.path.join(rep, entree))) and (entree==fichier):
                                    return rep 
                        # traitement récursif des sous-répertoires de rep
                n = 0
                #print 'BOUL' # 14000 DA BOUL DA BOUL
                for entree in entrees:
                    n = n +1
                    rep2 = os.path.join(rep, entree)
                    if os.path.isdir(rep2):
                                    chemin = cherchefichier(fichier, rep2)
                                    print 'K'
                                    if chemin!="":
                                        print 'LIEV'
                                        print chemin
                                        print chemin[12:17]#pareil chemin à revoir en permanence
                                        passe = chemin[11:17]#en 20151117denouvomec[34:40]#[11:17]#chemin[23:29]# ce troncon etait valable sous linux
                                        try:
                                            dico[passe] = chemin#'date%s'%(n)#] = chemin
                                        except NameError:
                                            global dico 
                                            dico = {}
                                            dico[passe] = chemin#'date%s'%(n)] = chemin
                return ""

            rep = os.path.join(os.path.dirname(__file__), "..", "shiatsu")
            m = a.get() # je sais doublon
            fichier = m+'.gfd'  # c'etait ca l oubli, le point gfd, qui empechait l entree du print 'LIEB
            #fichier = u"superpoulain.gfd"
            
            chemin = cherchefichier(fichier,rep)
            dicco = dico.copy()
            sauvegarde = dico.copy()
            diko=dico.copy()
            dicccccco = dico.copy()
            immortality2=dico.copy()
            rescue = dico.copy()### si c est ecrit avant chemin il dit qu il ne conait pas dico
            print dico
            dico.clear() # empeche bien des merdes
            def precedent():
                    global thunder
                    global su
                    su = len(sauvegarde)
                    #d.config(state="enabled")
                    while ListeItemCercles != []:
                        item2 = ListeItemCercles[-1]
                        #Efface le cercle
                        Canevas.delete(item2)
                        #Suppression de l'item de la liste
                        del ListeItemCercles[-1]
                    global pr
                    conteur = pr#+1
                    pr = pr +1
                    global prp
                    prp=pr-su+len(diko)-1-thunder##### le fait DAJOUTER LEN(DIKO)-1 fait MAGIKEMENT TOUT FONCTIONNER
                    print su
                    print pr
                    print prp
                  
                    final = diko.keys()
                    
                    final.sort(reverse=True)
                    print pr
                    if prp==len(final)-1:#-1:
                        #pr = 0
                        c.config(state="disabled")
                    #n = pr - su
                    last = final[prp]
                            
                    print "check"
                    def affichedate(): # je pense que cest une erreur dindent si affiche date est defini sous except laisse tomber le planting
                        
                        if True:#last = 0 # if ponctuel while temps
                            stal = []
                            stal[0:2] = last [4:6]
                            stal[2:4] = last[2:4]
                            stal[4:6]=last[0:2]
                            try:
                                M.config(text=stal)
                            except NameError:
                                M.config(text="derniere fois")
                            except TclError:
                                M.config(text="")
                    #if len(diko) - len(dicccccco) == 1:
                    #master = Toplevel(Mafenetre)
                    M = Label(Mafenetre, text = "", font = 'Arial 14', background = 'ivory')#, foreground = 'green')
                    M.grid(sticky = 'N', row = 0, column = 1)
                    U=threading.Thread(target=affichedate)
                    U.setDaemon(True)
                    U.start()
               
                    connex = gadfly.gadfly(m,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))
                    cur = connex.cursor()
                    requete = "select count(*) from %s" % (m)
                    cur.execute(requete)
                    nbreRangs = cur.pp()
               
                    nbreRangs = nbreRangs[18:20]
                  
                    nbreRangs = int(nbreRangs)
                    n = 0
                    ordre = 1
                    while n < nbreRangs:
                        
                                requete = "select * from %s" % (m)
                                cur.execute(requete)
                                #print cur.pp()
                                ordre = ordre + 1
                                #print ordre
                                #print n
                                requete = "select bulle from %s where item = %s" % (m, ordre)
                                cur.execute(requete)
                                z = cur.pp() #bulle
                              
                                """ Dessine un cercle de centre (x,y) et de rayon r """
                                requete = "select raycercle from %s where item = %s" % (m, ordre)
                                cur.execute(requete)
                                r = cur.pp() # rayon
                                r = r[20:25]
                                if r=="":
                                    n = n+1
                                    continue
                                else:
                              
                                    r = int(r)
                                    
                                    requete = "select xcercle from %s where item = %s" % (m, ordre)
                                    cur.execute(requete)
                                    x = cur.pp() # x
                                   
                                    x = x[15:20]
                                    x = int(x)
                                   
                                    requete = "select ycercle from %s where item = %s" % (m, ordre)
                                    cur.execute(requete)
                                    y = cur.pp() # y
                                   
                                    y = y[15:20]
                                    y = int(y)
                                    cur.fetchall()
                                   
                                    requete = "select police from %s where item = %s" % (m, ordre)
                                    cur.execute(requete)
                                    police = cur.pp() # couleur
                                   
                                    police = police[14:20]
                                    if police == 'black ':
                                        police = 'black'
                                    elif police == 'grey  ':
                                        police = 'grey'
                                       
                                    item2 = Canevas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill=police)
                                    # on ajoute l'item dans la liste
                                    ListeItemCercles.append(item2)
                                    balloon.tagbind(Canevas, item2, z)
                                    connex.commit() # ne surout pas oublier pour clore la base de données et ne pas creer une erreur qui empeche de multiples sauvegardes sans devoir eteindre le programme a chaque fois
                                    print "check5"
                                   
                                    def suivant():
                                        global prp
                                        global pro
                                        global thunder
                                        
                                        print pr
                                        global su
                                        global pr #### suit la valeur prise dans la derniere fonction
                                     
                                        pro= -su+1+len(final)-prp+len(diko)-1#-3#-1#pr+su-len(diko)-1#-1#su = su-1
                                        print pr
                                        print ' ok '
                                        print pro
                                        if len(sauvegarde)==1:###########################################################################
                                            d.config(state='disabled')
                                            return
                                       
                                        if pr == 0:
                                            pass
                                        if pro==len(diko): 
                                            
                                            return
                                           
                                        else:
                                            thunder = thunder+1
                                            c.config(state="enabled")
                                            print "suivant"
                                            while ListeItemCercles != []:
                                                item2 = ListeItemCercles[-1]
                                                #Efface le cercle
                                                Canevas.delete(item2)
                                                #Suppression de l'item de la liste
                                                del ListeItemCercles[-1]
                                        su = su-1
                                        final.sort()#reverse=True)
                                        last=final[pro]
                                        print "check foo"
                                              
                                        def affichedate():
                                            stal = []
                                            stal[0:2]=last[4:6]
                                            stal[2:4]=last[2:4]
                                            stal[4:6]=last[0:2]
                                            if True:
                                                try:
                                                    M.config(text=stal)
                                                except NameError:
                                                    M.config(text="derniere fois")
                                                except TclError:
                                                    M.config(text="")
                                               
                                        #master = Toplevel(Mafenetre)
                                        M = Label(Mafenetre, text = "", font = 'Arial 14', foreground = 'red')#'green')#, background = 'green')
                                        M.grid(sticky = 'N', row = 0, column = 1)
                                        U=threading.Thread(target=affichedate)
                                        U.setDaemon(True)
                                        U.start() 
                                       
                                        connex = gadfly.gadfly(m,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))
                                        cur = connex.cursor()
                                        requete = "select count(*) from %s" % (m)
                                        cur.execute(requete)
                                        nbreRangs = cur.pp()
                                   
                                        nbreRangs = nbreRangs[18:20]
                                        ##ok = 5
                                        nbreRangs = int(nbreRangs)
                                        n = 0
                                        ordre = 1
                                        while n < nbreRangs:
                                            
                                                    requete = "select * from %s" % (m)
                                                    cur.execute(requete)
                                                    #print cur.pp()
                                                    ordre = ordre + 1
                                                    #print ordre
                                                    #print n
                                                    requete = "select bulle from %s where item = %s" % (m, ordre)
                                                    cur.execute(requete)
                                                    z = cur.pp() #bulle
                                                    ##global ok
                                                    ##total = len(z)
                                                    ##if z[ok] =="=":
                                                    ##    print z[ok]
                                                    ##    ok = ok+1
                                                    ##    print ok
                                                    ##    print len(z)
                                                    ##    continue
                                                    ##else:
                                                    ##    ok = ok+1
                                                    ##    z = z[ok:total]
                                                    ##    print z
                                                    """ Dessine un cercle de centre (x,y) et de rayon r """
                                                    requete = "select raycercle from %s where item = %s" % (m, ordre)
                                                    cur.execute(requete)
                                                    r = cur.pp() # rayon
                                                    r = r[20:25]
                                                    if r=="":
                                                        n = n+1
                                                        continue
                                                    else:
                                                  
                                                        r = int(r)
                                                        
                                                        requete = "select xcercle from %s where item = %s" % (m, ordre)
                                                        cur.execute(requete)
                                                        x = cur.pp() # x
                                                       
                                                        x = x[15:20]
                                                        x = int(x)
                                                       
                                                        requete = "select ycercle from %s where item = %s" % (m, ordre)
                                                        cur.execute(requete)
                                                        y = cur.pp() # y
                                                       
                                                        y = y[15:20]
                                                        y = int(y)
                                                        cur.fetchall()
                                                       
                                                        requete = "select police from %s where item = %s" % (m, ordre)
                                                        cur.execute(requete)
                                                        police = cur.pp() # couleur
                                                       
                                                        police = police[14:20]
                                                        if police == 'black ':
                                                            police = 'black'
                                                        elif police == 'grey  ':
                                                            police = 'grey'
                                                           
                                                        item2 = Canevas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill=police)
                                                        # on ajoute l'item dans la liste
                                                        ListeItemCercles.append(item2)
                                                        balloon.tagbind(Canevas, item2, z)
                                                        
                                                        connex.commit() # ne surout pas oublier pour clore la base de données et ne pas creer une erreur qui empeche de multiples sauvegardes sans devoir eteindre le programme a chaque fois
                                if conteur   ==0:
                                    conteur = conteur +1
                                    d = Button(Mafenetre, text='Suivant', width=10, command=suivant)
                                    d.grid(row = 1, column = 0)#sticky = 'NE'
                                else:
                                    print "?"
                                    pass
            c = Button(Mafenetre, text='Précédent', width=10, command=precedent)
            c.grid(row = 2, column = 0)
        b = Button(Mafenetre, text='Dernier Soin', width=12, command=recherche)#je suis meme pas sur finalement
        b.grid()


        
        #try:
        #    Frame.destroy()
        #except TypeError:
        class RadioDemo (Frame):
                """ Bouton Radio """
                def __init__(Toplevel1, boss =None):
                    """ création du champs d'entrée avec 4 boutons radio """
                    Frame.__init__(Toplevel1)
                    Toplevel1.pack()
                    #Créer le ballon
                    Toplevel1.balloon = Pmw.Balloon(Toplevel1, initwait = 0, label_background = 'white')# valeur a 0 affichage -> immédiat
                    Toplevel1.balloon.wm_attributes('-alpha',0.5)
                    a = kems#temps#""
                    global radiTest
                    if radiTest == 0:
                        Toplevel1.texte = Entry(Toplevel1, width =30, font ="Arial 14")
                        Toplevel1.texte.insert(END, a)#"La programmation, c'est génial")
                        Toplevel1.texte.pack(padx =8, pady =8)
                    else:
                        pass
                    #Type de travail et couleurs associées
                    stylePoliceFr =["Tonification", "Harmonisation", "Sédation", "Dispersion"]
                    stylePoliceTk =["tomato", "purple", "grey", "black"]
                    #Le style actuel est mémorisé dans un 'objet-variable'
                    Toplevel1.choixPolice = StringVar()
                    Toplevel1.choixPolice.set(stylePoliceTk[0])
                    #Création des quatre 'boutons radio' :
                     #####badwindowpathname
                    ##if radiTest != 1:
                    radiTest = radiTest+1
                    for n in range(4):
                        bout = Radiobutton(Mafenetre,## Canesvas.. en oubliant grid
                            text = stylePoliceFr[n],
                            #highlightcolor = stylePoliceTk[n],
                            variable = Toplevel1.choixPolice,
                            value = stylePoliceTk[n],
                            command = Toplevel1.changePolice)
                        bout.grid(column = 1, sticky = 'NSEW', row = 4+n)#row = 5, column = 1)#, column = 0, sticky = 'NSEW')#pack(side =LEFT, padx =5)
                    #lol = Label(Mafenetre, background = Toplevel1.choixPolice.get())
                    #lol.grid(sticky = 'NS', ipadx = 88, column = 1, row =4)
                def changePolice(Toplevel1):#### indent ceci une fois et ca bug : radio demo has no instance 'changepolice'
                    police = Toplevel1.choixPolice.get()
                    lol = Label(Mafenetre, background= police)
                    ##Toplevel1.texte.configure(foreground = police) la limite que je me trouve est par là
                    """ Remplacement du style actuel """
                    #Toplevel1.texte.configure(background =police)  #### no attribute text je sais pas quoi
                    if police == "tomato":
                        cool = 4
                    elif police == "purple":
                        cool = 5
                    elif police == "grey":
                        cool = 6### cool == 6 ?
                    else:
                        cool = 7
                    lol.grid(sticky='NS', ipadx=88, column = 1, row =cool)
                    def Cercle(event):
                                        
                                        l = a.get()     #rappel obligatoire visiblement
                                        connex = gadfly.gadfly(l,os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps))
                                        cur = connex.cursor()
                                        """ Dessine un cercle de centre (x,y) et de rayon r """
                                        x = event.x
                                        y = event.y
                                        r = 5
                                        item = Canevas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill=police)
                                        ListeItemCercles.append(item)
                                        requete ="insert into %s (item, bulle, raycercle, xcercle, ycercle, police) values \
                        (%s, %s, %s, %s, %s, '%s')" % (l, item, 0, r, x, y, police)
                                        cur.execute(requete)
                                        connex.commit()
                   
                                        print "fonctionne-je ?"
                    def Cercle2(event):
                                        
                                        l = a.get()
                                        connex = gadfly.gadfly(l,os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps))
                                        cur = connex.cursor()
                                        master = Toplevel()
                                        e = Entry(master)
                                        e.pack()
                                        e.focus_set()
                                        x = event.x
                                        y = event.y
                                        r = 8
                                        item = Toplevel.bluecircle = Canevas.create_oval(x-r, y-r, x+r, y+r, fill=police, tags = 'TAG1')
                                        ListeItemCercles.append(item)

                                        def callback():
                                            z = e.get().encode('utf8')
                                            Toplevel1.balloon.tagbind(Canevas, item, z)
                            
                                            requete ="insert into %s (item, bulle, raycercle, xcercle, ycercle, police) values \
                            (%s, '%s', %s, %s, %s, '%s')" % (l, item, z, r, x, y, police)
                                            cur.execute(requete)
                                            connex.commit()
                                            e.delete(0,END)
                                            BoutonQuitter = Button(master, text='Quitter', command = master.destroy)
                                            BoutonQuitter.pack()

                                        b = Button(master, text='Ok', width=10, command=callback)
                                        b.pack()
                                        
                    #clic gauche lié au cercle
                    Canevas.bind("<Button-1>", Cercle)

                    #clic droit lié au cercle2
                    Canevas.bind("<Button-3>", Cercle2)

                    def Undo():
                        """ Efface le dernier cercle"""
                        j = a.get()
                        connex = gadfly.gadfly(j,os.path.join(os.path.dirname(__file__), "..", "shiatsu", temps))
                        cur = connex.cursor()
                        if ListeItemCercles != []:
                            item = ListeItemCercles[-1]
                            #Efface le cercle
                            Canevas.delete(item)
                            #Suppression de l'item de la liste
                            del ListeItemCercles[-1]
                            requete = "delete from %s where item = %s" % (j, item)
                            cur.execute(requete)
                            connex.commit()
                    global antiBoutonDoublon            #Création d'un widget Button0
                    if antiBoutonDoublon !=1:
                        antiBoutonDoublon = antiBoutonDoublon+1
                        print antiBoutonDoublon
                        BoutonEffacer = Button(Mafenetre, text='Effacer', command = Undo)
                        BoutonEffacer.grid(sticky = 'NSEW', padx = 10, pady = 10)#side = LEFT, padx = 10, pady = 10)
                    else:
                        pass
       
        if __name__ == '__main__':
                        
                        RadioDemo().mainloop()
    
##############################################################SUIVI ECRIT #############################################################

                                                                                           #3
    def action(event=None):                                                            #4
        """défilement du texte jusqu'à la balise <cible>"""                            #5
        index = st.tag_nextrange('cible', '0.0', END)                                  #6
        st.see(index[0])                                                               #7
    def suivi():                                                                               #8
        
        a = combo.get()###### si je met tout ca en dessous, contenu fichier effacé. Sans doute parce qu en meme temps d etre declare, suivi2 s autoecrase
        suivi2 = open(os.path.join(os.path.dirname(__file__),"..","shiatsu","Clients","Suivis",a),'w')###### 'a' au lieu de 'w' permet d'écrire à la suite
        suivi2.write(st.get().encode('utf8'))#texte+'\n'+st.get())###### unicode encode error ---> à dégager
        suivi2.close()                              
        print "enregistrer"       
######################################################################### SUIVI ECRIT #######################################################################

    # Initialisation de la liste des items des cercles
    ListeItemCercles = []

    #Création de la fenêtre principale (main window)
    Mafenetre = Toplevel()
    Mafenetre.title(combo.get())

    #Image de fond
    photo = PhotoImage(file="c.gif") #c

    #Création d'un widget Canvas ( zone graphique )
    Largeur = 777   #777  (1200 avec e mais nul a chier)
    Hauteur = 555   #666
    Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)
    Canevas.grid(row = 0, column = 1, sticky = 'NSEW')
    Mafenetre.wm_state(newstate="iconic")#"zoomed")
    # No more zoomed: normal iconic or withdrawn

        #Création d'un widget Button0
    BoutonQuitter = Button(Mafenetre, text='Quitter', command = Mafenetre.destroy)
    BoutonQuitter.grid(sticky = 'SE', padx=10, pady =10)#(side = LEFT, padx = 10, pady = 10)                               
    
    BoutonSuivi = Button (Mafenetre, text='Enregistrer', command = suivi)
    BoutonSuivi.grid(row=4,column=0, sticky = 'NSEW')#### tester le bouton en column 1. Assez impressionant.
    
    # Instanciation d'une fenêtre contenant un widget ScrolledText :                   #9
    #fen = Pmw.initialise()                                                             #10
    st = Pmw.ScrolledText(Mafenetre,                                                         #11
                          labelpos =S,                                                 #12
                          label_text ="%s:%s" % (combo.get(), kems),#Petite démo du widget ScrolledText",            #13
                          label_font ='Times 14 bold italic',                          #14
                          label_fg = 'navy', label_pady =5,                            #15
                          text_font='Helvetica 11 normal', text_bg ='ivory',           #16
                          text_padx =10, text_pady =10, text_wrap ='none',             #17
                          borderframe =1,                                              #18
                          borderframe_borderwidth =3,                                  #19
                          borderframe_relief =SOLID,                                   #20
                          usehullsize =1,                                              #21
                          hull_width =777, hull_height =555)  ########## 370 240  ####### hull width 644  hull height 555     777 sans bug 644 avec bug              
    st.grid(sticky = 'NSEW', row = 0, column = 0)#(expand =YES, fill =BOTH, padx =8, pady =8)#, side=LEFT)                                 
                                                                                
    # Définition de balises, liaison d'un gestionnaire d'événement au clic de souris : 
    st.tag_configure('titre', foreground ='brown', font ='Helvetica 11 bold italic')   
    st.tag_configure('lien', foreground ='blue', font ='Helvetica 11 bold')            
    st.tag_configure('cible', foreground ='forest green', font ='Times 11 bold')       
    st.tag_bind('lien', '<Button-1>', action)
    ##suivi = open(os.path.join(os.path.dirname(__file__),"..","shiatsu","Clients","Suivis",a),'r')                                                                                    
    titre ="""%s\n""" % (kems  )                                                                            
    auteur ="""                                                                        
    %s""" % (kems)                                                                
    ##texte = suivi.read()
                                                                                   
    # Remplissage du widget Text (2 techniques) :
    try :
        st.importfile(os.path.join(os.path.dirname(__file__),"..","shiatsu","Clients","Suivis","%s"%(combo.get())))## coercing to uicode : à cause d'open
    except IOError:#except TypeError:
        a = combo.get()
 
        suivi2 = open(os.path.join(os.path.dirname(__file__),"..","shiatsu","Clients","Suivis",a),'w')
        suivi = open(os.path.join(os.path.dirname(__file__),"..","shiatsu","Clients","Suivis",a),'r')
        texte = suivi.read()
        if texte =="":
            
            suivi2.write(kems)#texte+'\n'+st.get())
            suivi2.close()
        else:
            pass
    #    pass
    st.insert('0.0', titre, 'titre')                                                   
    st.insert(END, auteur, 'cible')                                                    
    # Insertion d'une image :                                                          
    #photo =PhotoImage(file= 'Fl.gif')     ###### si F.gif (corps modele 300x200) celui en taille normale ne s'affiche pas                                        
    #st.image_create('6.14', image =photo)                                              
    # Mise en oeuvre dynamique d'une balise :                                          
    st.tag_add('lien', '2.4', '2.23')                                                  
    
    Mafenetre.grid_columnconfigure(0,weight=1) # ok rouge bleu gris adaptes
    Mafenetre.grid_columnconfigure(1,weight=1)# grace a cette petite ligne, le dessin de droite reste au lieu de se barrer NIMPORTE OU
    Mafenetre.grid_rowconfigure(0,weight=1) # a l agrandissement de la fenetre
    Mafenetre.grid_rowconfigure(1,weight=1) # donc ces lignes servent a ca
        #self.root.grid_rowconfigure(2,weight=1) je ne sais pas utilité de cette ligne
#Mafenetre.mainloop()############# Comme TJRS element vitaml
#root = Tk() remplacé par Mafenetre
    frame=Frame(Mafenetre)#,width=300,height=300)
    frame.grid(row=0,column=0)
    #Création d'un widget Button0
    BoutonChange = Button(Mafenetre, text='Démarrer', command = Save())   ###### ici ils sont situés au dessus du texte #### question d'ordre, de position
    BoutonChange.grid(sticky = 'SW', padx = 10, pady=10)#(side = LEFT, padx = 10, pady = 10)####### en dessous en dessous


    Mafenetre.mainloop()


###############################" GO #######################################       
param1 = StringVar()
Label(win,text='',background = 'forest green').place(x=10, y=10)
combo = AutocompleteCombobox(win,textvariable=param1)
combo.set_completion_list(symbols)
combo.pack()
combo.focus_set()

#Entry(win,width=10,textvariable=param1).place(x=10, y=40)
Button(win,text='Soin',command=soin).place(x=10, y=77)# x 10 y 90
#Button(win,text='Centre',command=go).place(x=10, y=99)
Button(win,text='Fiches',command=go).place(x=10, y=121)
##Menu
menubar = Menu(win,background = 'cadet blue')
menubar.add_command(label="Quitter",command=win.destroy)#go)
def hello():#print "hello!"######elle ne marchait qu au debut et ne repondait pas
############" si je n imbriquais pas chercheficheir dans hello aux commandes
    balloon = Pmw.Balloon(initwait = 0)
    def cherchefichier(fichier, rep):
     
    # recherche du contenu du répertoire rep (fichiers et sous-répertoires)
        entrees = os.listdir(rep)  
        # traitement des fichiers du répertoire
        for entree in entrees:
            if (not os.path.isdir(os.path.join(rep, entree))) and (entree==fichier):
                            
                            return rep 
                # traitement récursif des sous-répertoires de rep
        n = 0
        
        for entree in entrees:
            
            n = n +1
            rep2 = os.path.join(rep, entree)
            if os.path.isdir(rep2):
                            chemin = cherchefichier(fichier, rep2)
                            print 'K'
                            if chemin!="":
                                print 'LIEV'
                                print chemin
                                print chemin[12:17]### encore a un pres il retourne
                                passe = chemin[34:40]## "x30" au lieu de la date
                                try:### lignes tres importantes a surveiller
                                    dico[passe] = chemin#'date%s'%(n)#] = chemin
                                except NameError:
                                    global dico 
                                    dico = {}
                                    dico[passe] = chemin#'date%s'%(n)] = chemin
                
        return ""
    a = combo.get()
    rep = os.path.join(os.path.dirname(__file__), "..", "shiatsu")#GoStraight . py ne pas oublier le remplacement par file
            #m = a.get() # je sais doublon
    fichier = a+'.gfd'  # c'etait ca l oubli, le point gfd, qui empechait l entree du print 'LIEB
            #fichier = u"superpoulain.gfd"
    print 'lol'
    print a
    b = "Date"
    chemin = cherchefichier(fichier,rep)#if chemin!="":
    root = tk.Tk(className =' %s' % b)###### premiere decouverte root plutot ici que ds la def test, ainsi button reconnu. Ensuite si on enleve celui de la def test alors les champs se retrouvent ds la meme fenetre
    entry = Entry(root)######## mais ces deux trucs, pour pouvoir lire le contenu, il fallait les déclarer AVANT LA FCTION AVANT LES BOEUFS
    combo2 = AutocompleteCombobox(root)#,textvariable = StringVar())(pas utile)
    def test(test_list):#ici ds la meme fenetre, car sinon l autre fenetre c juste les boutons, l autre juste les champs. PAS Fantastique
        """Run a mini application to test the AutocompleteEntry Widget."""# la surprise reste que je retrouve utilement le b demarrer ds cette fenetre qui est intelligemment place apres la fonction retrouvailels*
        #root = tk.Tk(className=' Choix date')# laisser un espace pour que la majuscule soit prise en compte. Je sais pas pourquoi.
        
        entry = AutocompleteEntry(root)
        print entry
        entry.set_completion_list(test_list)
        entry.grid()
        entry.focus_set()
        global last
        
        combo2.set_completion_list(test_list)
        combo2.grid()
        combo2.focus_set()
        ########entry = Entry(root)# = combo2.get()####### en fait continuer d annoncer tout ca hors fonction sinon la suivante connait pô
        #e888 = entry.get()## dej a c ca et surtout pas l inverse visiblement la fct est apres la variable
        e888 = combo2.get()
        entry.grid()
        entry.focus_set()
        #print str(Combobox.get)
        #print Combobox
        #print combo2.get()
        # I used a tiling WM with no controls, added a shortcut to quit
        root.bind('<Control-Q>', lambda event=None: root.destroy())
        root.bind('<Control-q>', lambda event=None: root.destroy())
    
    if __name__ == '__main__':
 
        dicco = dico.copy()########## deinitivement le seul systeme qui marche pour ne pas accuuler 
        test_list = dicco.keys()#('apple', 'banana', 'CranBerry', 'dogwood', 'alpha', 'Acorn', 'Anise' )
        dico.clear()
        test(test_list)
        last = temps
        
        
        m = combo.get()# deut du orchestra
        print a+m+"HAlo"#last = entry.get()
        print last+"last"
    
    def retrouvailles():
        while ListeItemCercles != []:
            item2 = ListeItemCercles[-1]
            Canevas.delete(item2)
            del ListeItemCercles[-1]
        
        last = combo2.get()
        print combo2.get()
        entry = combo2.get()
        #print entry.get()
        print test(test_list)
        connex = gadfly.gadfly(m,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))
        cur = connex.cursor()
        requete = "select count(*) from %s" % (m)
        cur.execute(requete)
        nbreRangs = cur.pp()
        #print cur.pp() #recherche du bug
        #print len(nbreRangs)
        #print nbreRangs[18]
        nbreRangs = nbreRangs[18:20]
        #créer une boucle pour refaire chaque cercle n est le nbre de rangees
        nbreRangs = int(nbreRangs)
        n = 0
        ordre = 1
        while n < nbreRangs:
            #def Cercleauto(event): #le bug vient de cette ligne
                    requete = "select * from %s" % (m)
                    cur.execute(requete)
                   
                    ordre = ordre + 1
                   
                    requete = "select bulle from %s where item = %s" % (m, ordre)
                    cur.execute(requete)
                    z = cur.pp() #bulle
                    
                    """ Dessine un cercle de centre (x,y) et de rayon r """
                    requete = "select raycercle from %s where item = %s" % (m, ordre)
                    cur.execute(requete)
                    r = cur.pp() # rayon
                    r = r[20:25]
                    if r=="":
                        n = n+1
                        continue
                    else:
                    
                        r = int(r)
                     
                        requete = "select xcercle from %s where item = %s" % (m, ordre)
                        cur.execute(requete)
                        x = cur.pp() # x
                        
                        x = x[15:20]
                        x = int(x)
                  
                        requete = "select ycercle from %s where item = %s" % (m, ordre)
                        cur.execute(requete)
                        y = cur.pp() # y
                        
                        y = y[15:20]
                        y = int(y)
                        cur.fetchall()
                        
                        requete = "select police from %s where item = %s" % (m, ordre)
                        cur.execute(requete)
                        police = cur.pp() # couleur
                       
                        police = police[14:20]
                        if police == 'black ':
                            police = 'black'
                        elif police == 'grey  ':
                            police = 'grey'
                         
                        #print cur.pp() # cherchebug
                        #z = contenu de bulle
                        # on dessine un cercle dans la zone graphique                      # on ajoute l'item dans la liste
                        item2 = Canevas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill=police)
                        ListeItemCercles.append(item2)
                        balloon.tagbind(Canevas, item2, z)
                     
                        connex.commit() # ne surout pas oublier pour clore la base de données et ne pas creer une erreur qui empeche de multiples sauvegardes sans devoir eteindre le programme a chaque fois
    
        
        
                        
        class RadioDemo (Frame):
            """ Bouton Radio """
            def __init__(self, boss =None):
                """ création du champs d'entrée avec 4 boutons radio """
                Frame.__init__(self)
                self.pack()
                #Créer le ballon
                self.balloon = Pmw.Balloon(self, initwait = 0)# valeur a 0 affichage -> immédiat
                #Un léger ballon
                #tip = Pmw.balloon(self) ce tip faisait tout planter
                #Champs d'entrée contenant un texte, Probablement en vue d'insérer un nom qui nommera une sauvegarde en l'état
                #print last
                #if last == 0:
                a = temps#""
                #else:
                #    a = temps + "visite du" + last
                self.texte = Entry(self, width =30, font ="Arial 14")
                self.texte.insert(END, a)#"La programmation, c'est génial")
                self.texte.pack(padx =8, pady =8)
                #Type de travail et couleurs associées
                stylePoliceFr =["Tonification", "Harmonisation", "Sédation", "Dispersion"]
                stylePoliceTk =["tomato", "purple", "grey", "black"]
                #Le style actuel est mémorisé dans un 'objet-variable'
                self.choixPolice = StringVar()
                self.choixPolice.set(stylePoliceTk[0])
                #Création des quatre 'boutons radio' :
                for n in range(4):
                    bout = Radiobutton(self,
                        text = stylePoliceFr[n],
                        variable = self.choixPolice,
                        value = stylePoliceTk[n],
                        command = self.changePolice)
                    bout.pack(side =LEFT, padx =5)
                    #tip.bind(bout, 'ok')      et celjui la faisait tout foirer egalement sous windows                  # c'est un autre type

            def changePolice(self):
                """ Remplacement du style actuel """
                police = self.choixPolice.get()
                self.texte.configure(background =police)

                def Cercle(event):
                                    l = a.get()     #rappel obligatoire visiblement
                                    connex = gadfly.gadfly(l,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))#temps
                                    cur = connex.cursor()
                                    """ Dessine un cercle de centre (x,y) et de rayon r """
                                    x = event.x
                                    y = event.y
                                    r = 5
                                    item = Canevas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill=police)
                                    ListeItemCercles.append(item)
                                    requete ="insert into %s (item, bulle, raycercle, xcercle, ycercle, police) values \
                    (%s, %s, %s, %s, %s, '%s')" % (l, item, 0, r, x, y, police)
                                    cur.execute(requete)
                                    connex.commit()
                   

                def Cercle2(event):
                                    l = a.get()
                                    connex = gadfly.gadfly(l,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))#temps
                                    cur = connex.cursor()
                                    master = Tk()
                                    e = Entry(master)
                                    e.pack()
                                    e.focus_set()
                                    x = event.x
                                    y = event.y
                                    r = 8
                                    item = self.bluecircle = Canevas.create_oval(x-r, y-r, x+r, y+r, fill=police, tags = 'TAG1')
                                    ListeItemCercles.append(item)

                                    def callback():
                                        z = e.get()
                                        self.balloon.tagbind(Canevas, item, z)
                        #Création d'un widget Button0
                                        requete ="insert into %s (item, bulle, raycercle, xcercle, ycercle, police) values \
                        (%s, '%s', %s, %s, %s, '%s')" % (l, item, z, r, x, y, police)
                                        cur.execute(requete)
                                        connex.commit()
                                        BoutonQuitter = Button(master, text='Quitter', command = master.destroy)
                                        BoutonQuitter.pack()

                                    b = Button(master, text='Ok', width=10, command=callback)
                                    b.pack()

                    
                   
                #clic gauche lié au cercle
                Canevas.bind("<Button-1>", Cercle)

                #clic droit lié au cercle2
                Canevas.bind("<Button-3>", Cercle2)

                def Undo():
                    """ Efface le dernier cercle"""
                    j = a.get()
                    connex = gadfly.gadfly(j,os.path.join(os.path.dirname(__file__), "..", "shiatsu", last))#temps
                    cur = connex.cursor()
                    if ListeItemCercles != []:
                        item = ListeItemCercles[-1]
                        #Efface le cercle
                        Canevas.delete(item)
                        #Suppression de l'item de la liste
                        del ListeItemCercles[-1]
                        requete = "delete from %s where item = %s" % (j, item)
                        cur.execute(requete)
                        connex.commit()
                            #Création d'un widget Button0
                BoutonEffacer = Button(Mafenetre, text='Effacer', command = Undo)
                BoutonEffacer.pack(side = LEFT, padx = 10, pady = 10)


        if __name__ == '__main__':
                    RadioDemo().mainloop()




        # Initialisation de la liste des items des cercles
    ListeItemCercles = []

        #Création de la fenêtre principale (main window)
    Mafenetre = Toplevel()#Tk() C POURQUOI CELA REFONCTIONNEEEEEUH
    Mafenetre.title(combo.get())

        #Image de fond
    photo = PhotoImage(file="c.gif") #c

        #Création d'un widget Canvas ( zone graphique )
    Largeur = 777   #777  (1200 avec e mais nul a chier)
    Hauteur = 555   #666
    Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
    item = Canevas.create_image(0,0,anchor=NW, image=photo)#####ici c 'est UE J UTILISE PLUSIEURS WINDOS ROOT IL FAUT
    Canevas.pack()# TROUVER AUTRE CHOSE
     

    ###############
     #Création d'un widget Button0
    BoutonChange = Button(root, text='Démarrer', command = retrouvailles)
    BoutonChange.grid()#sticky = 'N', row = 2, column = 2, padx = 10, pady = 10)
    root.mainloop()



# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0, background = 'dark red')
filemenu.add_command(label="Open", command=hello)#hello)#### si je met command = cherchefichier ici ca double le nbre de passages dans la boucle
file#enu.add_command(label="Save", command=hello)
filemenu.add_command(label="Save", command = Save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.destroy)#win.quit totalement foireux
menubar.add_cascade(label="Historique", menu=filemenu)

#display the menu
win.config(menu=menubar, background = 'forest green')

win.mainloop()
