import numpy as np

def metodo_bisezione(fname, a, b, tolx,tolf):
     """
     Implementa il metodo di bisezione per il calcolo degli zeri di un'equazione non lineare.
    
     Parametri:
      f: La funzione da cui si vuole calcolare lo zero.
      a: L'estremo sinistro dell'intervallo di ricerca.
      b: L'estremo destro dell'intervallo di ricerca.
      tol: La tolleranza di errore.
    
     Restituisce:
      Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
     """
     fa=fname(a)
     fb=fname(b)
     if np.sign(fa) * np.sign(fb) >= 0: # TODO: Teorema dei segni, in intervallo chiuso può esserci uno zero solo se gli estremi sono di segni diversi
         print("Non è possibile applicare il metodo di bisezione \n")
         return None, None,None
    
     it = 0
     v_xk = []
    
     max_it=int(np.ceil(np.log2((b - a) / tolx)))
     print("Max_It ",max_it)
     while abs(b - a) > tolx and it < max_it: # TODO : 
            xk = a + (b - a) / 2 # TODO: Formula del punto medio 
            v_xk.append(xk)
            it += 1
            fxk=fname(xk)
            if np.abs(fxk)<tolf:
              return xk, it, np.array(v_xk)
        
            if np.sign(fa) * np.sign(fxk) < 0:   # TODO: Teorema dei segni con il punto a sx    #la radice si trova nell'intervallo [a, xk].
              b = xk
              fb = fxk
            elif np.sign(fxk) * np.sign(fb) < 0: # TODO: Teorema dei segni con il punto a dx  #la radice si trova nell'intervallo [xk, b].
              a = xk
              fa = fxk
        
     
     return xk, it, np.array(v_xk)