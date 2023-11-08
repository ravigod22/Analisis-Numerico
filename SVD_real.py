import numpy as np

def mostrarMatriz(A):
    n,m = A.shape
    for i in range(0,n):
        strMatr = "[\t"
        for j in range(0,m):
            strMatr +=  str(A[i][j])+"\t"
        strMatr += "]"
        print(strMatr)

def descomposicionSVD(A):
	# Hallamos B = A x A^t 
	B = np.dot(A,np.transpose(A)) 
	# Hallamos los autovalores en ll y guardamos los autovectores normalizados en U
	ll, U = np.linalg.eig(B)
	# Hallamos los valores singulares s_o = σ = sqrt(l-autovalor)    
	s_o = []
	for i in ll:
		s_o.append(np.sqrt(i)) 
	# Hallamos Σ = E 
	nFilas, nColumnas = A.shape
	E = np.empty((nFilas, nColumnas),float)
	for i in range(nFilas):
		for j in range(nColumnas):
			if i==j:
				E[i,j] = s_o[i]
			else:
				E[i,j] = 0
	# Hallamos V a partir de AV = UE
	V = np.dot(np.linalg.inv(U),A)
	for i in range(nFilas):
		V[i] = V[i]/s_o[i]
	# step 5. rectangular case 
	if nFilas != nColumnas:
		fix = []
		for j in range(nColumnas):
			summation = 0
			for i in range(nFilas):
				summation += pow(V[i,j],2)
			fix.append(np.sqrt(1-summation))
		V = np.vstack((V,fix))
	V = np.transpose(V)
	return U,E,V

### ----------------------------------------- ###
A = np.array([[1,2,0],
			  [2,0,2]])
U,E,V = descomposicionSVD(A)
print('Descomposicion SVD:')
print('Matriz A\n',A)
print('Matriz U\n',U)
print('Matriz E\n',E)
print('Matriz V\n',V)