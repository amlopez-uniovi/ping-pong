import matplotlib.pyplot as plt
import numpy as np
import segmentation as sgm
import imp

import carga_datos as c_d

import clasifica as cls

imp.reload(sgm) 
imp.reload(c_d) 
imp.reload(cls)
 
"""
Cargo y represento datos
"""
 
 
senhales = c_d.carga_datos('./prueba_inicial/datos') 

flex_munheca = senhales['flex_munheca']
abd_munheca = senhales['abd_munheca']
flex_codo = senhales['flex_codo']
pron_codo = senhales['pron_codo']
flex_hombro = senhales['flex_hombro']
rot_hombro = senhales['rot_hombro']
abd_hombro = senhales['abd_hombro']
 
plt.figure(1)

sp1 = plt.subplot(311)
plt.title('Muñeca')
plt.plot(flex_munheca, 'r', label = "flex")
plt.plot(abd_munheca,'g', label = "abd")
plt.legend(loc='upper right')
plt.grid()

plt.subplot(312, sharex=sp1)
plt.title("Codo")
plt.plot(flex_codo, 'r', label = "flex")
plt.plot(pron_codo, 'b', label = "pron")
plt.legend(loc='upper right')
plt.grid()

plt.subplot(313, sharex=sp1)
plt.title("Hombro")
plt.plot(flex_hombro, 'r', label = "flex")
plt.plot(rot_hombro, 'm', label = "rot")
plt.plot(abd_hombro, 'g', label = "abd")
plt.legend(loc='upper right')

plt.show()
plt.grid()    


"""
Segmento datos, postproceso y represento segmentación
"""

res = sgm.segment_signal([flex_munheca, abd_munheca, flex_codo, pron_codo, flex_hombro, rot_hombro, abd_hombro], 
                          vecindad = 10, useacceleration = False, ordenfiltro = 20, fcorte = 0.05)
eventos = sgm.filtra_eventos1(eventos = res[0], derivada = res[1], derivada_menor_que = 1, salto_en_derivada_mayor_que = 10)

fig2 = plt.figure(2)

ax1 = fig2.add_subplot(111)
ax1.plot(flex_munheca, 'r', label = "flex_munheca")
ax1.plot(abd_munheca,'g', label = "abd_munheca")
ax1.plot(flex_codo, 'b', label = "flex_codo")
ax1.plot(pron_codo, 'y', label = "pron_codo")
ax1.plot(flex_hombro, 'k', label = "flex_hombro")
ax1.plot(rot_hombro, 'm', label = "rot_hombro")
ax1.plot(abd_hombro, 'c', label = "abd_hombro")
ax1.legend(loc='upper right')
ax1.set_ylabel("Señales")
ax1.grid()


ax2 = fig2.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(res[1])
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_ylabel("veloc-acel ")

ax2.bar(res[0], np.ones(res[0].size)*20)
ax2.bar(eventos, np.ones(eventos.size)*(-20))

ax2.grid()

"""
Clasifico datos
"""

golpes = sgm.divide_golpes(eventos, np.array((flex_munheca, abd_munheca,
                                                 flex_codo, pron_codo,
                                                 flex_hombro, rot_hombro, abd_hombro)))

clasificacion = cls.clasifica_golpes_mdtw(golpes)