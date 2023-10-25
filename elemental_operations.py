import numpy as np

def row_eo(data,A,mode):
  # dato[0] = i
  # dato[1] = j
  # intercambiar filas i con j
  if len(data)==2 and mode == 'Fij':
    aux = np.copy(A[data[0]])
    A[data[0]] = A[data[1]]
    A[data[1]] = aux
  # dato[0] = i
  # dato[1] = k
  # multiplicacion de fila i por k
  elif len(data)==2 and  mode == 'kFi':
    A[data[0]] = A[data[0]]*data[1]
  # dato[0] = i
  # dato[1] = j
  # dato[2] = k
  # sumar la fila j multiplicado por k veces la fila i
  elif len(data)==3 and mode == 'kFij':
    A[data[0]] += A[data[1]]*data[2]
  return data, mode

def main():
  A = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
  print('Matrix A\n',A)
  # modo Fij
  row_eo([0,1],A,mode='Fij')
  print('Operacion elemental R01A\n',A)
  # modo kFi
  row_eo([0,2],A,mode='Fi')
  print('Operacion elemental 2*R0A\n',A)
  # modo kRij
  row_eo([1,2,2],A,mode='Fij')
  print('Operacion elemental 2*R_12_A\n',A)

if __name__ == '__main__':
  main() 
