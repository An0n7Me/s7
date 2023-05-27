# s+7

Dans le cadre de la recherche de nouveau jeu de mots, les membres de l'Oulipo ont inventé un jeu dont le but est de remplacé tous les noms par le 7ieme nom suivant dans le dictionnaire.

J'ai automatisé cette regle grâce à un programme python. Dans un premier temps, dans le dossier `.\dico` on retrouve le dictionnaire source qui à été traités par le programme `extract.py` et sauvegardé dans le dossier `result`.
Ensuite, dans le programme `m.py`, il y a le programme qui permet d'automatisé ce règle d'ecriture.

## Requirement

 - sys
 - polygot (lien du repo : https://github.com/aboSamoor/polyglot)
 - PyICU & pycld2 (trouvez les sur : https://pypi.tuna.tsinghua.edu.cn/simple/mediapipe/)

## Installation

Pour telecharger le dossier : `git clone https://github.com/An0n7Me/s7 `

Pour installer Polyglot :
```
pip install PyICU-1.9.8-cp36-cp36m-win_amd64.whl
pip install pycld2-0.31-cp36-cp36m-win_amd64.whl
pip install git+https://github.com/aboSamoor/polyglot@master
```

Le module polyglot nécessite l'installation de langue qui serve de modèle pour reconnaitre la langue que l'on veut en l'occurence le français.
C'est poruquoi, on doit lancer le programme `download.py`une fois. En théorie, Normalement le programme est sensé afficher True à la dernière ligne.
Cependant, l'instruction n'a pas marché pour moi donc je vous laisse essayé. 

Ensuite, il faut mettre votre texte dans le dossier `t\` puis vous touverez le texte dans le dossier `\txtsp7`

