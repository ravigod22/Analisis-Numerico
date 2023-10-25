import numpy as np

#for real matrices

def schur(A):
	pass

def svd(A):
	# this is a method created by me :P
	# we start from AV = UE
	# A.shape = E.shape = (m,n)
	# V.shape = U.shape = (m,m) 
	# U is not singular matrix -> exist U^(-1)
	# we also know V^T = V^(-1)
	# U^(-1)AV = E
	# U'A = EV^T
	# Step 1. find eigenvalues and eigenvectors with Y = A.A^T
	Y = np.dot(A,np.transpose(A))
	w, U = np.linalg.eig(Y)
	# Step 2. 
	sv = []
	for i in w:
		sv.append(np.sqrt(i)) 
	# Step 3.
	r,c = A.shape
	E = np.empty((r,c),float)
	for i in range(r):
		for j in range(c):
			if i==j:
				E[i,j] = sv[i]
			else:
				E[i,j] = 0
	# step 4.
	V = np.dot(np.linalg.inv(U),A)
	for i in range(r):
		V[i] = V[i]/sv[i]
	# step 5. rectangular case 
	if r != c:
		fix = []
		for j in range(c):
			summation = 0
			for i in range(r):
				summation += pow(V[i,j],2)
			fix.append(np.sqrt(1-summation))
		V = np.vstack((V,fix))
	V = np.transpose(V)
	return U,E,V

def parllet_reid(A):
	pass

def main():
	# svd decomposition
	A = np.array([[3,2,2],
				[2,3,-2]])
	U,E,V = svd(A)
	print('svd decomposition')
	print('Matrix A\n',A)
	print('Matrix U\n',U)
	print('Matrix E\n',E)
	print('Matrix V\n',V)

if __name__ == '__main__':
	main() 