import numpy as np
import SolveTriangular as st

def gauss_seidel(A,b,x0,toll,it_max):   # Definisce la funzione che implementa il metodo iterativo di Gauss-Seidel

    errore=1+toll                      # Inizializza l'errore con un valore maggiore di toll per entrare nel ciclo

    d= np.diag(A)
    D= np.diag(d)

    E= np.tril(A, -1)
    F= np.triu(A, 1)

    M= D + E # TODO  
    N= -F  # TODO
    
    T= np.linalg.inv(M) @ N # TODO: Costruisce la matrice di iterazione di Gauss-Seidel

    autovalori=np.linalg.eigvals(T)     # Calcola gli autovalori della matrice di iterazione
    raggiospettrale= np.max(np.abs(autovalori))  # Calcola il raggio spettrale 

    print("raggio spettrale Gauss-Seidel ",raggiospettrale) # Stampa il raggio spettrale

    it=0                                # Inizializza il contatore delle iterazioni

    er_vet=[]                           # Lista per salvare l'errore a ogni iterazione

    while it<=it_max and errore>=toll: #to do

        

        x, _ = st.Lsolve(M, b + N @ x0) #to do 

        errore= np.linalg.norm(x - x0) / np.linalg.norm(x) # to do Calcola l'errore relativo tra due iterazioni successive

        er_vet.append(errore)           # Salva l'errore corrente

        x0=x.copy()                     # Aggiorna la soluzione per l'iterazione successiva

        it=it+1                         # Incrementa il contatore delle iterazioni

    return x,it,er_vet                  # Restituisce: soluzione approssimata, numero iterazioni, vettore errori
