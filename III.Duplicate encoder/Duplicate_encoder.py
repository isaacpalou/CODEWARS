def duplicate_encode(palabra):
    complete_String = ""
    palabra = palabra.lower()
    for letra in palabra:
        if palabra.count(letra) != 1:
            complete_String += ")"
        else:
            complete_String += "("
    return complete_String
