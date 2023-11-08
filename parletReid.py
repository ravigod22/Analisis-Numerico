import numpy as np

def parlett_reid(A):
    n = len(A)
    L = np.eye(n)
    T = A.copy()

    for k in range(n-2):
        x = T[k+1:,k]
        v = np.zeros_like(x)
        v[0] = np.sign(x[0]) * np.linalg.norm(x)
        v = v + x
        v = v / np.linalg.norm(v)

        T[k+1:, k:] = T[k+1:, k:] - 2 * np.outer(v, v.T @ T[k+1:, k:])
        T[:, k+1:] = T[:, k+1:] - 2 * np.outer(T[:, k+1:] @ v, v.T)

        L[k+1:,k] = v

    return L, np.diag(T.diagonal()) + np.diag(T.diagonal(-1), k=1) + np.diag(T.diagonal(-1), k=-1)

A = np.array([[0,1,2,3],
              [1,2,2,2],
              [2,2,3,3],
              [3,2,3,4]])

L, T = parlett_reid(A)
print(L)
print(T)