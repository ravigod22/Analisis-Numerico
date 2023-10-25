import numpy as np

def progressive(A,b):
  n = len(b)
  X = np.zeros((n,1), float)
  for i in range(n):
    # summation \sum_{j=0}^{i} a_{i,j}*x_{j}
    summation = 0
    for j in range(i):
      summation += A[i,j]*X[j]
    # end summation
    X[i] = (b[i] - summation)/A[i,i]
  return X

def regressive(A,b):
  n = len(b)
  X = np.zeros((n,1), float)
  for i in reversed(range(n)):
    # summation \sum_{j=i+1}^{n} a_{i,j}*x_{j}
    summation = 0
    for j in range(i+1,n):
      summation += A[i,j]*X[j]
    # end summation
    X[i] = (b[i] - summation)/A[i,i]
  return X

def main():
  # progressive substitution
  A = np.array([[2,0,0],
                [4,3,0],
                [2,1,1]])
  b = np.array([[1],
                [5],
                [6]])
  x = progressive(A,b) 
  print('progressive substitution\n',x)
  # regressive substitution
  A = np.array([[1,1,2],
                [0,3,4],
                [0,0,2]])
  b = np.array([[6],
                [5],
                [1]])
  x = regressive(A,b)
  print('regressive substitution\n',x) 
  
if __name__ == '__main__':
  main() 