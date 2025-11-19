# Password Validator – Python / Tkinter

Cette application propose un validateur de mot de passe avec interface graphique, développé en **Python 3**, **Tkinter** et **Pillow**.  
Elle permet de saisir un utilisateur, vérifier la robustesse d’un mot de passe en temps réel, puis stocker et afficher ses versions hachées (SHA-256).

---

## Fonctionnalités

- Interface graphique (Tkinter) en plusieurs écrans  
- Saisie du nom d’utilisateur  
- Vérification dynamique des critères :
  - Longueur ≥ 8 caractères  
  - Au moins une minuscule  
  - Au moins une majuscule  
  - Au moins un chiffre  
  - Au moins un caractère spécial (`!@#$%^&*`)  
- Option pour afficher / masquer le mot de passe  
- Hashage SHA-256 et sauvegarde dans un fichier JSON
- Affichage optionnel des mots de passe hachés enregistrés  

---

## Prérequis

### Installation de Python 3  
- **Windows :** [Télécharger Python 3](https://www.python.org/downloads/windows/)  
- **macOS :** [Télécharger Python 3 pour macOS](https://www.python.org/downloads/macos/)  
- **Linux (source) :** [Télécharger les sources Python](https://www.python.org/downloads/source/)  

### Dépendances Python
Installer la librairie Pillow :

```bash
pip install pillow
```

### Installation du projet

1. **Cloner le projet**

```bash
git clone https://github.com/lorenzo-brissardnavarro/password-generator.git
cd password-validator
```

2. **Lancer le projet**
```bash
python3 main.py
```