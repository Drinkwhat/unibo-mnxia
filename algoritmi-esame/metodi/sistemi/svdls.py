import numpy as np
import scipy.linalg as spLin

def SVDLS(A, b):
    # La funzione risolve il problema ai minimi quadrati:
    #
    #       Ax ≈ b
    #
    # utilizzando la decomposizione ai valori singolari, cioè la SVD.
    # Questo metodo è particolarmente stabile dal punto di vista numerico,
    # soprattutto quando la matrice A è mal condizionata.

    # Si ricavano le dimensioni della matrice A.
    # m è il numero di righe, cioè il numero di dati disponibili.
    # n è il numero di colonne, cioè il numero di incognite del problema.
    m, n = A.shape

    # Si calcola la decomposizione ai valori singolari della matrice A:
    #
    #       A = U Σ V^T
    #
    # dove U e V sono matrici ortogonali, mentre Σ è una matrice diagonale
    # contenente i valori singolari.
    #
    # La funzione spLin.svd(A) restituisce:
    # - U: matrice dei vettori singolari sinistri;
    # - s: array monodimensionale contenente i valori singolari;
    # - VT: matrice V trasposta.
    U, s, VT = spLin.svd(A)
 
    V = VT.T

    # Si definisce una soglia numerica per stabilire quali valori singolari
    # sono effettivamente significativi.
    #
    # np.spacing(1) rappresenta circa la precisione di macchina.
    # La soglia dipende anche dal numero di righe m e dal valore singolare
    # massimo s[0].
    thresh = np.spacing(1) * m * s[0]

    # Si calcola il rango numerico della matrice A contando quanti valori
    # singolari sono maggiori della soglia.
    #
    # I valori singolari troppo piccoli vengono trascurati perché potrebbero
    # causare instabilità numerica, amplificando gli errori di arrotondamento.
    k = np.count_nonzero(s > thresh)
    print("rango=", k)

     
    d: np.matrix = U.T @ b # TODO: Cambio cordinate vettore b

    # Si considerano solo le prime k componenti di d, cioè quelle associate
    # ai valori singolari significativi.
    d1 = d[:k].reshape(k, 1) # TODO 

    # Si considerano allo stesso modo solo i primi k valori singolari.
    s1 = s[:k].reshape(k, 1) # TODO

    c = d1 / s1 #to do 

    
    x = V[:, :k] @ c

    
    residuo = np.linalg.norm(d[k:]) ** 2 #to do 

    # La funzione restituisce:
    # - x: il vettore dei coefficienti della soluzione;
    # - residuo: l'errore quadratico associato all'approssimazione.
    return x, residuo