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
    elif selettore.indice == 5:
        try:
            sensoreTemperaturaCucina.letturaSensore()
            print 'Temperatura cucina: '
            print sensoreTemperaturaCucina.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in cucina'
            sensoreTemperaturaCucina.valore = 9999
            print e
    elif selettore.indice == 6:
        try:
            sensoreTemperaturaCorridoio.letturaSensore()
            print 'Temperatura corridoio: '
            print sensoreTemperaturaCorridoio.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in corridoio'
            sensoreTemperaturaCorridoio.valore = 9999
            print e
    elif selettore.indice == 7:
        try:
            sensoreTemperaturaBagno.letturaSensore()
            print 'Temperatura bagno: '
            print sensoreTemperaturaBagno.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in bagno'
            sensoreTemperaturaBagno.valore = 9999
            print e
    elif selettore.indice == 8:
        try:
            sensoreTemperaturaAntiBagno.letturaSensore()
            print 'Temperatura Antibagno: '
            print sensoreTemperaturaAntiBagno.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in antibagno'
            sensoreTemperaturaAntiBagno.valore = 9999
            print e
    elif selettore.indice == 9:
        try:
            sensoreTemperaturaSala.letturaSensore()
            print 'Temperatura Sala: '
            print sensoreTemperaturaSala.valore
        except Exception,e:
            print 'Errore nella lettura della temperatura in sala'
            sensoreTemperaturaSala.valore = 9999
            print e
    elif selettore.indice == 15:
        print 'Qui salviamo tutto...'
        data_store.scriviTemperatura(float(sensoreTemperaturaCamino.valore*10),"camino")
        data_store.scriviTemperatura(float(sensoreTemperaturaCantina.valore*10),"cantina")
        data_store.scriviTemperatura(float(sensoreTemperaturaEsterna.valore*10),"esterna")
        data_store.scriviTemperatura(float(sensoreTemperaturaVeranda.valore*10),"veranda")
        data_store.scriviTemperatura(float(sensoreTemperaturaCucina.valore*10),"cucina")
        data_store.scriviTemperatura(float(sensoreTemperaturaCorridoio.valore*10),"corridoio")
        data_store.scriviTemperatura(float(sensoreTemperaturaBagno.valore*10),"bagno")
        data_store.scriviTemperatura(float(sensoreTemperaturaAntiBagno.valore*10),"antibagno")
        data_store.scriviTemperatura(float(sensoreTemperaturaSala.valore*10),"sala")
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
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA CUCINA'
    sensoreTemperaturaCucina = sensori_temperatura()
    sensoreTemperaturaCucina.inizializzazione('28-030897790d0d')
    sensoreTemperaturaCucina.letturaSensore()
    print sensoreTemperaturaCucina.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA CUCINA'
    print e
time.sleep(0.1)
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA CORRIDOIO'
    sensoreTemperaturaCorridoio = sensori_temperatura()
    sensoreTemperaturaCorridoio.inizializzazione('28-001c0f000019')
    sensoreTemperaturaCorridoio.letturaSensore()
    print sensoreTemperaturaCorridoio.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA CORRIDOIO'
    print e
time.sleep(0.1)
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA BAGNO'
    sensoreTemperaturaBagno = sensori_temperatura()
    sensoreTemperaturaBagno.inizializzazione('28-00000b53574d')
    sensoreTemperaturaBagno.letturaSensore()
    print sensoreTemperaturaBagno.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA BAGNO'
    print e
time.sleep(0.1)
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA ANTIBAGNO'
    sensoreTemperaturaAntiBagno = sensori_temperatura()
    sensoreTemperaturaAntiBagno.inizializzazione('28-00000b5347c5')
    sensoreTemperaturaAntiBagno.letturaSensore()
    print sensoreTemperaturaAntiBagno.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA ANTIBAGNO'
    print e
time.sleep(0.1)
try:
    print 'INIZIALIZZAZIONE SENSORE TEMPERATURA SALA'
    sensoreTemperaturaSala = sensori_temperatura()
    sensoreTemperaturaSala.inizializzazione('28-019aa6070002')
    sensoreTemperaturaSala.letturaSensore()
    print sensoreTemperaturaSala.valore
except Exception,e:
    print 'ERRORE NELLA INIZIALIZZAZIONE DEL SENSORE TEMPERATURA SALA'
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
    data_store.scriviTemperatura(float(sensoreTemperaturaCucina.valore*10),"cucina")
    data_store.scriviTemperatura(float(sensoreTemperaturaCorridoio.valore*10),"corridoio")
    data_store.scriviTemperatura(float(sensoreTemperaturaBagno.valore*10),"bagno")
    data_store.scriviTemperatura(float(sensoreTemperaturaAntiBagno.valore*10),"antibagno")
    data_store.scriviTemperatura(float(sensoreTemperaturaSala.valore*10),"sala")
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