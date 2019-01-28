# Raspberry-Balao

Parte do projeto da Sonda de Exploração Científica voltada a captura e registro de temperatura

Material utilizado:
	- Raspberry Pi Zero W;
	- Sensor de temperatura DS18B20;
	- Resistor 4,7 KΩ;

Utilizamos na Raspberry o sistema operacional Raspbian Lite (uma versão do Raspbian sem interface gráfica), pois a ideia é que o minicomputador rode o mais leve possível.

O software é composto por dois arquivos. Um é o temp.py, que utiliza das portas GPIO da Raspberry para fazer a leitura da temperatura atravez do sensor DS18B20 e registra essa leitura em um banco de dados sqlite3. O outro arquivo é o db_temp.db, o banco onde ficarão registradas as temperaturas lidas.

O banco de dados é bastante simples, possuindo até o momento apenas uma entidade com dois atributos:
temperaturas( Id INTEGER PRIMARI KEY AUTOINCREMENT, Temperatura TEXT NOT NULL).
A escolha por registrar a temperatura em forma de texto é devido ao sensor disponibilizar a leitura inicial em forma de string.



Fontes:

o Montagem do circuito : http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
o Gerencia Sqlite3 através do Python: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
o Datasheet DS18B20: http://www.circuitbasics.com/wp-content/uploads/2016/03/DS18B20-Datasheet.pdf
o Esquema GPIO da Raspberry: https://shahbaz.co/img/pi-zero-GPIO.png