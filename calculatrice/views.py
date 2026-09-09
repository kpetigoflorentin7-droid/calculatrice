from django.shortcuts import render
import math


def calculer(request):
    resultat = None
    operation_texte = None
    erreur = None

    if request.method == 'POST':
        operation = request.POST.get('operation')

        try:
            if operation == '1':  # Addition
                nbre1 = float(request.POST.get('nbre1'))
                nbre2 = float(request.POST.get('nbre2'))
                resultat = nbre1 + nbre2
                operation_texte = f"{nbre1} + {nbre2}"

            elif operation == '2':  # Soustraction
                nbre1 = float(request.POST.get('nbre1'))
                nbre2 = float(request.POST.get('nbre2'))
                resultat = nbre1 - nbre2
                operation_texte = f"{nbre1} - {nbre2}"

            elif operation == '3':  # Multiplication
                nbre1 = float(request.POST.get('nbre1'))
                nbre2 = float(request.POST.get('nbre2'))
                resultat = nbre1 * nbre2
                operation_texte = f"{nbre1} × {nbre2}"

            elif operation == '4':  # Modulo
                nbre1 = float(request.POST.get('nbre1'))
                nbre2 = float(request.POST.get('nbre2'))
                if nbre2 == 0:
                    erreur = "Modulo par zéro impossible"
                else:
                    resultat = nbre1 % nbre2
                    operation_texte = f"{nbre1} % {nbre2}"

            elif operation == '5':  # Pourcentage
                nbre1 = float(request.POST.get('nbre1'))  # nombre de base
                nbre2 = float(request.POST.get('nbre2'))  # pourcentage
                resultat = nbre1 * nbre2 / 100
                operation_texte = f"{nbre2}% de {nbre1}"

            elif operation == '6':  # Carré
                nbre1 = float(request.POST.get('nbre1'))
                resultat = nbre1 ** 2
                operation_texte = f"{nbre1}²"

            elif operation == '7':  # Cube
                nbre1 = float(request.POST.get('nbre1'))
                resultat = nbre1 ** 3
                operation_texte = f"{nbre1}³"

            elif operation == '8':  # Racine carrée
                nbre1 = float(request.POST.get('nbre1'))
                if nbre1 < 0:
                    erreur = "Impossible de calculer la racine carrée d'un nombre négatif"
                else:
                    resultat = math.sqrt(nbre1)
                    operation_texte = f"√{nbre1}"

            elif operation == '9':  # Factorielle
                nbre1 = float(request.POST.get('nbre1'))
                if nbre1 < 0 or not nbre1.is_integer():
                    erreur = "La factorielle exige un nombre entier positif"
                else:
                    resultat = math.factorial(int(nbre1))
                    operation_texte = f"{int(nbre1)}!"

            elif operation == '10':  # Sinus (en degrés)
                nbre1 = float(request.POST.get('nbre1'))
                resultat = math.sin(math.radians(nbre1))
                operation_texte = f"sin({nbre1}°)"

            elif operation == '11':  # Cosinus (en degrés)
                nbre1 = float(request.POST.get('nbre1'))
                resultat = math.cos(math.radians(nbre1))
                operation_texte = f"cos({nbre1}°)"

            else:
                erreur = "Opération inexistante, choisissez un numéro entre 1 et 11"

        except (ValueError, TypeError):
            erreur = "erreur veuillez revérifier svp"

    return render(request, 'calculatrice/calculatrice.html', {
        'resultat': resultat,
        'operation_texte': operation_texte,
        'erreur': erreur
    })