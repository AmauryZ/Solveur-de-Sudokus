Instructions d'utilisation du programme :

Générer un suduoku à l'aide du site https://qqwing.com/generate.html en choisissant csv comme format de sortie ('Output format'). 
Copier la 2e ligne (ie le sudoku généré sous forme de ligne) (ex : 64.8.....91.....8..876.9.24....7.8.......4......9..16..7.4..3.......7.1..9.1.8.7.,27,41,13,3,0,0,0,0,0,Intermediate,)

Executer la fonction solveur_sudoku('[sudoku généré]') (résolution avec déduction des valeurs isolées) ou solveur_sudoku2('[sudoku généré]') (sans déduction des valeurs isolées) 

Par exemple : solveur_sudoku('64.8.....91.....8..876.9.24....7.8.......4......9..16..7.4..3.......7.1..9.1.8.7.,27,41,13,3,0,0,0,0,0,Intermediate,') affiche sur la console :
Sudoku initial :
 6 4 . | 8 . . | . . . 
 9 1 . | . . . | . 8 . 
 . 8 7 | 6 . 9 | . 2 4 
-------|-------|-------
 . . . | . 7 . | 8 . . 
 . . . | . . 4 | . . . 
 . . . | 9 . . | 1 6 . 
-------|-------|-------
 . 7 . | 4 . . | 3 . . 
 . . . | . . 7 | . 1 . 
 . 9 . | 1 . 8 | . 7 . 

Sudoku résolu :
 6 4 5 | 8 2 3 | 7 9 1 
 9 1 2 | 7 4 5 | 6 8 3 
 3 8 7 | 6 1 9 | 5 2 4 
-------|-------|-------
 5 6 9 | 3 7 1 | 8 4 2 
 1 2 8 | 5 6 4 | 9 3 7 
 7 3 4 | 9 8 2 | 1 6 5 
-------|-------|-------
 2 7 1 | 4 9 6 | 3 5 8 
 8 5 6 | 2 3 7 | 4 1 9 
 4 9 3 | 1 5 8 | 2 7 6 
