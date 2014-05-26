#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko
import datetime
import time

LogFil = '/tmp/sendsms.log'


def send_sms(phone,sms,debug=False):
   """ Subprogram for sending sms 
           phone - recipients phone
           sms - SMS message """
   host  = '192.168.1.1'
   user = 'user'
   myKey = '/home/kouts/Texnika/kouts.key'

   with open(LogFil,'a+') as LogFile:
       ssh = paramiko.SSHClient()
       key = paramiko.DSSKey.from_private_key_file(myKey)
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(host,username=user,pkey=key)
       stdin,stdout,stderr = ssh.exec_command("sendsms '%s' '%s'"%(phone,sms))
       result = stdout.read().splitlines()
       if debug:
          print result
       ts = time.time()
       st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       LogFile.write("%s sendsms '%s' '%s' \n"%(st,phone,sms))

if __name__ == '__main__':
   send_sms('+380501234567','Test message',debug=True)

