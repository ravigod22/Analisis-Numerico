import numpy as np
def metodoRichardson(a, x):
    TOL = 1E-3; MAX_ITER = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    t=x.copy()
    criterio=np.linalg.norm(np.array(x)-np.array(t),np.inf)
    while(cambio_rel>TOL) and (cont<MAX_ITER):
        print("x=["+(" "*4).join(list(map('{:5.3f}'.format,x)))+"]")
        for i in range(n):
            y[i] = x[i] - np.dot(a[i,:], x[:]) + b[i]
        cambio_rel = np.linalg.norm(x-y, np.inf)/np.linalg.norm(y,np.inf)
        x[:] = y[:]
        cont+=1
    print("x=["+(" "*4).join(list(map('{:5.3f}'.format,x)))+"]")
    if cambio_rel<=TOL:
        print("Metodo converge")
    else:
        print("Metodo no converge")
    print(f"Metodo terminado en {cont} iteraciones. ||x-y||/||y|| = {criterio:5.3f}")
    return (x, criterio, cont)
n = 3
a = np.array([0.5, -0.2, 0.5, 0.1, 0.6, 0.4, -0.3, 0.1, 0.0], dtype = 'f4')
a = np.reshape(a,(n,n))
b = np.array([-1, 6.5, 0.7], dtype='f4')
x = np.array([0, 0, 0],dtype= 'f4')
(x, criterio, cont)= metodoRichardson(a,x)
    
    
