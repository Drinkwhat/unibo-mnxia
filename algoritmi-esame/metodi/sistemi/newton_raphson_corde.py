import numpy as np

def newton_raphson_corde(initial_guess, F_numerical, J_numerical, tolX, tolF, max_iterations):
    
    # Converte il punto iniziale in array NumPy
    X = np.array(initial_guess, dtype=float)

    # Contatore iterazioni
    it = 0

    # Inizializzazione errori (devono essere > tolleranze per entrare nel ciclo)
    erroreF = 1 + tolF
    erroreX = 1 + tolX

    # Lista per salvare errore relativo sugli iterati
    errore = []

    # La Jacobiana viene calcolata SOLO alla prima iterazione
    # e poi riutilizzata sempre (metodo delle corde)
    
    jx = np.array(J_numerical(X[0], X[1]), dtype=float) # TODO: Jacobiana
    # Controllo che la Jacobiana sia invertibile
    if np.linalg.matrix_rank(jx) < jx.shape[0]: # TODO: massimo rango
        print("La matrice Jacobiana non è a rango massimo")
        return None, None, None
            
    # Ciclo iterativo
    while it < max_iterations and erroreF > tolF and erroreX > tolX: # TODO

        # Valutazione della funzione nel punto corrente
        fx = np.array(F_numerical(X[0], X[1]), dtype=float).squeeze()

        
        s = np.linalg.solve(jx, -fx) # TODO

        # Aggiornamento dell'iterato
        Xnew = X + s # TODO

        # Calcolo errore relativo tra iterati successivi (norma 1)
        normaXnew = np.linalg.norm(Xnew, 1)
        if normaXnew != 0:
            erroreX = np.linalg.norm(s, 1) / normaXnew # TODO
        else:
            erroreX = np.linalg.norm(s, 1) # TODO

        # Salvataggio errore
        errore.append(erroreX)

        # Calcolo del residuo nel nuovo punto
        fxnew = np.array(F_numerical(Xnew[0], Xnew[1]), dtype=float).squeeze() # TODO 
        erroreF = np.linalg.norm(fxnew, 1)

        # Aggiornamento iterato
        X = Xnew
        it = it + 1

    # Output finale
    return X, it, errore