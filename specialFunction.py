#!/usr/bin/python3
#!/usr/bin/env python

########################################
#### IMPORTAZIONE LIBRERIE / CLASSI ####
########################################
import time
import sys
import os
import datetime
import site
site.addsitedir(sys.path[0]+'/lib')
from db_manager import database_engine
from temp_sens_manager import sensori_temperatura
from oneWireBusDriver import oneWireBus
from threading import Timer
from cadenziatore import cadenziatore


def oneMinFunction():
    selettore.indice = selettore.indice + 1
    print 'Il valore del indice:'
    print selettore.indice
    if selettore.indice == 1:
        sensoreTemperaturaCamino.letturaSensore()
        print 'Temperatura aria camino: ' 
        print sensoreTemperaturaCamino.valore
    elif selettore.indice == 2:
        sensoreTemperaturaCantina.letturaSensore()
        print 'Temperatura cantina: '
        print sensoreTemperaturaCantina.valore
    elif selettore.indice == 15:
        print 'Qui salveremo tutto...'
        print 'Resetto il indice'
        selettore.indice = 0
    print 'INTERRUPT ad 1 Min.'
    t = Timer(60.0,oneMinFunction)
    t.start()



######################################
#### INIZIALIZZAZIONE BUS ONEWIRE ####
######################################
try:
    print 'INIZIALIZZAZIONE BUS ONEWIRE'
    busone = oneWireBus()
    busone.inizializzazione()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL BUS ONEWIRE'
time.sleep(0.5)
#################################################
#### INIZIALIZZAZIONE SENSORI DI TEMPERATURA ####
#################################################
print 'INIZIALIZZAZIONE SENSORI DI TEMPERATURA'
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA CANTINA'
    sensoreTemperaturaCantina = sensori_temperatura()
    sensoreTemperaturaCantina.inizializzazione('28-00044c9e3aff')
    sensoreTemperaturaCantina.letturaSensore()
    print sensoreTemperaturaCantina.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA CANTINA'
    print e
time.sleep(0.1)
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA CAMINO'
    sensoreTemperaturaCamino = sensori_temperatura()
    sensoreTemperaturaCamino.inizializzazione('28-00044ea1a3ff')
    sensoreTemperaturaCamino.letturaSensore()
    print sensoreTemperaturaCamino.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA CAMINO'
    print e
time.sleep(0.1)
#############################################
#### INIZIALIZZAZIONE DATABASE DEI TREND ####
#############################################
try:
    print 'INIZIALIZZAZIONE DATABASE DEI TREND'
    dbTrend = database_engine('/home/pi/db_imp_ele/dbTrend.db')
    dbTrend.inserisciTrendValue("tCamino",float(sensoreTemperaturaCamino.valore))
    dbTrend.inserisciTrendValue("tCantina",float(sensoreTemperaturaCantina.valore))
    dbTrend.salva_dati()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL DATABASE DEI TREND'
    print e
time.sleep(0.5)
#######################################
#### INIZIALIZZAZIONE CADENZIATORE ####
#######################################
try:
    print 'INIZIALIZZAZIONE CADENZIATORE'
    selettore = cadenziatore()
    selettore.inizializzazione()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL CADENZIATORE'
    print e
####################################################
#### INIZIALIZZAZIONE TIMER INTERRUPT AD 1 MIN. ####
####################################################
try:
    print 'INIZIALIZZAZIONE ONE MINUTE INTERRUPT'
    t = Timer(60.0,oneMinFunction)
    t.start()
except:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL TIMER DI INTERRUPT'
    t.cancel()
print 'FINE CICLO DI INIZIALIZZAZIONE'