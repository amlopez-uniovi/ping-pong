# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.signal as sgn

def segment_signal_va(S, ordenfiltro = 1, vecindad = 1, useacceleration = True, fcorte = 0.5):
    """
    Segmentación sobre un grupo de señales pasadas en una lista
    """
        
    tam = S[0].size
    
    h = np.zeros(tam)    
    b,a = sgn.butter(5, fcorte, 'lowpass', output = 'ba')
   
    
    for senhal in S:
        
        filtrada = sgn.filtfilt(b, a, senhal)
     
        diff1 = np.append(0, np.diff(filtrada))
         
        
        h = h +diff1**2
        if useacceleration:
           diff2 = np.append(0, np.diff(diff1))
           h = h + diff2**2    
        
    locmin = sgn.argrelextrema(h, np.less, order = vecindad)
    
    return (locmin[0], h)
    

def segment_signal_fpb(senhal, ordenfiltro = 1, vecindad = 1, fcorte = 0.5):
    """
    Segmentación sobre una señal previamente suavizada con un filtro paso bajo
    """
        
    b,a = sgn.butter(5, fcorte, 'lowpass', output = 'ba')
   
    filtrada = sgn.filtfilt(b, a, senhal)
    
    locmin = sgn.argrelextrema(filtrada, np.less, order = vecindad)
    
    return (locmin[0], filtrada)

    
def filtra_eventos1(eventos, derivada, derivada_menor_que = 1, salto_en_derivada_mayor_que = 10):
    
    eventos2 = np.array([t for t in eventos if derivada[t] < derivada_menor_que])

    eventos3 = np.array([eventos2[t] for t in range(eventos2.size-1) if np.amax(derivada[eventos2[t]:eventos2[t+1]])>salto_en_derivada_mayor_que])
    
    return eventos3
    

def divide_golpes(eventos, sens):
    
    glp = {}
    
    #print(sens)
    
    for k in np.arange(eventos.size-1):
        glp.update({k:(eventos[k], eventos[k+1], sens[:, eventos[k]:eventos[k+1]])})
        
    return glp
    

