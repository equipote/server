# -*- coding: utf-8 -*-
#¡/usr/bin/env python

"""
Created on Wed Dec 25 04:00:46 2013
"""
@author: kaotika
"""

#Este script es posible gracias a la siguiente fuente: http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
#Creado por kaotika ada_lovelance@hackingcodeschool.net Visitanos en hackingcodeschool.net

import subprocess



print "Este script configurará Django con Nginx, Gunicorn, virtualenv,\
       supervisor y PostgreSQL, este script requiere permisos de superusuario"
print "Lo primero que se va a ejecutar es aptitude update && upgrade, \
       es recomendable para las instalaciones posteriores"

respUdt = raw_input("Permites actualizar el sistema (s/n)")

if respUdt == "s" :
    subprocess.call(["aptitude","update"])
    subprocess.call(["aptitude","upgrade"])
else:
    print "Tu sistema no se actualizará"
   
dominio = raw_input("Introduce tu dominio ej hackingcodeschool.net : ")

respdb = raw_input("Se recomienda postgres como base de datos, \
                    deseas instalarlo, s/n: ")

if respdb == "s":
    subprocess.call(["aptitude","install","postgresql postgresql-contrib"])
    
    nombredb = raw_input("Introduce un nombre para tu nueva base de datos")
    usuariodb = raw_input("Introduce un usuari@ para tu base de datos: ")
    passdb1 = raw_input("Introduce una contraseña para tu base de datos:")
    passdb2 = raw_input("Repite tu contraseña")
    
    while passdb1 != passdb2:
        print "Las contraseñas introducidas no coinciden"
        passdb1 = raw_input("Introduce una contraseña para tu base de datos:")
        passdb2 = raw_input("Repite tu contraseña")
    else:
        print "La contraseña ha sido almacenada correctamente"
        subprocess.call(["su", "-", "postgres" "|" "createuser CREATE ROLE \
        usuariodb LOGIN ENCRYPTED PASSWORD passdb1"])

