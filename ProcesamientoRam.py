# ProcesamientoRam.py
# Cristopher Recinos 16005
# Cristian Perez 16011

import simpy
import random

def operacion(nombre,env,memoria):
    global tiempoMemoria
    while True:
        new_duration = random.randint(1,10)
        print(nombre, 'pidio', new_duration, 'de memoria en el tiempo:',env.now)
        tiempoPedir = env.now
        
        with memoria.request() as turno:
            yield turno
            yield env.timeout(new_duration)
            print(nombre,'libero memoria a las',env.now)
            tiempoTotal = env.now - tiempoPedir
            print('%s se tardo %d' % (nombre,tiempoTotal ))
            tiempoMemoria = tiempoMemoria+tiempoTotal

        ready_duration = random.randint(1,10)
        print(nombre,'va a realizar',ready_duration,'operaciones')

        with operaciones.request() as turno:
            yield turno
            yield env.timeout(ready_duration)
            print (nombre,'termino a las',env.now)
            if ready_duration-3 !=0:
                a = random.randint(1,2)
                if a ==1:
                    Iduration = random.randint(1,3)
                    print(nombre,'realizo', Iduration, 'operaciones adicionales')

                if a ==2:
                    with operaciones.request() as turno:
                        yield turno
                        yield env.timeout(ready_duration)
                        print (nombre,'termino a las',env.now)
                
                    
           
            
env = simpy.Environment()
memoria = simpy.Resource(env,capacity=10)
operaciones = simpy.Resource(env,capacity=3)
tiempoMemoria = 0
cantidad = 3
cantidadfloat = cantidad + 0.0
for i in range(cantidad):
    env.process(operacion('operacion %d' %i,env,memoria))
env.run(until=30)                
print('el tiempo promedio es',tiempoMemoria/cantidadfloat)

