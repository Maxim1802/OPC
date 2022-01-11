URL = "opt.tcp://192.168.9.57:4840"
port = 502

from opcua import Server
from pyModbusTCP.client import ModbusClient
import time

class Items:
    def __init__(self, objName, objNS, objDev, objDevIP, objDevMBAddr):
    	self.objName = objName
    	self.objNS = objNS
    	self.objDev = objDev
    	self.objDevIP = objDevIP
    	self.objDevMBAddr = objDevMBAddr
    	self.TCP = None

    def connectModbusTCP(self):
    	self.TCP = ModbusClient(host=self.objDevIP, 
								port=port, 
								unit_id=self.objDevMBAddr, 
								auto_open=True)
    
    def writeItemModbusTCP(self, itemAddress):
    	self.itemAddress = itemAddress
    	self.TCP.write_single_coil(self.itemAddress,1)
    	time.sleep(1)
    	self.TCP.write_single_coil(self.itemAddress,0)

if __name__ == "__main__":

	server = Server()
	server.set_endpoint(URL)
	Barion = server.get_objects_node()
	ns = server.register_namespace('Переменные')
	Segnetics_1 = Barion.add_object(ns, 'Segnetics_1')  

	item_distant = Segnetics_1.add_variable(ns,'Дист/местн', 0)
	item_distant.set_writable()

	item_time = Segnetics_1.add_variable(ns,'Таймер', 0)
	item_time.set_writable()

	item_start = Segnetics_1.add_variable(ns,'Пуск', 0)
	item_start.set_writable()

	item_stop = Segnetics_1.add_variable(ns,'Стоп', 0)
	item_stop.set_writable()

	item_alarm = Segnetics_1.add_variable(ns,'Сброс аварии', 0)
	item_alarm.set_writable()

	item_block = Segnetics_1.add_variable(ns,'Блокировка', 0)
	item_block.set_writable()
	
	#Создание узла с параметрами
	segnetics_1 = Items(objName = 'Barion',
						objNS = 'ns',
						objDev = 'Segnetics_1',
						objDevIP = '192.168.9.222',
						objDevMBAddr = 1)

	server.start()
	while True:
		if item_distant.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15360) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)
			item_distant.set_value(0)

		elif item_time.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15361) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)
			item_time.set_value(0)

		elif item_start.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15362) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)
			item_start.set_value(0)

		elif item_stop.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15363) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)
			item_stop.set_value(0)

		elif item_alarm.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15364) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)
			item_alarm.set_value(0)

		elif item_block.get_value() == 1:
			segnetics_1.connectModbusTCP()
			segnetics_1.writeItemModbusTCP(15365) #Запись значения в параметр с последующим сбросом
			time.sleep(0.5)	
			item_block.set_value(0)

		time.sleep(1)


