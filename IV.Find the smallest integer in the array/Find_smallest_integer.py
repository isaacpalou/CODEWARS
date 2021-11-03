# Primera solución:
def find_smallest_int(list):
    sorted_numbers = sorted(list)
    return sorted_numbers[0]
# Solución refactorizada después de descubrir la funcion min():


def find_smallest_int(list):
    return min(list)
