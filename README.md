# Calculatrice Django

## Présentation

Application web simple développée avec Django permettant d'effectuer différentes opérations mathématiques via une interface unique avec un menu déroulant numéroté.

## Objectif

Ce projet a été réalisé dans un but pédagogique, pour apprendre les bases de Django : vues, templates, formulaires POST, gestion des erreurs.

## Fonctionnalités

- Menu numéroté de 1 à 11 pour choisir l'opération
- Affichage de l'opération effectuée en plus du résultat (ex : `15 + 8 = 23`)
- Gestion des erreurs (saisie invalide, division par zéro, racine négative, factorielle invalide, opération inexistante)
- Interface adaptée automatiquement selon l'opération choisie (le deuxième champ se cache pour les opérations à un seul nombre)


## Installation

```bash
python -m pip install django
```

## Exécution

```bash
python manage.py migrate
python manage.py runserver
```

Puis ouvrir `http://127.0.0.1:8000/` dans un navigateur.

## Utilisation

1. Choisir une opération dans le menu déroulant (numéro 1 à 11)
2. Renseigner le ou les nombres demandés
3. Cliquer sur "Calculer"
4. Le résultat s'affiche avec l'opération correspondante

## Gestion des erreurs

- **Saisie non numérique** → "Veuillez entrer des nombres valides"
- **Division par zéro** → "Division par zéro impossible"
- **Racine carrée d'un nombre négatif** → "Impossible de calculer la racine carrée d'un nombre négatif"
- **Factorielle d'un nombre négatif ou non entier** → "La factorielle exige un nombre entier positif"
- **Numéro d'opération invalide** → "Opération inexistante, choisissez un numéro entre 1 et 11""# calculatrice" 
