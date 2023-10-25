import numpy as np

def jacobi(A,b,x_0,i):
	# A = U + L + D
	D = np.diag(np.diag(A))
	U = np.triu(A)-D
	L = np.tril(A)-D
	Dinv = np.linalg.inv(D)
	# x^k+1 = D'b-D'(L+U)x^k
	iteration = 0
	x_k = x_0
	while iteration < i:
		Rx = np.dot(L+U,x_k) 
		x_k = np.dot(Dinv,b) - np.dot(Dinv,Rx)
		iteration += 1 
	return x_k

def gauss_seidel(A,b,x_0,i):
	# A = U + D + L
	D = np.diag(np.diag(A))
	U = np.triu(A)-D
	L = np.tril(A)-D
	DLinv = np.linalg.inv(D+L)
	# x^k+1 = -(D+L)'Ux^k + (D+L)'b
	iteration = 0
	x_k = x_0
	while iteration < i:
		RU = np.dot(DLinv,U) 
		x_k = -np.dot(RU,x_k) + np.dot(DLinv,b)
		iteration += 1 
	return x_k

def attached_conjugate(A,b,x0,i):
	pass

def main():
	# jacobi iteration method 
	A = np.array([[2,0,-1],
                [-2,-10,0],
                [-1,-1,4]])
	b = np.array([[1],
                [-12],
                [2]])
	x_0 = np.array([[0],
                [0],
                [0]])
	x = jacobi(A,b,x_0,2)
	print('Jacobi method\n',x)
	# gauss-seidel iteration method 
	x = gauss_seidel(A,b,x_0,1)
	print('Gauss-Seidel method\n',x)
  

if __name__ == '__main__':
 	main() 