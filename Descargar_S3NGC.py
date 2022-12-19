#Created on Fri Nov 12 09:30:53 2021

#@author: Gabriela Resendiz Colorado 
#Posgrado en Ecologia Marina

import os
import eumdac
import datetime
from datetime import date, timedelta
import subprocess
import shutil 


day1=date.today()
day2=day1+timedelta(days=1)


consumer_key='hCOdrJF2oo469sh7Y0U5nvwb2Xca'
consumer_secret='eT20D2lCFc3e98xi2RQYtfUdbm8a'

credentials = (consumer_key, consumer_secret)
token = eumdac.AccessToken(credentials)

#Collection S3 L2 Reduced Resolution EO:EUM:DAT:0408
#Collection S3 L2 Full Resolution EO:EUM:DAT:0407
 # Retrieve all collection objects from DataStore
 
datastore = eumdac.DataStore(token)
datastore.collections;
selected_collection = datastore.get_collection('EO:EUM:DAT:0407')


# Set bounding-box coordinates
bbox = '-115,29,-112,32'

# Retrieve datasets that match our filter
products = selected_collection.search(bbox=bbox, dtstart=day1, 
                                      dtend=day2)
os.chdir(r'I:\Monitoreo_TR2020\Descargas')

print(f'Found Datasets: {len(products)} datasets for the given time range') 

for product in products:
    with product.open() as fsrc,open(os.path.join(r'I:\Monitoreo_TR2020\Descargas',fsrc.name), mode='wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)
        print(f'Download of product {product} finished.')


print('All downloads are finished.')



# importing required modules

from zipfile import ZipFile
  
# specifying the zip file name

file_name=os.listdir(r'I:\Monitoreo_TR2020\Descargas')

# opening the zip file in READ mode

for i in file_name:
    myZip=ZipFile(os.path.abspath(i))
    myZip.extractall(r'I:\Monitoreo_TR2020\Unzip')
    
    #with ZipFile(f,'r') as zip:
    #zip.extractall(r'I:\Monitoreo_TR2020\Unzip')
        
        
#import subprocess

#subprocess.call('/mnt/i/Monitoreo_TR2020/Subsetymosaico.bash')


#os.system('I:\Monitoreo_TR2020\Subsetymosaico.bash')



###########CODIGO ANTERIOR AL CAMBIO DE SEPTIEMBRE DE 2022


#today = date.today()
#day1=today.strftime('%Y%m%d')
#day2=today+timedelta(days=1)
#day2=day2.strftime('%Y%m%d')


#'https://coda.eumetsat.int/'

#day1='20170106'
#day2='20170125'

#os.chdir('I:\Monitoreo_TR2020\Descargas')

#api = SentinelAPI('gresendiz', 'palomus2021','https://coda.eumetsat.int/')


#footprint= geojson_to_wkt(read_geojson(r'I:\Monitoreo_TR2020\Mapa_GC.geojson'))


#products = api.query(footprint,date=(day1,day2),producttype= 'OL_2_WFR___')


#for ii in products.keys():
#  api.download(ii, "")

#api.download_all(products)



# importing required modules

#from zipfile import ZipFile
  
# specifying the zip file name

#file_name =os.listdir('I:\Monitoreo_TR2020\Descargas')

  
# opening the zip file in READ mode


#for i in file_name:

 #with ZipFile(i,'r') as zip:
     
 # zip.extractall(r'I:\Monitoreo_TR2020\Unzip')
        
        
# import subprocess

# subprocess.call('/mnt/i/Monitoreo_TR2020/Subsetymosaico.bash')

        
        
        
        
        
        
        
        
