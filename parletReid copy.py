import numpy as np
def mostrarMatriz(A):
    n,m = A.shape
    for i in range(0,n):
        strMatr = "[\t"
        for j in range(0,m):
            strMatr +=  str(round(A[i][j],3))+"\t"
        strMatr += "]"
        print(strMatr)
def mostrarVector(v):
    s = "[\t"
    for i in range (0,len(v)):
        s += str(round(v[i],3)) + "\t"
    s += "]"
    print(s)

def metParlettReid(A, n):
    T = A
    PP = np.array([])
    MM = np.array([])
    print("---------------------- Parlett-Reid ----------------------")
    for k in range (1,n-1):
        print("\n => k : ", k, "\n" )
        P = np.eye(n)
        idx = np.arange(0,n)
        i_max = k
        for i in range (k,n):
            if (T[i_max][k-1] < T[i][k-1]):
                i_max = i
        P[[i_max,k]] = P[[k,i_max]]
        idx[i_max], idx[k] = idx[k], idx[i_max]
        a = np.zeros(n)
        e = np.zeros(n)
        e[k] = 1
        for i in range (k+1, n):
            a[i] = T[idx[i], k-1] / T[idx[k],k-1]
        M = np.eye(n) - np.outer(a, e)
        T = np.dot(np.dot(np.dot(np.dot(M, P), T), np.transpose(P)), np.transpose(M))
        #print(np.outer(a, e))
        print("alpha: ",end="")
        mostrarVector(a)

        print("P: [ ", end="")
        for i in range (n):
            for j in range (n):
                if (P[i][j] == 1):
                    print("e" + str(j+1), end=" ")
        print("]")
        
        print("--------------- MATRIZ M -----------")
        mostrarMatriz(M)
        print("--------------- MATRIZ T -----------")
        mostrarMatriz(T)
        PP = np.append(PP,P)
        MM = np.append(MM,M)
   
    P = np.eye(n)
    for i in range(len(PP)-1, -1, -1):
        P = np.dot(P, PP[i])
    L = np.eye(n)
    for i in range(len(PP)-1, -1, -1):
        L = np.dot(L, MM[i])
        L = np.dot(L,PP[i])
    L = np.dot(L,np.transpose(P))
    L = np.linalg.inv(L)
    return L,T

# ---------------------------------------------

# A simetrica e indefinida
A = np.array([[0,1,2,3],
              [1,2,2,2],
              [2,2,3,3],
              [3,2,3,4]])

L,T = metParlettReid(A, len(A))

print("\n\n--------------------------- RESULTADOS --------------------------- ")
print("Matriz: L")
mostrarMatriz(L)
print("Matriz: T")
mostrarMatriz(T)
print("Matriz: L^t")
mostrarMatriz(np.transpose(L))


