from numpy import linalg as la
import numpy as np

def mostrarMatriz(A):
    for v_fila in A:
        print("\t\t\t\t\t[\t{}\t]".format("\t".join("{:.4f}".format(x) for x in v_fila)))
    print()

def mostrarIteracion(x_kk, k, e):
    print("x^({}) = ".format(k), 
          "[\t" + "\t".join("{:.15f}".format(x) for x in x_kk) + "\t]", "\t\t e = ", e)

def metGaussJacobi(A,b):
    datos = ["GAUSS - JACOBI", "M = D^-1 (L+U)", "c = D^-1 b"]   
    D = np.zeros_like(A)
    np.fill_diagonal(D, np.diag(A))   
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)
    
    M = np.dot(la.inv(D), L + U)
    c = np.dot(la.inv(D), b)
    return M,c,datos

def metJacobiRichardson(A,b):
    datos = ["JACOBI - RICHARDSON", "M = I - D^-1 A", "c = D^-1 b"]   
    D = np.zeros_like(A)
    np.fill_diagonal(D, np.diag(A))   
    
    M = np.eye(len(A)) - np.dot(la.inv(D), A)
    c = np.dot(la.inv(D), b)
    return M,c,datos

def metRichardson(A,b):
    datos = ["RICHARDSON", "M = (I-A)", "c = b"]
    M = np.eye(len(A)) - A
    c = b
    return M,c,datos


def metGaussSeidel(A,b):
    datos = ["GAUSS - SIEDEL", "M = (D-L)^-1 U", "c = (D-L)^-1 b"]
    D = np.zeros_like(A)
    np.fill_diagonal(D, np.diag(A))   
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)
    
    M = np.dot(la.inv(D-L), U)
    c = np.dot(la.inv(D-L), b)

    return M,c,datos

def metIterativo(A,b):
    M,c,datos = metGaussSeidel(A,b)
    print("--------------------------------------- METODO", datos[0],  "--------------------------------------")
    print("Esquema iterativo: x^(k+1) = M x^(k) + c")
    
    print("\n =>  Matriz de Iteración: ", datos[1])
    mostrarMatriz(M)
    print(" =>  Vector de coeficientes: ", datos[2])

    for elemento in c:
        print("\t\t\t\t\t\t[  {:.5f}".format(elemento)," ]")
    
    p_M = max(abs(la.eigvals(M)))
    print("\nRadio espectral: ", p_M)
    if (p_M < 1):
        print(" => El Método CONVERGE")
        print("----------------------------------------------- Iteraciones ----------------------------------------------\n")
        cambio_rel = float('inf') 
        k = 1
        TOL = 1e-5
        x_k = np.zeros(len(A))
        mostrarIteracion(x_k, 0, cambio_rel)
        while(cambio_rel > TOL):
            x_kk = np.dot(M,x_k) + c
            mostrarIteracion(x_kk, k, cambio_rel)       
            if la.norm(x_k, ord=np.inf) != 0 :
                cambio_rel = la.norm(x_kk - x_k) / la.norm(x_k, ord=np.inf)
            else : 
                cambio_rel = float('inf')
            x_k = x_kk
            k+=1
    else:
        print(" => El Método NO CONVERGE")
    
    


np.set_printoptions(precision=15)

A = np.array([[4,1,2],
              [3,1,4],
              [5,1,3]])
b = np.array([40,53,51])


metIterativo(A,b)