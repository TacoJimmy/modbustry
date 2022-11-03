import sys
import struct  
import modbus_tk 
import modbus_tk.defines as mtk  
import modbus_tk.modbus  
import modbus_tk.modbus_tcp  
import time  
import random  
import string
  
logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")  
  
try:  
    #server = modbus_tk.modbus_tcp.TcpServer()   
    server = modbus_tk.modbus_tcp.TcpServer(port=502, address='0.0.0.0', timeout_in_sec=3)         
    server.start()  
    slave_1 = server.add_slave(1)  
    slave_1.add_block('block1', modbus_tk.defines.HOLDING_REGISTERS, 0, 11) 
    slave_1.add_block('block2', modbus_tk.defines.HOLDING_REGISTERS, 11, 1) 
    #slave_1.set_values('block1', 0, [1,2,3,4,5,6,7,8,9,10])
    slave_1.set_values('block1', 0, 10*[5])
    slave_1.set_values('block1', 10, 255)
    slave_1.set_values('block1', 9, 8)
    valueAll = slave_1.get_values('block1', 0, 11)
    print ('valueAll: ', valueAll)
    valueSet = slave_1.get_values('block1', 0, 1) 
    print ('valueSet:  ', valueSet)
    while True:       
        value1 = slave_1.get_values('block1', 9, 1)
        value2 = slave_1.get_values('block2', 11, 1)  
        print (value1)
        print (value2)
        time.sleep(10)  

    
except:  
    print ('============error===========' ) 
finally:  
    print ('=========stop========')  
    server.stop() 