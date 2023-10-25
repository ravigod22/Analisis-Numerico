import numpy as np

from partial_pivot import partial_pivot
from elemental_operations import row_eo

def lu_validation(A):
  n = len(A)
  for i in range(n):
    if np.linalg.det(A[:i,:i]) == 0:
      return False
  return True

def palu(A):
  n = len(A)
  P = np.eye(n)
  L = np.eye(n)
  Log,U = partial_pivot(A)
  for R in Log:
    if R[1] == 'Fij':
      data = R[0]
      row_eo(data,P,mode='Fij')
  for R in reversed(Log):
    if R[1] == 'kFij':
      data = R[0]
      data[2] = (-1)*data[2]
      row_eo(data,L,mode='kFij')
  return P,L,U

def crout(A):
  n = len(A)
  U = np.eye(n)
  L = np.zeros((n,n))
  for j in range(n):
    for i in range(j):
      summation = 0
      for k in range(i):
        summation += L[i,k]*U[k,j]
      U[i,j] = (A[i,j]-summation)/L[i,i]
    for i in range(j,n):
      summation = 0
      for k in range(j):
        summation += L[i,k]*U[k,j]
      L[i,j] = (A[i,j]-summation)/U[j,j]
  return L,U

def doolittle(A):
  n = len(A)
  L = np.eye(n)
  U = np.zeros((n,n))
  for i in range(n):
    for j in range(i):
      summation = 0
      for k in range(j):
        summation += L[i,k]*U[k,j]
      L[i,j] = (A[i,j]-summation)/U[j,j]
    for j in range(i,n):
      summation = 0
      for k in range(i):
        summation += L[i,k]*U[k,j]
      U[i,j] = (A[i,j]-summation)/L[i,i]
  return L,U

def cholesky(A):
  n = len(A)
  L = np.zeros((n, n),float)
  for j in range(n):
    # summation \sum_{k=0}^{j} l_{j,k}^2
    summation = 0
    for k in range(j):
      summation += pow(L[j,k],2)
    # where l_{j,j} = \sqrt{a_{j,j}-\sum_{k=0}^{j} l_{j,k}^2}
    L[j,j] = np.sqrt(A[j,j]-summation)
    for i in range(j+1,n):
      # summation \sum_{k=0}^{j} l_{i,k}*l_{j,k}
      summation=0
      for k in range(j):
        summation += L[i,k]*L[j,k]
    # where l_{i,j} = \fracc{{a_{i,j}-\sum_{k=0}^{j} l_{i,k}*l_{j,k}}{l_{j,j}}
      L[i,j] = (A[i,j]-summation)/L[j,j]
  return L

def main():
  # PA = LU factorization
  A = np.array([[2,1,2],
                [0,1,2],
                [2,1,0]])
  P,L,U = palu(A)
  print('\nPA = LU factorization')
  if not np.array_equal(P,np.eye(len(A))):
    print('Matrix P\n',P)
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix U\n',U)
  # crout factorization
  L,U = crout(A)
  print('\nCrout factorization')
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix U\n',U)
  # doolittle factorization
  L,U = doolittle(A)
  print('\nDoolittle factorization')
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix U\n',U)
  # cholesky factorization
  A = np.array([[4,0,1],
                [0,4,1],
                [1,1,4]])
  L = cholesky(A)
  print('\nCholesky factorization')
  print('Matrix A\n',A)
  print('Matrix L\n',L)
  print('Matrix L^t\n',np.transpose(L))
  
  
if __name__ == '__main__':
  main() 
