#!/usr/bin/env python
#clearConsoleWidget.py
#written by Kevin Ersoy in Python 3
import os
import sys
#sys.path.append("C:\python") #add path to kevdriver to sys.path
#import kevdriver
import socket
import time
from Tkinter import *

filename = 'favicon2.ico'
if hasattr(sys, '_MEIPASS'):
    # PyInstaller >= 1.6
    os.chdir(sys._MEIPASS)
    filename = os.path.join(sys._MEIPASS, filename)
#else:
#	chdir(dirname(sys.argv[0]))
#	filename = os.path.join(dirname(sys.argv[0]), filename)

def setBaud(IP, port, baud):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, 23))
	s.recv(2048)
	data=Entry3.get() + "\n"
	s.send(data.encode())
	s.send(b'enable\n')
	data=Entry4.get() + "\n"
	s.send(data.encode())
	time.sleep(0.3)
	data = ("conf t")
	s.send(data.encode())
	s.send(b'\n\n')
	data = ("line " + port)
	s.send(data.encode())
	s.send(b'\n\n')
	data = ("speed " + baud)
	s.send(data.encode())
	s.send(b'\n\n')
	print (s.recv(2048).decode('ascii'))
	print (s.recv(2048).decode('ascii'))
	time.sleep(0.3)
	rateData = (s.recv(2048).decode('ascii'))
	time.sleep(0.25)
	print rateData
	s.close()

def getBaud(IP, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, 23))
	s.recv(2048)
	data=Entry3.get() + "\n"
	s.send(data.encode())
	s.send(b'enable\n')
	data=Entry4.get() + "\n"
	s.send(data.encode())
	time.sleep(0.3)
	data = ("show line " + port)
	s.send(data.encode())
	s.send(b'\n\n')
	print (s.recv(2048).decode('ascii'))
	print (s.recv(2048).decode('ascii'))
	time.sleep(0.3)
	rateData = (s.recv(2048).decode('ascii'))
	time.sleep(0.25)
	location = rateData.find("Baud rate (TX/RX) is ")
	sub = rateData[location + 21:]
	slash = sub.find("/")
	print (sub[0:slash])
	Entry5.set(sub[0:slash])
	s.close()

def clearLine(IP, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, 23))
	s.recv(2048)
	data=Entry3.get() + "\n"
	s.send(data.encode())
	s.send(b'enable\n')
	data=Entry4.get() + "\n"
	s.send(data.encode())
	time.sleep(0.3)
	data = ("clear line " + port)
	s.send(data.encode())
	s.send(b'\n\n')
	print (s.recv(2048).decode('ascii'))
	print (s.recv(2048).decode('ascii'))
	time.sleep(0.3)
	print (s.recv(2048).decode('ascii'))
	time.sleep(0.25)
	s.close()
	
def quitMe():
	sys.exit()
	
def setPasswords():
	top2.deiconify()
	top2.title("Set Passwords")
	top2.protocol("WM_DELETE_WINDOW", handlerPass)
	L3 = Label(top2, text="Password").grid(row=0,column=0, sticky=E)
	L4 = Label(top2, text="Enable Password").grid(row=1,column=0, sticky=E)
	E3 = Entry(top2, width=15, bd=4, textvariable=Entry3, justify=LEFT)
	E3.grid(row=0, column=1)
	E4 = Entry(top2, width=15, bd=4, textvariable=Entry4, justify=LEFT)
	E4.grid(row=1, column=1)
	B2 = Button(top2, text="Save", command=handlerPass, height=3).grid(row=0, column=2, rowspan=2)

def handlerPass():
	writeConfig()
	top2.withdraw()
	
def handlerAbout():
	top3.withdraw()	
	
def showAbout():
	top3.deiconify()
	top3.title("About")
	top3.protocol("WM_DELETE_WINDOW", handlerAbout)
	L9 = Label(top3, width=20, height=1, text="").grid(row=0,column=0)
	L6 = Label(top3, text = "Console Buddy", justify=LEFT).grid(row=1, column=0, sticky=W)
	L7 = Label(top3, text = "Created  in 2015", justify=LEFT).grid(row=2, column=0, sticky=W)
	L8 = Label(top3, text = "by Kevin Ersoy", justify=LEFT).grid(row=3, column=0, sticky=W)
	
top = Tk()
top2 = Toplevel(top)
top2.iconbitmap(filename)
top2.withdraw()
top3 = Toplevel(top)
top3.iconbitmap(filename)
top3.withdraw()
top.title('Console Buddy')
Entry1 = StringVar()
Entry2 = StringVar()
Entry3 = StringVar()
Entry4 = StringVar()
Entry5 = StringVar()

L1 = Label(top, text="IP/Hostname").grid(row=1,column=0, sticky=E)
L2 = Label(top, text="Port").grid(row=2,column=0, sticky=E)
E1 = Entry(top, width=15, bd=4, textvariable=Entry1, justify=LEFT).grid(row=1, column=1, columnspan=2)
E2 = Entry(top, width=6, bd=4, textvariable=Entry2, justify=LEFT).grid(row=2, column=1, sticky=W)
B1 = Button(top, width=8, text="Clear Line", command=lambda:clearLine(Entry1.get(),Entry2.get()), height=3).grid(row=1, column=3, rowspan=2)
L5 = Label(top, text="Baud Rate").grid(row=3, column=0, sticky=E)
E5 = Entry(top, width=6, bd=4, textvariable=Entry5, justify=LEFT).grid(row=3,column=1, sticky=W)
B3 = Button(top, width=8, text="Get", command=lambda:getBaud(Entry1.get(),Entry2.get()), height=1).grid(row=3,column=2,rowspan=1)
B3 = Button(top, width=8, text="Set", command=lambda:setBaud(Entry1.get(),Entry2.get(),Entry5.get()), height=1).grid(row=3,column=3,rowspan=1)

Entry1.set('termserv-ip')
Entry2.set('3')
Entry3.set('')
Entry4.set('')
Entry5.set('9600')

menubar = Menu(top)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=quitMe)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="set passwords", command=setPasswords)
menubar.add_cascade(label="Edit", menu=editmenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=showAbout)
menubar.add_cascade(label="Help", menu=aboutmenu)

top.config(menu=menubar)
top.iconbitmap(filename)

configFile = 'config.txt'
configPath = os.getenv('APPDATA') + "\\ConsoleBuddy\\"
configFile = configPath + configFile

#open config
try:
	os.makedirs(configPath)
except:
	print configFile

myConfig = ""
try:
	with open (configFile, "r") as myfile:
		myConfig=myfile.read()
except:
	print configFile
	
if len(myConfig) > 0:
	colon=myConfig.find(":")
	Entry3.set(myConfig[:colon])
	Entry4.set(myConfig[colon + 1 :])	

#write config
def writeConfig():
	text_file = open(configFile, "w")
	text_file.write("%s:%s" % (Entry3.get(), Entry4.get()))
	text_file.close()	
	
top.mainloop()