import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    row = len(a)
    cols = len(a[0])
    result =[[0]*row for _ in range(cols)]
    for i in range(row):
        for j in range(cols):
            result[j][i]=a[i][j]
    return result
    pass