# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:39:26 2015

@author: amlopez
"""
import multi_dtw as mdtw
import numpy as np

def clasifica_golpes_mdtw(golpes, patrones = {}):

    masparecido = {}
        
    if(len(patrones)==0):
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
        
    else:
        for k in np.arange(len(golpes)):
            distancia_minima = float('inf')
            print('K = ', k)
            for r in patrones.keys():
                print('    R = ', r)
                for patron in patrones[r]:
                    print('        patron: ', patron[0], patron[1])
                    distancia, cost, path = mdtw.multi_dtw(golpes[k][2], patron[2], normalize = False)
                    if(distancia < distancia_minima):
                        distancia_minima = distancia
                        masparecido[k] = (r, patron)
       
        
    return masparecido