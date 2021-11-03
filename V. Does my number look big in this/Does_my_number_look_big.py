def narcissistic(input):
    Num_a_sumar = []
    elevador = len(str(input))
    for number in str(input):
        Num_a_sumar.append(int(number)**elevador)
    if input == sum(Num_a_sumar):
        return True
    else:
        return False
