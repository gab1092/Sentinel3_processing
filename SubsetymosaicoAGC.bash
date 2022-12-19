#!/bin/bash

#Este bash es para hacer subset y reproyectar archivos contenidos en una sola carpeta formato de archivos:netcdf 
##Carpeta de los archivos para los mosaicos


fecha=$(date +'%Y%m%d')
cd /mnt/c/'Program Files'/snap/bin

B="/xfdumanifest.xml"
base="I:"
rutarep="I:\Monitoreo_TR2020\Unzip\Subset_reproyectAGC.xml"
rutamosaicos="I:\Monitoreo_TR2020\Repro\MosaicosS3_AGC.xml"
baset="I:\Monitoreo_TR2020\Repro"
baset2="I:\Monitoreo_TR2020\Mosaicos"


   for i in $(find /mnt/i/Monitoreo_TR2020/Unzip -name "*S3A_OL_2_WFR____$fecha*"); do

        i1=`expr substr $i 7 129`
        A=$base$i1$B
        C=$i1;   AA=`expr substr $C 25 64`
                
        sudo /mnt/c/'Program Files'/snap/bin/gpt.exe $rutarep -Ssource=$A -Ptarget=$baset/$AA
       

   done
  
   for ii in $(find /mnt/i/Monitoreo_TR2020/Unzip -name "*S3B_OL_2_WFR____$fecha*"); do

        ii1=`expr substr $ii 7 129`
        Aa=$base$ii1$B
        CC=$ii1;   AA2=`expr substr $CC 25 64`
        #nombre="$fecha"
        #echo $nombre
        sudo /mnt/c/'Program Files'/snap/bin/gpt.exe $rutarep -Ssource=$Aa -Ptarget=$baset/$AA2
    
   done    
        
        
        
   ##Para buscar archivos Sentinel3A
cd /mnt/i/Monitoreo_TR2020/Repro/
  
A1=$(find -name "*S3A_OL_2_WFR____$fecha*")
AA1=$A1 
##Para ordenar y hacer mosaicos por dÃ­a con los archivos de Sentinel3 A y B
cd /mnt/i/Monitoreo_TR2020/Repro/
B1=$(find -name *"*S3B_OL_2_WFR____$fecha*")
BB1=$B1

if [[ -n $AA1 ]]; then  
 
   if [[ -n $BB1 ]]; then  

         nombre="$fecha"
        #echo $nombre
         sudo /mnt/c/'Program Files'/snap/bin/gpt.exe $rutamosaicos $A1 $B1 -Ptarget=$baset2/$nombre
    fi

fi

if [[ -z $BB1 ]]; then  
 
     if [[ -n $AA1 ]]; then  

         nombre="$fecha"
        #echo $nombre
         sudo /mnt/c/'Program Files'/snap/bin/gpt.exe $rutamosaicos $A1 -Ptarget=$baset2/$nombre
     fi

fi

if [[ -z $AA1 ]]; then  
 
     if [[ -n $BB1 ]]; then  

         nombre="$fecha"
        #echo $nombre
         sudo /mnt/c/'Program Files'/snap/bin/gpt.exe $rutamosaicos $B1 -Ptarget=$baset2/$nombre
     fi

fi
