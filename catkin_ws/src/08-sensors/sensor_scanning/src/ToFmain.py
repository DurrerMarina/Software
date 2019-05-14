import smbus
import time
import sys
import os
import sys
from ToF import ToF
from AvgOverLastNValues import AvgOverLastNValues

while 1:
	try:
		fp1 = smbus.SMBus(1)
		fp1.write_byte(0x70, 0x01)	
		time.sleep(0.001) 
		sensor1 = ToF()
		if sensor1.begin()==True:
			try:
				ToFDistance1 = sensor1.takeMeasurement()[0]
				print 'sensor 1 distance:',ToFDistance1 
			except:
				print 'Could not take Measueement 1 ____________'	
		else:
			break
		time.sleep(0.1)
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
	
	try:
		fp2 = smbus.SMBus(1)
		fp2.write_byte(0x70, 0x02)	
		time.sleep(0.001)
		sensor2 = ToF()
		if sensor2.begin()==True:
			try:
				ToFDistance2 = sensor2.takeMeasurement()[0]
				print 'sensor 2 distance:',ToFDistance2 
			except:
				print 'Could not take Measueement 2 ____________'
		else:
			break
		time.sleep(0.1)
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
	
	try:
		fp3 = smbus.SMBus(1)
		fp3.write_byte(0x70, 0x04)	
		time.sleep(0.001)			
		sensor3 = ToF()
		if sensor3.begin()==True:
			try:
				ToFDistance3 = sensor3.takeMeasurement()[0]
				print 'sensor 3 distance:',ToFDistance3 
			except:
				print 'Could not take Measueement 3 ____________'
		else:
			break
		time.sleep(0.1)
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
