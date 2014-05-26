#!/usr/bin/python
# -*- coding: utf-8 -*- 
import hpilo
import sendsms
import os,time

# ILOGB851486EN
mysrv = hpilo.Ilo('192.168.1.2',login='Administrator',password='PASSWORD',timeout=60,port=443) # авторизуемся на сервере iLo

sendsms.send_sms('+380501234567','Internet store http://tekhnika.ua is down!')                 # Шлем себе СМС
os.system('sudo /usr/bin/monit unmonitor "tekhnika.ua"')                                       # отключаем мониторинг сайта

mysrv.reset_server()                     # Power cycle the server - пытаемся перегрузить сервер

time.sleep(6*60) 				       # выжидаем 6 минут
os.system('sudo /usr/bin/monit monitor "tekhnika.ua"') # возобновляем мониторинг сайта
