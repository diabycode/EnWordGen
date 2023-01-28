# EnWordGen

![image](https://user-images.githubusercontent.com/97140632/215263594-6173d858-5bd2-485d-bba1-20ebfd64594a.png)


**EnWordGen**, un generateur de verbe anglais. 

Cette application s’appuie sur une mini base de donnée au format json et vous génère de manière aléatoire un verbe anglais à chaque démarrage. Elle vous offre des infos comme le prétérit, le participe passé et la traduction en francais du verbe généré. Pratique pour tout amateur apprenant l’anglais.


**fonctionnalités** 

- Interface graphique
- Deux thèmes gérés (sombre/clair)
- +110 verbes disponibles


**Outils utilisés** 

Python & Kivy


**Installation et utilisation** 

<aside>
💡 Notez que la méthode d’installation proposée est celle qui marche pour Windows. Alors n’hésitez pas à faire quelques recherches pour trouver l’équivalent si vous êtes sur un autre système. Aussi assurez-vous d’utiliser python3 pour l'installation.

</aside>

- Ouvrez un nouveau terminal
- Cloner le repo chez vous avec la syntaxe:
    
    ```bash
    git clone <lien du repo>
    ```
    
- Un nouveau dossier sera créé dans le répertoire courant (EnWordGen). Rendez-vous à l’intérieur avec la syntaxe:
    
    ```bash
    cd .\EnWordGen
    ```
    
- Créer un nouvel environnement virtuel python
    
    ```bash
    python -m venv env
    ```
    
- Activer l’environnement virtuel
    
    ```bash
    .\env\Script\activate
    ```
    
- Installer les dépendances
    
    ```bash
    pip install -r requirements.txt
    ```
    
- Exécution de l’app
    
    ```bash
    python .\main.py
    ```
    

<aside>
💡 Pour afficher les différents infos vous juste qu'a faire un clic sur la zone juste sous le verbe.
Aussi, si vous modifiez le thème, la modification sera prise en compte au prochain démarrage.

</aside>
