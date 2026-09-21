import numpy as np

from SolveTriangular import Lsolve

def gauss_seidel_sor(A,b,x0,toll,it_max,omega):  # Definisce la funzione per il metodo di Gauss-Seidel con rilassamento (SOR)

    errore=1+toll                                 # Inizializza l'errore con un valore più grande di toll

    d= np.diag(A) # TODO
    D= np.diag(d) # TODO
    
    E = np.tril(A, -1) # TODO
    F = np.triu(A, 1) # TODO

    Momega = D+omega*E                             # Matrice M modificata per SOR: D + ωE
    Nomega = (1-omega)*D-omega*F                   # Matrice N modificata per SOR

    T=np.dot(np.linalg.inv(Momega),Nomega)       # Matrice di iterazione SOR: T = Mω^{-1} Nω

    autovalori=np.linalg.eigvals(T)              # Calcola gli autovalori della matrice di iterazione
    raggiospettrale= np.max(np.abs(autovalori)) # Calcola il raggio spettrale

    print("raggio spettrale Gauss-Seidel SOR ", raggiospettrale)  # Stampa il raggio spettrale

    M= D + E
    N= -F

    it=0                                         # Contatore iterazioni



    er_vet=[]                                    # Lista per memorizzare gli errori

    while it<=it_max and errore>=toll: #to do          # Ciclo iterativo con criterio di arresto


        xtilde, _ = Lsolve(M, b + N @ x0) #to do

        x = (1 - omega) * x0 + omega * xtilde #to do

        errore= np.linalg.norm(x - x0) / np.linalg.norm(x) #to do   # Errore relativo tra iterazioni successive

        er_vet.append(errore)                    # Salva l'errore

        x0=x.copy()                         # Aggiorna la soluzione per iterazione successiva

        it=it+1                                  # Incrementa il contatore

    return x,it,er_vet                        # Restituisce soluzione, numero iterazioni e vettore errori
