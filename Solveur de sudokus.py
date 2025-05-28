# -*- coding: utf-8 -*-

##### 1ere methode avec deduction des valeurs possibles ############################




#Le programme fonctionne avec des sudokus en format .csv générés à l'aide du site https://qqwing.com/generate.html
    
#liste les valeurs possibles d'une case si sa valeur est inconnue et change la représentation du sudoku en chaîne de caractères en une liste de listes (liste de 9 listes de 9 cases)
def formater(L): #L est une chaîne de caractères
    Sudoku=[[]for i in range(9)]
    for i in range(len(L)):
        x = L[i]
        if x=='.':
            val=[1,2,3,4,5,6,7,8,9]
        else:
            val=[int(x)]
        Sudoku[i//9].append(val)
    return Sudoku                
                
def copier_sudoku(SUDOKU):#fait une copie profonde du sudoku 
    Li=[]
    for i in range(len(SUDOKU)):
        Lj=[]
        for j in range(len(SUDOKU[i])):
                a=SUDOKU[i][j].copy()
                Lj.append(a)
        Li.append(Lj)
    return Li


def coords_ligne(i):#coordonnée des cases de la ieme ligne
    return [(i, k) for k in range (9)]

def coords_colonne(i):#coordonnée des cases de la ieme colonne
    return [(k,i) for k in range (9)]

def coords_bloc(num):#coordonnée des cases du num-ième bloc
    L=[]
    i_init=(num//3)*3
    j_init=(num%3)*3
    for i in range (3):
        for j in range(3):
            L.append((i+i_init,j+j_init))
    return L
    
def valeurs_isolees(SUDOKU,coord):#recherche des valeurs isolees (cases où il n'y a qu'une seule possiblité) parmi un ensemble de coordonnées
    L=[]
    for couple in coord:
        a,b=couple
        x=SUDOKU[a][b]
        
        if len(x)==1:
            L.append(x[0])
    return L
    
def effacer(SUDOKU,coord): #cherche quelles cases sont des valeurs isolées et supprime ces valeurs isolées des autres cases (la valeur est déjà prise)
    L=valeurs_isolees(SUDOKU,coord)
    for i in L:
        for couple in coord:
            a,b = couple
            if i in SUDOKU[a][b] and len(SUDOKU[a][b])>1:
                SUDOKU[a][b].remove(i)
                
    return SUDOKU

def effacer_tout(SUDOKU):#applique effacer à chaque ligne, chaque colonne et chaque bloc
    A=copier_sudoku(SUDOKU)
    for i in range(9):#à chaque ligne
        co=coords_ligne(i)
        SUDOKU=effacer(SUDOKU,co)
    for j in range(9):#à chaque colonne
        co=coords_colonne(j)
        SUDOKU=effacer(SUDOKU,co)
    for k in range(9):# à chaque bloc
        co=coords_bloc(i)
        SUDOKU=effacer(SUDOKU,co)
    if A==SUDOKU:
        return False
    return True

def deduire_tout(SUDOKU):#diminue au maximium le nombre de possibilités
    a=effacer_tout(SUDOKU)
    while a==True:
        a=effacer_tout(SUDOKU)
    return SUDOKU
        
        
def statut(SUDOKU):
    #AFINIR = 0
    #CONTRADICTION = 1
    #TERMINE = 2
    #renvoie le statut du sudoku et les coordonnées d'une case avec plusieurs possibilités si le statut est AFINIR
    #######Vérif des contradictions#
    for i in range (9):#vérif de contradiction sur les lignes et les colonnes
        L=[]
        C=[]
        for j in range(9):
            a=SUDOKU[i][j]
            b=SUDOKU[j][i]
            if len(a)==1:
                if a in L:
                    return 1, 'contradiction'
                L.append(a)
                
            if len(b)==1:
                if b in C:
                    return 1, 'contradiction'
                C.append(b)
                
    for i in range(9):#vérif de contradiction sur les blocs
      B=[]
      for j in range(9):
        c,d=coords_bloc(i)[j]
        a=SUDOKU[c][d]
        if len(a)==1:
            if a in B:
                return 1, 'contradiction'
            B.append(a)
    ################################
    
    for i in range(9):
        for j in range(9):
            etat=SUDOKU[i][j]
            if len(etat)>1:
                coord=(i,j)
                return 0, coord
    
    return 2, 'fini'

def resoudre(SUDOKU):#résout récurssivement le SUDOKU
    deduire_tout(SUDOKU)
    etat=statut(SUDOKU) 
    if etat[0] == 1:
        return None
    elif etat[0] == 2:
        return SUDOKU
    else:
        a,b=etat[1]
        for i in SUDOKU[a][b]:
            copie=copier_sudoku(SUDOKU)
            copie[a][b]=[i]
            m=resoudre(copie)
            if m!=None: #retourne le SUDOKU dès qu'une solution est possible
                return m
            
def afficher_sudoku(grille):
    Longueur_bloc=3 #à modifier si on veut représenter des blocs 2*2 dans des grilles 4*4 par exemple
    Taille_bloc=Longueur_bloc**2
    Taille_ligne=Taille_bloc
    Taille_colonne=Taille_bloc
    
    for i in range(Taille_colonne):
        ligne=" "
        for j in range(Taille_ligne):
            if grille[i][j]==[1,2,3,4,5,6,7,8,9]:
              ligne +=". "
            else:
                ligne += str(grille[i][j][0])+" "
            if j%Longueur_bloc == Longueur_bloc-1 and j!=Taille_ligne-1:
                ligne += "| "
        print(ligne)
        if i%Longueur_bloc == Longueur_bloc-1 and i!=Taille_colonne-1:
            sep=""
            for i in range (Longueur_bloc):
                sep +=(Longueur_bloc*2+1)*"-"+"|"
            sep = sep[:-1] # on enlève le dernier | en trop
            print(sep)
            
def solveur_sudoku(sudoku): #à utiliser avec '.....' un sudoku sous forme de ligne
    A=sudoku.split(",")[0]#[0] pour ne garder que le sudoku (enlever la difficulté, etc.)
    SUDOKU=formater(A)
    print('Sudoku initial :')
    afficher_sudoku(SUDOKU)
    sol=resoudre(SUDOKU)
    print('\nSudoku résolu :')
    afficher_sudoku(sol)

#####FIN 1ère Méthode (avec déduction des valeurs possibles)############################
    
##### 2e methode sans deduction des valeurs possibles #####

#on réécrit la fonction formater car il est inutile pour cette méthode de lister les valeurs possibles (est uniquement utile pour chercher les valeurs isolées). On remplace donc les . par des 0.

def formater2(S):#S est une chaîne de caractères
    Sudoku=[[]for i in range(9)]
    for i in range(len(S)):
        x = S[i]
        if x=='.':
            val=0
        else:
            val=int(x)
        Sudoku[i//9].append(val)
    return Sudoku

def absentSurLigne (k,grille,i):#regarde si le nombre est absent de la i-ème ligne
    for j in range (9):
        if grille[i][j] == k:
            return False
    return True
    
def absentSurColonne (k,grille,j):
    for i in range(9):
        if grille[i][j]==k:
            return False
    return True

def absentSurBloc (k,grille,i,j):
    i_init=(i//3)*3
    j_init=(j//3)*3
    for i in range (3):
        for j in range(3):
            if grille[i+i_init][j+j_init]==k:
                return False
    return True      

def estValide(grille,position):#position est un entier compris entre 0 et 80
    #si on a parcouru toutes les cases sans contradiction, la grille est valide
    if position == 9*9:
        return True
    i = position//9
    j = position%9
    
    #si la case n'est pas vide, on passe à la case suivante avec un appel récursif
    if grille[i][j]!=0:
        return estValide(grille,position+1)
    
    #sinon, on fait le test de toutes les valeurs possibles
    for k in range(1,10):
        if absentSurLigne(k,grille,i) and absentSurColonne(k,grille,j) and absentSurBloc(k,grille,i,j):#si la valeur est absente sur la ligne, la colonne et le bloc (donc autorisée)
          grille[i][j]=k #on teste k dans la grille
          if estValide(grille,position+1):#si la grille est valide avec cette valeur
              return True #le choix est bon. On a résolu notre Sudoku (en supposant qu'il ne possède qu'une solution)
    grille[i][j] = 0 #tous les chiffres ont été testés et aucun n'est bon. On réinitialise la case
    return False

Longueur_bloc=3 #à modifier si on veut représenter des blocs 2*2 dans des grilles 4*4 par exemple
Taille_bloc=Longueur_bloc**2
Taille_ligne=Taille_bloc
Taille_colonne=Taille_bloc
          
def afficher_sudoku2(grille):
    for i in range(Taille_colonne):
        ligne=" "
        for j in range(Taille_ligne):
            if grille[i][j]==0:
              ligne +=". "
            else:
                ligne += str(grille[i][j])+" "
            if j%Longueur_bloc == Longueur_bloc-1 and j!=Taille_ligne-1:
                ligne += "| "
        print(ligne)
        if i%Longueur_bloc == Longueur_bloc-1 and i!=Taille_colonne-1:
            sep=""
            for i in range (Longueur_bloc):
                sep +=(Longueur_bloc*2+1)*"-"+"|"
            sep = sep[:-1] # on enlève le dernier | en trop
            print(sep)

def solveur_sudoku2(sudoku): #à utiliser avec '.....' un sudoku sous forme de ligne
    A=sudoku.split(",")[0]#[0] pour ne garder que le sudoku (enlever la difficulté, etc.)
    SUDOKU=formater2(A)
    print('Sudoku initial :')
    afficher_sudoku2(SUDOKU)
    estValide(SUDOKU,0) #on part de 0 et on va jusqu'à 80 pour vérifier l'intégralité du SUDOKU
    print('\nSudoku résolu :')
    afficher_sudoku2(SUDOKU)
    
######FIN 2e méthode #######