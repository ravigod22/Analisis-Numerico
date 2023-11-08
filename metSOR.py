import numpy as np

def SOR(A,b):
    print("====> METODO SOR <====")
    TOL=1e-4
    e_rel = 1
    w = 1.25
    x=np.array([1,1,1])

    D = np.diag(np.diag(A)); 
    E=-(np.tril(A)-D); F=-(np.triu(A)-D)
    Gw = np.linalg.inv(D-w*E)@((1-w)*D+w*F)
    c = w*np.linalg.inv(D-w*E)@b

    print("Parametros:\tTOL:", TOL, "\tw:", w, "\tx_0 = ", x)
    print("Matriz G(w):\n",Gw)
    print("--------------------------------------------------------------------------------------------------")
    k = 1
    while e_rel>TOL:
        x_prev = x
        x = Gw@x_prev + c
        e_rel = np.linalg.norm(x_prev-x,np.inf) / np.linalg.norm(x_prev,np.inf)
        
        print("k =",k,"\t\tx = ", x, "\t\t Error = ", e_rel)
        k+=1 

#------------------------------
A=np.array([[4,3,0],
            [3,4,-1],
            [0,-1,4]])
b=np.array([24,30,-24])
SOR(A,b)