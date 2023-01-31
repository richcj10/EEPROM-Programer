import sys
import time
import Define as DF
from array import array
import re
import IODriver as IO

import ChargerTestGUI as GUI

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
        print(hexify(BinFile))
        First16 = BinFile[0:16]
        #print(hexify(First16))
        Second16 = BinFile[16:32]
        #print(hexify(Second16))
        EEPROMDevice.WritePage(0,First16)
        time.sleep(0.5)
        EEPROMDevice.WritePage(16,Second16)
        time.sleep(0.5)
        ReadValue = EEPROMDevice.ReadPage(0)
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
        print(a)
    finally:
        file.close()
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
            if(SendBinFile()):
                GUIHandel.GUIStatus(DF.PASS)
            else:
                GUIHandel.GUIStatus(DF.FAIL)
                GUIHandel.GUIErrorMsgBox(" Failed ")
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
