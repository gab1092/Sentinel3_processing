#Created on Fri Nov 12 09:30:53 2021

#@author: Gabriela Resendiz Colorado 
#Posgrado en Ecologia Marina
#Este código fue generado para descargar las imágenes diarias disponibles sobre una región definida en bbox,
#fue configurado para correr en una instalación de python en windows, es necesario instalar la librería eumdac y contar con el consumer key y secret.


import os
import eumdac
import datetime
from datetime import date, timedelta
import subprocess
import shutil 


day1=date.today()
day2=day1+timedelta(days=1)


consumer_key='tu consumer key aqui'
consumer_secret='tu consumer secret aqui'

credentials = (consumer_key, consumer_secret)
token = eumdac.AccessToken(credentials)

#Collection S3 L2 Reduced Resolution EO:EUM:DAT:0408
#Collection S3 L2 Full Resolution EO:EUM:DAT:0407
 # Retrieve all collection objects from DataStore
 
datastore = eumdac.DataStore(token)
datastore.collections;
selected_collection = datastore.get_collection('EO:EUM:DAT:0407')


# Set bounding-box coordinates/coordenadas que definen el área para buscar las imágenes
bbox = 'oeste,sur,este,norte' #sustituir por las coordenadas correspondientes

# Retrieve datasets that match our filter
products = selected_collection.search(bbox=bbox, dtstart=day1, 
                                      dtend=day2)
os.chdir(r'I:\Monitoreo_TR2020\Descargas')

print(f'Found Datasets: {len(products)} datasets for the given time range') 

for product in products:
    with product.open() as fsrc,open(os.path.join(r'ruta_donde_seguardan_lasimagenes',fsrc.name), mode='wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)
        print(f'Download of product {product} finished.')


print('All downloads are finished.')


#Esta parte del código descomprimi los archivos zip de las imágenes en otra carpeta, a partir de la que se generarán los mosaicos con el programa SNAP.

# importing required modules

from zipfile import ZipFile
  
# specifying the zip file name

file_name=os.listdir(r'ruta_dondeseguardaron_lasimagenes')

# opening the zip file in READ mode

for i in file_name:
    myZip=ZipFile(os.path.abspath(i))
    myZip.extractall(r'ruta_dondesevan_adescomprimir')

       
        
        
        
        
        
        
        
        
