import os
import glob
import time
import sqlite3

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

intervalo_temperatura = 5 # Tempo entre leituras de temperatura

base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"

def read_temp_raw():
	f = open(device_file, "r")
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != "YES":
		time.sleep(0.2)
		lines = read_temp_raw()
		print(lines)
	equals_pos = lines[1].find("t=")
	if (equals_pos != -1):
		temp= lines[1][equals_pos+2:]
		return (temp)
while True:
	temp = (read_temp())

	conn = sqlite3.connect('db_temp.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO temperaturas (Temperatura)  VALUES (?)", (temp,))
	conn.commit()
	conn.close()

	time.sleep(intervalo_temperatura)
