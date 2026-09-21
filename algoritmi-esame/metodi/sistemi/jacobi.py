import numpy as np

def jacobi(A,b,x0,toll,it_max):          # Definisce una funzione che applica il metodo iterativo di Jacobi
    errore= 1+toll                       

    d = np.diag(A) # TODO                        
    D = np.diag(d) # TODO 
    n=A.shape[0]                         
    
    E = np.tril(A, -1) # TODO 
    F = np.triu(A, 1) # TODO 

    M = D # TODO 
    N = -(E + F) # TODO 
    
    T = np.linalg.inv(M) @ N # TODO 

    autovalori = np.linalg.eigvals(T)     # Calcola gli autovalori della matrice di iterazione T
    raggiospettrale =  np.max(np.abs(autovalori)) # TODO: Il massimo degli autovalori # Calcola il raggio spettrale

    print("raggio spettrale jacobi", raggiospettrale) # Stampa il raggio spettrale

    it=0                                # Inizializza il contatore delle iterazioni

    er_vet=[]                           # Crea una lista vuota per salvare gli errori a ogni iterazione

    while it<=it_max and errore>=toll: # TODO

        x = (b + N @ x0) / d.reshape(n, 1) # TODO       # Calcola la nuova approssimazione x con la formula di Jacobi
    
        errore = np.linalg.norm(x - x0) / np.linalg.norm(x) # TODO # Calcola l'errore relativo tra due iterazioni successive

        er_vet.append(errore)           # Aggiunge l'errore corrente alla lista degli errori

        x0=x.copy()                     # Aggiorna x0 con la nuova approssimazione x

        it=it+1                         # Incrementa il numero di iterazioni

    return x,it,er_vet                  # Restituisce la soluzione approssimata, il numero di iterazioni e il vettore degli errori
