


PASS = 1
FAIL = 2

TRUE = 1
FALSE = 0

DEVICEOK = 1
PROGRAM = 2
PASS = 3
FAIL = 4

BinFile = ""
Status = 0
DeviceDetected = 0
TestModeGUI = 0
UpdateModeGUI = 0

def initialize(): 
    global BinFile
    global AppRunning
    global Status
    global DeviceDetected
    global TestModeGUI
    global UpdateModeGUI
    BinFile = ""
    AppRunning = 1
    DeviceDetected = 0
    TestModeGUI = 0
    UpdateModeGUI = 0

def SetAppRun(val):
    global AppRunning
    AppRunning = val

def GetAppRun():
    global AppRunning
    return(AppRunning)

def SetStatus(x):
    global Status
    Status = x

def GetStatus():
    global Status
    return(Status)

def SetBinFile(val):
    global BinFile
    BinFile = val

def GetBinFile():
    global BinFile
    return(BinFile)

def SetDeviceDetected(x):
    global DeviceDetected
    DeviceDetected = x

def GetDeviceDetected():
    global DeviceDetected
    return(DeviceDetected)

def SetTestModeGUI(x):
    global TestModeGUI
    TestModeGUI = x

def GetTestModeGUI():
    global TestModeGUI
    return(TestModeGUI)

def SetUpdateModeGUI(x):
    global UpdateModeGUI
    UpdateModeGUI = x

def GetUpdateModeGUI():
    global UpdateModeGUI
    return(UpdateModeGUI)
