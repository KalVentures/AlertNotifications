#!/usr/bin/env python

import ConfigParser
import os

path = os.path.dirname(os.path.abspath(__file__))

Config = ConfigParser.ConfigParser()

cfgfile = open(path+"/config.ini",'w')

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
#Config.set('AlertInformation','App_port',"22")

Config.write(cfgfile)
cfgfile.close()

path = os.path.dirname(os.path.abspath(__file__))

print("Set up crontab with the following path:")
print(path+"/alertNotifications.py\n")

print("Example for 5 interval:")
print("*/5 * * * * python "+path+"/alertNotifications.py\n")
