# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:39:26 2015

@author: amlopez
"""
import multi_dtw as mdtw
import numpy as np

def clasifica_golpes_mdtw(golpes):

    masparecido = {}
    
    for k in np.arange(len(golpes)):
        distancia_minima = float('inf')
        print('K = ', k)
        for r in np.arange(len(golpes)):
            print('    R = ', r)
            if(k!=r):
                distancia, cost, path = mdtw.multi_dtw(golpes[k][2], golpes[r][2], normalize = False)
                if(distancia < distancia_minima):
                    distancia_minima = distancia
                    masparecido[k] = r
    
    return masparecido
        

