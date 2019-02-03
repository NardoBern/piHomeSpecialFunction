import os


class oneWireBus:
    def inizializzazione(self):
        print 'INIZIALIZZAZIONE IN CORSO'
        #INIZIALIZZAZIONE DEI SENSORI DI TEMPERATURA
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')