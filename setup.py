#!/usr/bin/env python

import ConfigParser
import os

Config = ConfigParser.ConfigParser()

cfgfile = open("config.ini",'w')
serverName = raw_input(    'Enter server name      : ')
serverEmail = raw_input(   'Server Email           : ')
serverPassword = raw_input('Server Email Password  : ')
alertEmail = raw_input(    'Email to send Alerts to: ')

Config.add_section('ServerEmail')
Config.add_section('AlertEmail')
Config.add_section('AlertInformation')

Config.set('ServerEmail','email',serverEmail)
Config.set('ServerEmail','password',serverPassword)
Config.set('ServerEmail','name',serverName)
Config.set('AlertEmail','email',alertEmail)

Config.set('AlertInformation','ip',"0.0.0.0")
Config.set('AlertInformation','lastReboot', "")

#add any information you want sent along with IP:
#Config.set('AlertInformation','ServerTemp',"32")
#Config.set('AlertInformation','App_port',"22")

Config.write(cfgfile)
cfgfile.close()

path = os.path.dirname(os.path.abspath(__file__))

print(path+"/alertNotifications.py")


#crontab -l > my-crontab
#crontab my-crontab
#rm my-crontab
