from django.core.exceptions import PermissionDenied
from django.http import Http404

MESSAGE_SUCCESS = 'SUCCES'
MESSAGE_FATAL = "FATAL"
MESSAGE_WARNING = 'WARNING'
RESULAT = 'resultat'
MESSAGE_RETOUR = 'message'
CHAMP_ERREUR = 'champs_erreur'

def erreur404(message="La ressource demandée n'existe pas !"):
    raise Http404(message)

def erreur403(message="La ressource demandée n'existe pas !"):
    raise PermissionDenied("Vous n'êtes pas autorisé à utiliser cette page")

def reponseSucces(message):
    response_data = {
        RESULAT: MESSAGE_SUCCESS,
        MESSAGE_RETOUR: message
    }
    return response_data


def reponseWarning(message):
    response_data = {
        RESULAT: MESSAGE_WARNING,
        MESSAGE_RETOUR: message
    }
    return response_data


def reponseFatal(message):
    response_data = {
        RESULAT: MESSAGE_FATAL,
        MESSAGE_RETOUR: message
    }
    return response_data

def formatEmail(email):
    try:
        emails = email.strip()
    except Exception as e:
        print(e)
        emails = email
    # regex = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[\.]\w{2,3}$'
    # regex = '^[a-z0-9A-Z]+[\._\-]?[a-z0-9A-Z]+[\._\-]?[a-z0-9A-Z]+[@]\w+[a-z0-9A-Z]*[\._\-]?[a-zA-Z0-9]*[.]\w{2,4}$'
    regex = r'^[a-z0-9A-Z]+[\._\-]?[a-z0-9A-Z]+[\._\-]?[a-z0-9A-Z]+[@]\w+[a-z0-9A-Z]*[\._\-]?[a-zA-Z0-9]*[.]\w{2,4}$'

    if (re.search(regex, emails)):
        return True, emails
    return False ,emails

def isGood_Password(text,min_taille=8, char = ['majuscule','minuscule','symbole','chiffre']):
    # print('--code psw:',text,min_taille,char)

    message = ''
    erreur = 'le mot de passe doit avoir au moins '
    majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    # print('--minuscules:',minuscules)

    chiffres = '0123456789'
    symbole = "+!@-$_"
    # ======================== Message
    if 'majuscule' in char:
        erreur += "une lettre majuscule [A-Z], "
    if 'minuscule' in char:
        erreur += "une lettre minuscule [a-z], "
    if 'chiffre' in char:
        erreur += "un chiffre [0-9], "
    if 'symbole' in char:
        erreur += "un caractère spécial [+!@-$_], "


    M = False
    m = False
    c = False
    s = False

    valide = False
    if len(text) < 8:
        message = f'il faut au moin {min_taille} Charatères pour le mot de passe'
        return valide,message

    for i in text:
        if 'majuscule' in char and i in majuscules:
            # print(" majus:", i)
            M = True
        elif 'minuscule' in char and i in minuscules:
            # print(" minus:",i)
            m = True
        elif 'chiffre' in char and i in chiffres:
            # print(" chiffre:", i)
            c = True
        elif 'symbole' in char and i in symbole:
            # print(" symbole:", i)
            s = True

    for g in char:
        if g == 'majuscule' and M == False:
            return valide , "le mot de passe doit avoir au moins une lettre majuscule [A-Z]"
        elif g == 'minuscule' and m == False:
            return valide, "le mot de passe doit avoir au moins une lettre en minuscule [a-z]"
        elif g == 'chiffre' and c == False:
            return valide, "le mot de passe doit avoir au moins un chiffre [0-9]"
        elif g == 'symbole' and s == False:
            return valide, "le mot de passe doit avoir au moins un symbole [+!@-$_]"

    return True,'Mot de passe Correct'

# def handler404(request, exception=None):
#     message = exception.args[0] if exception and exception.args else "La ressource demandée n'existe pas !"
#     return render(request, 'templates/profiles/404.html', {'message': message, 'erreur': 4}, status=404)
#     # return render(request, 'templates/profiles/404.html', status=404)
#
# def handler403(request, exception):
#     message = exception.args[0] if exception and exception.args else "Vous n'êtes pas autorisé à utiliser cette page"
#     return render(request, 'templates/profiles/404.html', {'message': message, 'erreur': 3}, status=403)
    # return render(request, 'templates/profiles/404.html', status=403)