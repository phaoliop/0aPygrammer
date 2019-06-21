import numpy as np


def validSolution(board):

    b = np.array(board)
    for i in range(9):

        #Valida fila o columna
        if (0 in b[i,:]) or (0 in b[:,i]) or len(set(b[i,:]))!=9 or len(set(b[:,i]))!=9:
            return False

        #Valida submatriz
        c = b[3*int((i/3)):int(3*(i/3))+3, int(3*(i%3)):int(3*(i%3)+3)]
        d = []
        for sc in c:
            d+=[dato for dato in sc]

        if (0 in d) or (len(set(d)) != 9): return False
    return True