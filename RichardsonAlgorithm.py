import numpy as np

def metodoRichardson(a, x, b):
    TOL = 1e-3; MAX_ITER = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    n = x.shape[0]
    while (cambio_rel > TOL) and (cont < MAX_ITER):
        print("x=[" + " ".join(list(map('{:5.3f}'.format, x))) + "]")
        for i in range(n):
            y[i] = x[i] - np.dot(a[i,:], x[:]) + b[i]
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
