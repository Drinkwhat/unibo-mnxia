import numpy as np

def newton_raphson_sham(initial_guess,F_numerical, J_numerical, tolX, tolF, update, max_iterations):
    
    # Converte il vettore iniziale in un array NumPy di float
    X = np.array(initial_guess, dtype=float)

    # Contatore delle iterazioni
    it = 0

    # Inizializzazione degli errori con valori maggiori delle tolleranze,
    # in modo da entrare sicuramente nel ciclo while
    erroreF = 1 + tolF
    erroreX = 1 + tolX

    # Lista per memorizzare l'errore relativo sugli iterati
    errore = []

    # 
    while it < max_iterations and erroreF > tolF and erroreX > tolX: #to do
        
        if it % update == 0:
            jx = np.array(J_numerical(X[0], X[1]), dtype=float) # TODO: Jacobiana

            # Controlla che la Jacobiana sia invertibile
            if np.linalg.matrix_rank(jx) < jx.shape[0]: #to do 
                print("La matrice Jacobiana calcolata non è a rango massimo")
                return None, None, None

        # Calcola il valore della funzione F nel punto corrente
        fx = np.array(F_numerical(X[0], X[1]), dtype=float).squeeze() #to do 

        s = np.linalg.solve(jx, -fx) #to do 

        # Aggiorna l'iterato
        Xnew = X + s #to do 

        # Calcola l'errore relativo tra iterati successivi usando la norma 1
        normaXnew = np.linalg.norm(Xnew, 1)
        if normaXnew != 0:
            erroreX = np.linalg.norm(s, 1) / normaXnew #to do 
        else:
            erroreX = np.linalg.norm(s, 1) #to do 

        # Salva l'errore relativo nella lista
        errore.append(erroreX)

        # Calcola il residuo nel nuovo punto
        fxnew = np.array(F_numerical(Xnew[0], Xnew[1]), dtype=float).squeeze() #to do 
        erroreF = np.linalg.norm(fxnew, 1)

        # Aggiorna l'iterato corrente e il contatore
        X = Xnew
        it = it + 1

    # Restituisce:
    # - l'approssimazione della soluzione
    # - il numero di iterazioni eseguite
    # - la lista degli errori relativi
    return X, it, errore