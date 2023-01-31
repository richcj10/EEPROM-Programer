
from pyftdi import FtdiLogger
from pyftdi.i2c import I2cController, I2cIOError
from time import sleep
from array import array as Array
from binascii import hexlify
import time

DeviceAddress = 0x50

class EEPROM():

    def __init__(self):
        self._i2c = I2cController()
        self._i2c.configure('ftdi://ftdi:232h/1')
        self.DA = DeviceAddress
        self.port = self._i2c.get_port(self.DA)

    def ReadName(self,Pos,Lenth):
        try:
            device_id = self.port.exchange([0,Pos], Lenth)
            print(device_id)
        except:
            print("An exception occurred")
            return 0

    def DeviceAddress(self,Address):
        self.DA = Address;
        return 0

    def WriteName(self,Pos,Name):
        new_string = bytes(Name,"ascii")
        Init = [0,Pos]
        Init += bytearray(new_string)
        self.port.write(Init)
        return 0

    def ReadByte(self,Pos):
        try:
            device_id = self.port.exchange([0,Pos], 1)
            return device_id
        except:
            print("An exception occurred")
            return 0

    def WriteByte(self,Loc,Byte):
        try:
            self.port.write(Loc, Byte)
        except:
            print("An exception occurred")
            return 0

    def ReadPage(self,Pos):
        try:
            device_id = self.port.exchange([0,Pos], 1)
            return device_id
        except:
            print("An exception occurred")
            return 0

    def WritePage(self,Pos,Byte): ## 16 bytes at a time
        try:
            self.port.write(Pos, Byte)
        except:
            print("An exception occurred")
            return 0



Device = EEPROM()
#Device.WriteName(0,"RickIsCool")
Device.ReadName(0,10)
##for i in range(9):
##    print(i, end=" ")
##    Device.SetCurrent(i)
##    time.sleep(3)

