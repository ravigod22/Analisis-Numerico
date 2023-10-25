import numpy as np

from elemental_operations import row_eo
from substitution_methods import regressive

def augmented_matrix(A,b):
  r,c = A.shape
  M = np.zeros((r,c+1),float)
  for i in range(r):
    for j in range(c+1):
      M[i,j] = A[i,j] if j != c else b[i]
  return M

def gaussian_elimination(A,b):
  n = len(b)
  M = augmented_matrix(A,b)
  for i in range(n):
    # p is a pivot with a single constraint p!=0
    p = i
    for k in range(i,n):
      if M[k,i]!=0:
        p = k 
    if p == 0:
      return 'Sin solucion'
    if p != i:
    # elemental operation Fij
      row_eo([i,p],M,mode='Fij')
    # elemental operation kFij
    for j in range(i+1,n):
      k =  M[j,i]/M[i,i]
      row_eo([j,i,-k],M,mode='kFij')
  # regressive substitution
  # A = M[:,:n] y b = M[:,n:]
  x = regressive(M[:,:n] ,M[:,n:])
  return x

def main():
  # gaussian elimination
  A = np.array([[2,1,2],
                [0,1,2],
                [2,1,0]])
  b = np.array([[4],
                [3],
                [2]])
  print('Gaussian elimination')
  print('Matrix A\n',A)
  print('Matrix b\n',b)
  x = gaussian_elimination(A,b)
  print('Matrix x\n',x)

if __name__ == '__main__':
  main() 

