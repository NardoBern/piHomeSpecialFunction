import os
import glob
import time
class sensori_temperatura:
    
    def inizializzazione(self,address):
        #INIZIALIZZAZIONE DEL PERCORSO DI LOCALIZZAZIONE DEI SENSORI NEL SISTEMA
        self.base_dir = '/sys/bus/w1/devices/'
        self.indirizzo = address
        self.valore = 999
        self.databaseUpdateRequired = False
 
    #FUNZIONE CHE SI VA A LEGGERE IL CONTENUTO DEL SENSORE
    def read_temp_raw(self):     
        #print 'FUNZIONE READ TEMP RAW'
        #global device_file
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        #print lines
        return lines 

    #FUNZIONE CHE CONTROLLA SE LA CONNESSIONE E OK E ESTRAPOLA LA TEMPERATURA
    def read_temp(self): 
        #print 'FUNZIONE READ TEMP'
        global read_temp_raw
        lines = self.read_temp_raw()
        #print lines
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        #print equals_pos
        if equals_pos !=-1:
            temp_string = lines[1][equals_pos+2:]
            #print temp_string
            temp_c = float(temp_string)/1000.0
            temp_f = temp_c * 9.0/5.0 + 32.0
            #print temp_c
            return temp_c
            

    #FUNZIONE DI LETTURA DI TUTTI I SENSORI PRESENTI IN RETE
    def leggi_tutti_sensori(self):
        global lista_sensori,base_dir,device_dir,device_file,read_temp,tempin 
        tempin = []
        print('LETTURA DI TUTTI I SENSORI PRESENTI IN RETE')
        for item in lista_sensori:
            #print 'ENTRO NEL CICLO FOR'
            temp_nome = item[0:2]
            if temp_nome == '28':
                #print 'ENTRO NELLA IF'
                device_dir = item
                device_folder = glob.glob(base_dir + device_dir)[0]
                device_file = device_folder + '/w1_slave'
                #print 'CHIAMO READ TEMP'
                tempin.append(self.read_temp()) #get the temp
                #print tempin
        return tempin
                
    def letturaSensore(self):
        self.device_dir = self.indirizzo
        self.device_folder = self.base_dir + self.device_dir
        self.device_file = self.device_folder + '/w1_slave'
        #print 'CHIAMO READ TEMP'
        self.valore = round(self.read_temp(),1) #get the temp
        self.databaseUpdateRequired = True
        #self.valore = tempin