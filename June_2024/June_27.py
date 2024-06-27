# Toeplitz matrix

def isToeplitz(mat):
    if not mat:
        return 1

    rows = len(mat)
    cols = len(mat[0])

    for r in range(1, rows):
        for c in range(1, cols):
            if mat[r][c] != mat[r - 1][c - 1]:
                return 0

    return 1
