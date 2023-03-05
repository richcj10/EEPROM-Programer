
from pyftdi import FtdiLogger
from pyftdi.i2c import I2cController, I2cIOError
from time import sleep
from array import array as Array
from binascii import hexlify
import time

DeviceAddress = 0x50
AddressSpace = 16


def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)


class EEPROM():

    def __init__(self):
        self._i2c = I2cController()
        self._i2c.configure('ftdi://ftdi:232h/1')
        self.gpio = self._i2c.get_gpio()
        self.gpio.set_direction(240,240)
        self.DA = DeviceAddress
        self.Bit = AddressSpace
        self.port = self._i2c.get_port(self.DA)

    def SetPower(self,ctrl):
        pins = self.gpio.read(True)
        if(ctrl == 1):
            pins = set_bit(pins,7)
        else:
            pins = clear_bit(pins,7)

        self.gpio.write(pins)

    def SetAllert(self,ctrl):
        pins = self.gpio.read(True)
        if(ctrl == 1):
            pins = set_bit(pins,6)
        else:
            pins = clear_bit(pins,6)

        self.gpio.write(pins)

    def SetUSBReset(self,ctrl):
        pins = self.gpio.read(True)
        if(ctrl == 1):
            pins = set_bit(pins,5)
        else:
            pins = clear_bit(pins,5)

        self.gpio.write(pins)

    def ReadName(self,Pos,Lenth):
        try:
            if(self.Bit == 16):
                #print("16bit")
                device_id = self.port.exchange([0,Pos], Lenth)
                #print(device_id)
            if(self.Bit == 8):
                #print("8bit")
                device_id = self.port.exchange([Pos], Lenth)
                #print(device_id)
        except:
            print("An exception occurred")
            return 0

    def DeviceAddress(self,Address):
        self.DA = Address;
        self.port = self._i2c.get_port(self.DA)
        return 0

    def DeviceBit(self,Bit):
        self.Bit = Bit;
        return 0

    def WriteName(self,Pos,Name):
        new_string = bytes(Name,"ascii")
        if(self.Bit == 16):
            #print("16bit")
            Init = [0,Pos]
        if(self.Bit == 8):
            #print("8bit")
            Init = [Pos]
        Init += bytearray(new_string)
        self.port.write(Init)
        return 0

    def ReadByte(self,Pos):
        try:
            if(self.Bit == 16):
                #print("16bit")
                device_Pkt = self.port.exchange([0,Pos], 1)
                return device_Pkt
            if(self.Bit == 8):
                #print("8bit")
                device_Pkt = self.port.exchange([Pos], 1)
                return device_Pkt
        except:
            print("An exception occurred")
            return 0

    def WriteByte(self,Pos,Byte):
        try:
            self.port.write_to(Pos, Byte)
        except Exception as A: #(Where A is a temporary variable)
            print(A)
            return 0

    def ReadPage(self,Pos): ## 8 Bytes at a time? 
        try:
            if(self.Bit == 16):
                #print("16bit")
                List = self.port.exchange([0,Pos], 8)
                return List
            if(self.Bit == 8):
                #print("8bit")
                List = self.port.exchange([Pos], 8)
                return List
        except:
            print("An exception occurred")
            return 0

    def WritePage(self,Pos,ByteArray): ## 16 bytes at a time
        try:
            #print("First List:")
            #print(ByteArray)
            if(self.Bit == 16):
                #print("16bit")
                Init = [0,Pos]
            if(self.Bit == 8):
                #print("8bit")
                Init = [Pos]
            Init += bytearray(ByteArray)
            self.port.write(Init)
        except Exception as A: #(Where A is a temporary variable)
            print(A)
            return 0



#Device = EEPROM()
#Device.SetAllert(0)
#Device.SetPower(1)
#Device.WriteName(0,"RickIsCool")
#Device.ReadName(0,10)
##for i in range(9):
##    print(i, end=" ")
##    Device.SetCurrent(i)
##    time.sleep(3)

