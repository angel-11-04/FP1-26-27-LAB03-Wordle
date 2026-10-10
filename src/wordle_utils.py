from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if cadena.isalpha():
        if len(cadena) == 5:
            return True
        else:
            return False
    else:
        return False

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    diferencia = fin - inicio
    total_seg = diferencia.total_seconds()
    total_min = int(total_seg//60)
    seg = int(total_seg%60)
    return total_min,seg

def quitar_letras(cadena: str, letra: str)->str:
    res = ""
    borra = True
    for i in cadena:
        if i == letra and borra == True:
            borra = False
        else:
            res = res + i
    return res
    
def marcar_verdes(palabra_secreta: str, intento: str)-> str:
    verdes = ""
    restantes = palabra_secreta
    for i in range(5):
        if palabra_secreta[i] == intento[i]:
            verdes = verdes + "V"
            restantes = quitar_letras(restantes, palabra_secreta[i])
        else:
            verdes = verdes + "_"

    return verdes, restantes

def marcar_amarillos(restantes:str,verdes:str,intento:str)->str:
    colores = ""
    for i in range(5):
        if verdes[i] == "V":
            colores += "V"
        else:
            if intento[i] in restantes:
                colores += "A"
                restantes = quitar_letras(restantes, intento[i])
            else:
                colores += "_"

    return colores

                



def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    verdes, restantes = marcar_verdes(palabra_secreta,intento)
    pistas = marcar_amarillos(restantes,verdes,intento)
    return pistas


