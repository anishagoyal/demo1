#!/usr/bin/python

import os
import time 
x=''

print   "press 1 to give a message:  "
print   "press 2 to reboot my machine:  "
print   "press 3 to open web camera:  "
print   "press 4 to take screenshot:  "

print x

ch= raw_input()

if ch=='1':
	print "welcome to python 2.7"
	time.sleep(2)
elif ch=='2':
	print "os is about to reboot"
	os.system('reboot')
elif  ch=='3':
	print "wait for internet"
	os.system('cheese')
elif  ch=='4':
	print "taking screenshot"
	os.system('gnome-screenshot')
else :
	print "wrong value"
	
