import numpy as np

def metodoJacobi(a, x, b):
    TOL = 1e-3; MAX_ITER = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    n = x.shape[0]  # Tamaño de la matriz

    while (cambio_rel > TOL) and (cont < MAX_ITER):
        print("x=[" + " ".join(list(map('{:5.3f}'.format, x))) + "]")
        for i in range(n):
            idx = [j for j in range(n) if j != i]
            y[i] = (b[i] - np.dot(a[i, idx], x[idx])) / a[i, i]
        cambio_rel = np.linalg.norm(x-y, np.inf) / np.linalg.norm(y, np.inf)
        x[:] = y[:]
        cont += 1

    print("x=[" + " ".join(list(map('{:5.3f}'.format, x))) + "]")
    if cambio_rel <= TOL:
        print("Metodo converge")
    else:
        print("Metodo no converge")

    print(f"Metodo terminado en {cont} iteraciones. ||x-y||/||y|| = {cambio_rel:5.3f}")
    return (x, cambio_rel, cont)

a_input = np.array([[10,1],[2,10]],dtype='f4')
b_input = np.array([11,12],dtype='f4')
x = np.zeros(b_input.shape,dtype='f4')

(x ,criterio ,cont) = metodoJacobi(a_input,x,b_input)

