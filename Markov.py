import numpy as np

def are_matrices_similar(matrix1, matrix2, t):
    # 检查两个矩阵是否在误差t范围内相似
    if matrix1.shape != matrix2.shape:
        return False
    diff = np.abs(matrix1 - matrix2)
    if np.all(diff < t):
        return True
    else:
        return False

def converge_within_n_rounds(state, matrix, n):
    # 检查状态是否在n轮内收敛
    for i in range(n):
        temp = state @ matrix  # 矩阵乘法
        if are_matrices_similar(temp, state, 1e-30):  # 用一个极小误差来判断收敛
            return True, i + 1
        else:
            state = temp
    return False, -1
