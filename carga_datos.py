# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:16:26 2015

@author: amlopez
"""

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt


def carga_datos(fichero):

    config_mat = sio.loadmat(fichero, struct_as_record=False, squeeze_me=True)
    
    silop_config_struct = config_mat['SILOP_CONFIG']
    
    datos = np.loadtxt('./prueba_inicial/datos/datos.log')
    datos_alg = np.loadtxt('./prueba_inicial/datos/datos_alg.log')
    datos = np.concatenate((datos, datos_alg), axis = 1)
    
    flex_munheca = datos[:, silop_config_struct.SENHALES.m.flex-1]
    abd_munheca = datos[:, silop_config_struct.SENHALES.m.abd-1]
    
    flex_codo = datos[:, silop_config_struct.SENHALES.c.flex-1]
    pron_codo = datos[:, silop_config_struct.SENHALES.c.pron-1]
    
    flex_hombro = datos[:, silop_config_struct.SENHALES.h.flex-1]
    rot_hombro = datos[:, silop_config_struct.SENHALES.h.rot-1]
    abd_hombro = datos[:, silop_config_struct.SENHALES.h.abd-1]
       
    return {'flex_munheca':flex_munheca, 'abd_munheca':abd_munheca,
            'flex_codo':flex_codo, 'pron_codo':pron_codo,
            'flex_hombro':flex_hombro, 'rot_hombro':rot_hombro, 'abd_hombro':abd_hombro}
