def esta_resuelto(cubo):
    for cara in cubo:
        if len(set(cara)) != 1:
            return False
    return True


cubo_resuelto = [
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y','Y']
]
print("Esta armado" if esta_resuelto(cubo_resuelto) else "No esta armado")


cubo_no_resuelto = [
    ['R', 'B', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['G', 'G', 'O', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['O', 'O', 'O', 'G', 'O', 'O', 'O', 'O', 'O'],
    ['W', 'W', 'W', 'W', 'Y', 'W', 'W', 'W', 'W'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'W', 'Y', 'Y','Y']
]
print("Esta armado" if esta_resuelto(cubo_no_resuelto) else "No esta armado")
