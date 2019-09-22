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
        try:
            sensoreTemperaturaCamino.letturaSensore()
            print 'Temperatura aria camino: ' 
            print sensoreTemperaturaCamino.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura aria camino'
            sensoreTemperaturaCamino.valore = 9999
            print e
    elif selettore.indice == 2:
        try:
            sensoreTemperaturaCantina.letturaSensore()
            print 'Temperatura cantina: '
            print sensoreTemperaturaCantina.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in cantina'
            sensoreTemperaturaCantina.valore = 9999
            print e
    elif selettore.indice == 3:
        try:
            sensoreTemperaturaEsterna.letturaSensore()
            print 'Temperatura esterna: '
            print sensoreTemperaturaEsterna.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura esterna'
            sensoreTemperaturaEsterna.valore = 9999
            print e
    elif selettore.indice == 4:
        try:
            sensoreTemperaturaVeranda.letturaSensore()
            print 'Temperatura veranda: '
            print sensoreTemperaturaVeranda.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in veranda'
            sensoreTemperaturaVeranda.valore = 9999
            print e
    elif selettore.indice == 15:
        print 'Qui salviamo tutto...'
        data_store.scriviTemperatura(float(sensoreTemperaturaCamino.valore*10),"camino")
        data_store.scriviTemperatura(float(sensoreTemperaturaCantina.valore*10),"cantina")
        data_store.scriviTemperatura(float(sensoreTemperaturaEsterna.valore*10),"esterna")
        data_store.scriviTemperatura(float(sensoreTemperaturaVeranda.valore*10),"veranda")
        data_store.salva_dati()
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
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA ESTERNA'
    sensoreTemperaturaEsterna = sensori_temperatura()
    sensoreTemperaturaEsterna.inizializzazione('28-03089779cf4c')
    sensoreTemperaturaEsterna.letturaSensore()
    print sensoreTemperaturaEsterna.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA ESTERNA'
    print e
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA VERANDA'
    sensoreTemperaturaVeranda = sensori_temperatura()
    sensoreTemperaturaVeranda.inizializzazione('28-03089779b6ce')
    sensoreTemperaturaVeranda.letturaSensore()
    print sensoreTemperaturaVeranda.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA VERANDA'
    print e
time.sleep(0.1)
#############################################
#### INIZIALIZZAZIONE DATABASE DEI TREND ####
#############################################
try:
    print 'INIZIALIZZAZIONE DATABASE DEI TREND'
    #dbTrend = database_engine('/home/pi/db_imp_ele/dbTrend.db')
    #dbTrend.inserisciTrendValue("tCamino",float(sensoreTemperaturaCamino.valore))
    #dbTrend.inserisciTrendValue("tCantina",float(sensoreTemperaturaCantina.valore))
    #dbTrend.salva_dati()
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL DATABASE DEI TREND'
    print e
time.sleep(0.5)
#############################################################
#### INIZIALIZZAZIONE CONNESSIONA AL DATABASE DATA_STORE ####
#############################################################
try:
    print 'INIZIALIZZAZIONE CONNESSIONE AL DATABASE DATA_STORE'
    data_store = database_engine('/home/pi/db_imp_ele/data_store.db')
    data_store.scriviTemperatura(float(sensoreTemperaturaCamino.valore)*10,"camino")
    data_store.scriviTemperatura(float(sensoreTemperaturaCantina.valore)*10,"cantina")
    data_store.scriviTemperatura(float(sensoreTemperaturaEsterna.valore*10),"esterna")
    data_store.scriviTemperatura(float(sensoreTemperaturaVeranda.valore*10),"veranda")
    data_store.salva_dati()
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