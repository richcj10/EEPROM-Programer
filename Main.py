import sys
import time
import Define as DF
from array import array
import re
import IODriver as IO
import pickle
import ChargerTestGUI as GUI
import EEPROMMap as EM

BinFile = []
AppRunning = 1
EEPROMDevice = 0

#USB Hub,PD,MFB,Drawer
EEPROMAddress = [0x50,0x50,0x50,0x50]

##This function is a "all Clear" helpper that defults the loads and power supplys to defults / off.
def onExit():
    sys.exit()

def hexify(s):
    return "b'" + re.sub(r'.', lambda m: f'\\x{ord(m.group(0)):02x}', s.decode('latin1')) + "'"

##This is the map function to get test time to 0-100% for the GUI task bar. 
def mapval(x,in_min,in_max):
  return (x - in_min) * (100) / (in_max - in_min)

def SetTestMode():
    global EEPROMDevice
    mode = DF.GetTestModeGUI()
    print("New Mode ", mode)
    EEPROMDevice.DeviceAddress(EEPROMAddress[mode])
    EEPROMDevice.DeviceBit(8)

def TestI2C():
    global EEPROMDevice
    try:
        EEPROMDevice = IO.EEPROM()
        DF.SetDeviceDetected(1)
        print("I2C Device OK")
    except:
        print("No I2C Device?")

def SendBinFile():
    global EEPROMDevice
    CheckPass = 0
    try:
        FilePath = DF.GetBinFile()
        file = open(FilePath,"rb")
        #print("Send to Device")
        #print(FilePath)
        BinFile = file.read(32)
        #print(hexify(BinFile))
        First16 = BinFile[0:16]
        print(hexify(First16))
        Second16 = BinFile[16:32]
        print(hexify(Second16))
        EEPROMDevice.WritePage(0,First16)
        time.sleep(0.5)
        EEPROMDevice.WritePage(16,Second16)
        time.sleep(0.5)
        ReadValue = EEPROMDevice.ReadPage(0)
        print(hexify(ReadValue))
        time.sleep(0.5)
        ReadValue += EEPROMDevice.ReadPage(8)
        time.sleep(0.5)
        print(hexify(ReadValue))
        if(First16 == ReadValue):
            print("Good!")
            CheckPass = 1
        else:
            print("Bad!")
    except Exception as A: #(Where A is a temporary variable)
        print(A)
    finally:
        file.close()
        return CheckPass

def ProgramMFB():
    global EEPROMDevice
    CheckPass = 0
    try:
        ReturnByte = []
        EM.SetEEPROM(EM.MFB)
        EM.StartEEPROMMap() 
        EM.PackatizeEEPROMDF()
        SendArray = EM.ReturnEEPROMMap()
        Size  = EM.ReturnEEPROMMapSize()
        print(SendArray)
        print(Size)

        for x in range(Size): ##Add P#
            bytes_val = int(SendArray[x]).to_bytes(1, 'big')
            #print("Byte = ",Data)
            #print("x = ",x)
            EEPROMDevice.WriteByte(x,bytes_val)
            #time.sleep(0.1)

        time.sleep(0.5)
        for x in range(Size):
            Return = EEPROMDevice.ReadByte(x)
            ReturnByte.append(Return[0])

        Returned = bytearray(ReturnByte)
        print(Returned)
        if(SendArray == Returned):
            print("Good!")
            CheckPass = 1
    except Exception as A: #(Where A is a temporary variable)
        print(A)
    finally:
        return CheckPass

def ReadMFB():
    global EEPROMDevice
    CheckPass = 0
    try:
        EM.SetEEPROM(EM.MFB)
        EM.StartEEPROMMap() 

        ReturnByte = []
        for x in range(18):
            Return = EEPROMDevice.ReadByte(x)
            ReturnByte.append(Return[0])

        ##nEED TO LOOK AT BYTE, Check Lenth
        Returned = bytearray(ReturnByte)
        EM.SetEEPROMFile(Returned)
        result = EM.EEPROMMapValidate()
        if(result):
            EM.SaveToDF()
            CheckPass = 1
    except Exception as A: #(Where A is a temporary variable)
        print(A)
    finally:
        return CheckPass

def ProgramPD():
    global EEPROMDevice
    CheckPass = 0
    try:
        ReturnByte = []
        EM.SetEEPROM(EM.PD)
        EM.StartEEPROMMap() 
        EM.PackatizeEEPROMDF()
        SendArray = EM.ReturnEEPROMMap()
        Size  = EM.ReturnEEPROMMapSize()
        print(SendArray)
        print(Size)

        for x in range(Size): ##Add P#
            bytes_val = int(SendArray[x]).to_bytes(1, 'big')
            #print("Byte = ",Data)
            #print("x = ",x)
            EEPROMDevice.WriteByte(x,bytes_val)
            #time.sleep(0.1)

        time.sleep(0.5)
        for x in range(Size):
            Return = EEPROMDevice.ReadByte(x)
            ReturnByte.append(Return[0])

        Returned = bytearray(ReturnByte)
        print(Returned)
        if(SendArray == Returned):
            print("Good!")
            CheckPass = 1
    except Exception as A: #(Where A is a temporary variable)
        print(A)
    finally:
        return CheckPass
        
if __name__ == "__main__":
    DF.initialize()  ##Set up Data Dictonary, (DF)
    TestI2C()## Test if we have a good I2C Device
    GUIHandel = GUI.PythonGUI()  ##Start GUI
    if(DF.GetDeviceDetected()):
        GUIHandel.GUIStatus(DF.DEVICEOK)
        GUIHandel.TestMode(0)
    else:
        GUIHandel.GUIErrorMsgBox("No I2C Device!")
    while 1:
        if(DF.GetStatus() == 1):
            print("Program USB Hub")
            GUIHandel.GUIStatus(DF.PROGRAM)
            GUI.GlobalRoot.update()
            if(SendBinFile()):
                GUIHandel.GUIStatus(DF.PASS)
            else:
                GUIHandel.GUIStatus(DF.FAIL)
                GUIHandel.GUIErrorMsgBox(" Failed ")
            DF.SetStatus(0)
        if(DF.GetStatus() == 2):
            GUIHandel.GUIStatus(DF.PROGRAM)
            GUI.GlobalRoot.update()
            Process = ProgramMFB()
            if(Process == 1):
                print("Pass")
                GUIHandel.GUIStatus(DF.PASS)
            else:
                GUIHandel.GUIStatus(DF.FAIL)
            DF.SetStatus(0)
        if(DF.GetStatus() == 3):
            GUIHandel.GUIStatus(DF.PROGRAM)
            GUI.GlobalRoot.update()
            Process = ProgramPD()
            if(Process == 1):
                GUIHandel.GUIStatus(DF.PASS)
            else:
                GUIHandel.GUIStatus(DF.FAIL)
            DF.SetStatus(0)
        if(DF.GetUpdateModeGUI()):
            DF.SetUpdateModeGUI(0)
            SetTestMode()
        if(DF.GetAppRun()): ##If  app is still running
            GUI.GlobalRoot.update() #keep updating GUI, if this isn't clled regularly, app will "hang" 
        else:
            GUI.GlobalRoot.destroy()  ##If app has closed ( Exit button pushed )
            break
    onExit() ##Play "clean up"
