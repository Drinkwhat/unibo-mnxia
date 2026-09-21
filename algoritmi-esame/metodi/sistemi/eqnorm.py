import numpy as np
import SolveTriangular as st
import scipy.linalg as spl

def eqnorm(A: np.matrix, b: np.typing.ArrayLike):
    
    #matrice delle equazioni normali 
    G = A.T @ A # TODO 

    cond_G = np.linalg.cond(G) # TODO: indice di condizionamento di G

    print(f"Condizionamento eqnorm: {cond_G}")

    # Costruisce il termine noto delle equazioni normali:
    f = A.T @ b # TODO

    # Applica la fattorizzazione di Cholesky alla matrice G e la utilizza per risolve il sistema Gx=f 
    
    l = spl.cholesky(G, lower = True) # TODO: Matrice triangolare inferiore
    
    lt = l.T # TODO

    z, flag = st.Lsolve(l, f) # TODO
    if flag != 0:
        return [], flag

    x, flag = st.Usolve(lt, z) # TODO

    return x