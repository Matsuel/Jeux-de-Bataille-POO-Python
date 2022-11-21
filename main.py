#from tkinter import *
import random

class Carte :
  def __init__(self,val,coul):
    assert val in range(2,15),"cette valeur n'existe pas "
    assert coul in ["Trèfle","Carreau","Coeur","Pique"],"cette couleur n'existe pas "
    self.__valeur = int(val)
    self.__couleur= coul
    self.__SetFig(val)

  def GetVal(self):
    return self.__valeur

  def GetCoul(self):
    return self.__couleur

  def GetFig(self):
    return self.__figure
  
  def Nom(self):
    return self.__figure+" de "+self.__couleur

  def __SetFig(self,val):
    if val==14 :
      self.__figure = "As"
    elif val == 11 : 
      self.__figure = "Valet"
    elif val ==12:
      self.__figure = "Dame"
    elif val==13:
      self.__figure = "Roi"
    else :
      self.__figure = str(self.__valeur)

  
  def __repr__ (self):
    if self.__couleur== "Pique":
      codecouleur = u'\u2660'
    elif self.__couleur== "Trèfle":
      codecouleur = u'\u2663'
    elif self.__couleur== "Coeur":
      codecouleur = u'\u2665'
    else :
      codecouleur= u'\u2666'
    if self.__valeur >= 2 and self.__valeur<=10:
      return self.__figure+codecouleur
    else:
      return self.__figure [0]+codecouleur

class JeuDeCartes :
  def __init__(self,taille,n,nomj1,nomj2):
    assert taille == 32 or taille == 52
    assert n>= 1 and type (n) == int
    self.__paquet=[]
    self.__paquetj1=[]
    self.__paquetj2=[]
    self.__tapis = []
    self.__nomj1= nomj1
    self.__nomj2= nomj2
    if taille == 32:
      for i in range(n):
        for val in range (7,15):
          for coul in ["Trèfle","Carreau","Coeur","Pique"]:
            self.__paquet.append(Carte(val,coul))
    elif taille == 52:
      for i in range(n):
        for val in range (2,15):
          for coul in ["Trèfle","Carreau","Coeur","Pique"]:
            self.__paquet.append(Carte(val,coul))

  def DistribuerCartes(self):
    for i in range(len(self.__paquet)//2):
      self.__paquetj1.append(self.__paquet[i])
    for i in range(len(self.__paquet)//2):
      self.__paquetj2.append(self.__paquet[-i-1])
    print(self.__paquetj1, self.__paquetj2)

  #for i in range (2,52,2):
       # self.__jeu1.append(self.__paquet[i])
      #for i in range (1,51,2):
       # self.__jeu2.append(self.__paquet[i-1])

  def GetPaquet(self):
    return self.__paquet

  def GetPaquetJ1(self):
    return self.__paquetj1

  def GetPaquetJ2(self):
    return self.__paquetj2

  def GetVal1ereCartesJ1(self):
    return Carte.GetVal(self.__paquetj1[0])

  def GetVal1ereCartesJ2(self):
    return Carte.GetVal(self.__paquetj2[0])

  def GetTapis(self):
    return self.__tapis

  def Melanger(self):
    for i in range(15):
      random.shuffle(self.__paquet)


  def GetNomJ1(self):
    return self.__nomj1

  def GetNomJ2(self):
    return self.__nomj2    

  def BatailleDeCartes(self):     
    if self.__paquetj2==[]:
      return (print(self.__nomj1 +" a gagné la partie. Bravo!"))
    elif self.__paquetj1==[]:
      return (print(self.__nomj2+" a gagné la partie. Bravo!"))
    else:  
      while self.__paquetj1!=[] or self.__paquetj2!=[]:
        print("Tour suivant:") 
        if Carte.GetVal(self.__paquetj1[0])>Carte.GetVal  (self.__paquetj2[0]):
          self.__tapis.append(self.__paquetj1[0])
          self.__paquetj1.pop(0)
          self.__tapis.append(self.__paquetj2[0])
          self.__paquetj2.pop(0)
          for i in range(len(self.__tapis)):
            self.__paquetj1.append(self.__tapis[i])
          print(self.__tapis)
          print(self.__nomj1," remporte les cartes")
          self.__tapis=[]
          print(self.__paquetj1)
          print(self.__paquetj2)
          if self.__paquetj2==[]:
            return(print(self.__nomj1," a gagné la partie. Bravo!"))
        elif Carte.GetVal(self.__paquetj2[0])> Carte.GetVal (self.__paquetj1[0]):
          self.__tapis.append(self.__paquetj1[0])
          self.__paquetj1.pop(0)
          self.__tapis.append(self.__paquetj2[0])
          self.__paquetj2.pop(0)
          for i in range(len(self.__tapis)):
            self.__paquetj2.append(self.__tapis[i])
          print(self.__tapis)
          print(self.__nomj2," remporte les cartes")
          self.__tapis=[]
          print(self.__paquetj1)
          print(self.__paquetj2)
          if  self.__paquetj1==[]:
            return (print(self.__nomj2," a gagné la partie. Bravo!"))
        elif Carte.GetVal(self.__paquetj1[0])==Carte.GetVal (self.__paquetj2[0]):
          if len(self.__paquetj1)>=3 and len(self.__paquetj2)>=3:
            print("Même carte , Bataille!")
            for i in range(2):
              self.__tapis.append(self.__paquetj1[0])
              self.__paquetj1.pop(0)
              self.__tapis.append(self.__paquetj2[0])
              self.__paquetj2.pop(0)
              #print(self.__tapis)
          elif len(self.__paquetj1)<3:
          #if len(self.__paquetj1)==0:  
            return (print("Bataille impossible "+self.__nomj1, "n'a pas assez de cartes, "+self.__nomj2," remporte la partie"))
          elif len(self.__paquetj2)<3:
          #elif len(self.__paquetj2)==0:
            return print("Bataille impossible "+self.__nomj2, "n'a pas assez de cartes, "+self.__nomj1," remporte la partie")
    

#taille=int(input("Quel est la taille du paquet ?"))
#nb=int(input("Combien de paquet voulez-vous ?"))
#j1=str(input("Quel est le nom du premier joueur ?"))
#j2=str(input("Quel est le nom du second joueur ?"))
Jeu =JeuDeCartes(32,1,"roger","pipi")
Jeu.Melanger()
Jeu.DistribuerCartes()
Jeu.BatailleDeCartes()