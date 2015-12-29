#!/usr/bin/env python

import smtplib
import ConfigParser
import subprocess
import os

path = path = os.path.dirname(os.path.abspath(__file__))

#CPU temp for Raspberry pi
def getPiCPUtemp():
	temp = os.popen('vcgencmd measure_temp').readline().strip("temp=").strip("'C\n")
	return temp
	
#requires 'dig' installed 
def getIpAddress():
	proc = subprocess.Popen(["dig", "+short", "myip.opendns.com", "resolver1.opendns.com"], stdout=subprocess.PIPE)
	currentIp = proc.communicate()[0].strip('\n')
	return currentIp
	
def getRebootTime():
	proc = subprocess.Popen(["uptime", "-s"], stdout=subprocess.PIPE)
	rebootTime = proc.communicate()[0].strip('\n')
	return rebootTime
	
def sendMail(Config,msg):
	serverEmail = Config.get('ServerEmail','email')
	serverPassword = Config.get('ServerEmail','password')
	alertEmail = Config.get('AlertEmail','email')
	serverName = Config.get('ServerEmail','name')
	
	#If using own SMTP server change the followling line to 'localhost' and port number
	smtpServer = 'smtp.gmail.com'
	smtpPort = 587	
	
	header  = 'From: %s\n' % serverEmail
	header += 'To: %s\n' % alertEmail
	header += 'Subject: %s alerts\n\n' % serverName
	
	msg = header + msg
	
	server = smtplib.SMTP(smtpServer, smtpPort)
	server.starttls()
	server.login(serverEmail, serverPassword)
	server.sendmail(serverEmail, alertEmail, msg)
	server.quit()
	
def ipChangeMessage(new,old):
	if new == old:
		return ""
	else:
		return "New IP: "+new+"\n"
		
def rebootMessage(new,old):
	if new == old:
		return ""
	else:
		return "Server reboot @: "+new+"\n"
	
def main():
	alertMessage = ""
	#Read configureation file
	Config = ConfigParser.ConfigParser()
	Config.read(path+"/config.ini")

	#read in previous values from configuration file
	previousIp = Config.get('AlertInformation','ip')
	lastReboot = Config.get('AlertInformation','lastReboot')
	
	
	#call alert functions
	currentIp = getIpAddress()
	rebootTime = getRebootTime()
	
	#Add custom alerts as followed:
	#code start
	
	#temp = getPiCPUtemp()
	#if temp == "60":
	#	alertMessage += "Server temp critical @"+temp+"\n"
		
	#code ends
	
	#For each alert condition update 'alertMessage', if no changes return
	#empty string. Based on final string length we send the update.
	alertMessage = ipChangeMessage(currentIp, previousIp)
	alertMessage += rebootMessage(rebootTime, lastReboot)
	
	#true if message is empty
	if len(alertMessage) == 0:
		quit()
	else:
		#update the configuration file to new updated data
		Config.set('AlertInformation','ip',currentIp)
		Config.set('AlertInformation','lastReboot',rebootTime)
		with open(path+'/config.ini', 'wb') as configfile:
			Config.write(configfile)
			
		sendMail(Config,alertMessage)

main()