
vin_offset = 0
vinilim_offset = 1
vinsclim_offset = 2
mobvout_offset = 3
mobvoutper_offset = 4
mobItest_offset = 5
lfpvout_offset = 6
lfpvoutper_offset = 7
lfpItest_offset = 8
burntime_offset = 9
channelcount_offset = 10
ArrayLen = 11

CH1 = 1
CH2 = 2
CH3 = 3
CH4 = 4

PASS = 1
FAIL = 2

TRUE = 1
FALSE = 0

TestStarted = 0
AppRunning = 1
CHUpdate = 0
CHCount = 0
CH1Status = 0
CH1VIn = 0.0
CH1IIn = 0.0
CH1VOut = 0.0
CH1IOut = 0.0
CH2Status = 0
CH2VIn = 0.0
CH2IIn = 0.0
CH2VOut = 0.0
CH2IOut = 0.0
CH3Status = 0
CH3VIn = 0.0
CH3IIn = 0.0
CH3VOut = 0.0
CH3IOut = 0.0
CH4Status = 0
CH4VIn = 0.0
CH4IIn = 0.0
CH4VOut = 0.0
CH4IOut = 0.0
TestTime = 0
TestSetup = 0

CH1TestPassPU = 0
CH2TestPassPU = 0
CH3TestPassPU = 0
CH4TestPassPU = 0

CH1TestPassVOUT = 0
CH2TestPassVOUT = 0
CH3TestPassVOUT = 0
CH4TestPassVOUT = 0

CH1TestPass = 0
CH2TestPass = 0
CH3TestPass = 0
CH4TestPass = 0

CH1Type = 0
CH2Type = 0
CH3Type = 0
CH4Type = 0

def initialize(): 
    global TestStarted
    global AppRunning
    global AppRunning
    global CHUpdate
    global CHCount
    global CH1VIn
    global CH1IIn
    global CH1VOut
    global CH1IOut
    global CH2VIn
    global CH2IIn
    global CH2VOut
    global CH2IOut
    global CH3VIn
    global CH3IIn
    global CH3VOut
    global CH3IOut
    global CH4VIn
    global CH4IIn
    global CH4VOut
    global CH4IOut
    global TestTime
    global CH1TestPU
    global CH1TestPassPU
    global CH2TestPassPU
    global CH3TestPassPU
    global CH4TestPassPU
    global CH1TestPassVOUT
    global CH2TestPassVOUT
    global CH3TestPassVOUT
    global CH4TestPassVOUT
    global CH1TestPass
    global CH2TestPass
    global CH3TestPass
    global CH4TestPass
    global CH1Type
    global CH2Type
    global CH3Type
    global CH4Type
    global TestSetup
    global CH1Status
    global CH2Status
    global CH3Status
    global CH4Status
    CH1Status = 0
    CH2Status = 0
    CH3Status = 0
    CH4Status = 0
    TestStarted = 0 
    AppRunning = 1
    CH1VIn = 0.0
    CH1IIn = 0.0
    CH1VOut = 0.0
    CH1IOut = 0.0
    CH2VIn = 0.0
    CH2IIn = 0.0
    CH2VOut = 0.0
    CH2IOut = 0.0
    CH3VIn = 0.0
    CH3IIn = 0.0
    CH3VOut = 0.0
    CH3IOut = 0.0
    CH4VIn = 0.0
    CH4IIn = 0.0
    CH4VOut = 0.0
    CH4IOut = 0.0
    TestTime = 0
    CH1TestPassPU = 0
    CH2TestPassPU = 0
    CH3TestPassPU = 0
    CH4TestPassPU = 0
    CH1TestPassVOUT = 0
    CH2TestPassVOUT = 0
    CH3TestPassVOUT = 0
    CH4TestPassVOUT = 0
    CH1TestPass = 0
    CH2TestPass = 0
    CH3TestPass = 0
    CH4TestPass = 0
    CH1Type = 0
    CH2Type = 0
    CH3Type = 0
    CH4Type = 0
    CHUpdate = 0
    CHCount = 0
    TestSetup = 0

def SetTestStart(val):
    global TestStarted
    TestStarted = val

def SetAppRun(val):
    global AppRunning
    AppRunning = val

def GetTestStart():
    global TestStarted
    return(TestStarted)

def GetAppRun():
    global AppRunning
    return(AppRunning)

def SetTestResultPU(ch, val):
    global CH1TestPassPU
    global CH2TestPassPU
    global CH3TestPassPU
    global CH4TestPassPU
    if(ch == 1):
        CH1TestPassPU = val
    if(ch == 2):
        CH2TestPassPU = val
    if(ch == 3):
        CH3TestPassPU = val
    if(ch == 4):
        CH4TestPassPU = val

def GetTestResultPU(ch):
    global CH1TestPassPU
    global CH2TestPassPU
    global CH3TestPassPU
    global CH4TestPassPU
    if(ch == 1):
        return(CH1TestPassPU)
    if(ch == 2):
        return(CH2TestPassPU)
    if(ch == 3):
        return(CH3TestPassPU)
    if(ch == 4):
        return(CH4TestPassPU)

def SetTestResultPassVOUT(ch, val):
    global CH1TestPassVOUT
    global CH2TestPassVOUT
    global CH3TestPassVOUT
    global CH4TestPassVOUT
    if(ch == 1):
        CH1TestPassVOUT = val
    if(ch == 2):
        CH2TestPassVOUT = val
    if(ch == 3):
        CH3TestPassVOUT = val
    if(ch == 4):
        CH4TestPassVOUT = val

def GetTestResultPassVOUT(ch):
    global CH1TestPassVOUT
    global CH2TestPassVOUT
    global CH3TestPassVOUT
    global CH4TestPassVOUT
    if(ch == 1):
        return(CH1TestPassVOUT)
    if(ch == 2):
        return(CH2TestPassVOUT)
    if(ch == 3):
        return(CH3TestPassVOUT)
    if(ch == 4):
        return(CH4TestPassVOUT)

def SetTestResultPass(ch, val):
    global CH1TestPass
    global CH2TestPass
    global CH3TestPass
    global CH4TestPass
    if(ch == 1):
        CH1TestPass = val
    if(ch == 2):
        CH2TestPass = val
    if(ch == 3):
        CH3TestPass = val
    if(ch == 4):
        CH4TestPass = val

def GetTestResultPass(ch):
    global CH1TestPass
    global CH2TestPass
    global CH3TestPass
    global CH4TestPass
    if(ch == 1):
        return(CH1TestPass)
    if(ch == 2):
        return(CH2TestPass)
    if(ch == 3):
        return(CH3TestPass)
    if(ch == 4):
        return(CH4TestPass)

def SetCh1Val(InV,InI,OutV,OutI):
    global CH1VIn
    global CH1IIn
    global CH1VOut
    global CH1IOut
    CH1VIn = InV
    CH1IIn = InI
    CH1VOut = OutV
    CH1IOut = OutI

def SetCh2Val(InV,InI,OutV,OutI):
    global CH2VIn
    global CH2IIn
    global CH2VOut
    global CH2IOut
    CH2VIn = InV
    CH2IIn = InI
    CH2VOut = OutV
    CH2IOut = OutI

def SetCh3Val(InV,InI,OutV,OutI):
    global CH3VIn
    global CH3IIn
    global CH3VOut
    global CH3IOut
    CH3VIn = InV
    CH3IIn = InI
    CH3VOut = OutV
    CH3IOut = OutI

def SetCh4Val(InV,InI,OutV,OutI):
    global CH4VIn
    global CH4IIn
    global CH4VOut
    global CH4IOut
    CH4VIn = InV
    CH4IIn = InI
    CH4VOut = OutV
    CH4IOut = OutI

def GetCH1():
    global CH1VIn
    global CH1IIn
    global CH1VOut
    global CH1IOut
    returnlist = [CH1VIn,CH1IIn,CH1VOut,CH1IOut]
    return returnlist

def GetCH2():
    global CH2VIn
    global CH2IIn
    global CH2VOut
    global CH2IOut
    returnlist = [CH2VIn,CH2IIn,CH2VOut,CH2IOut]
    return returnlist

def GetCH3():
    global CH3VIn
    global CH3IIn
    global CH3VOut
    global CH3IOut
    returnlist = [CH3VIn,CH3IIn,CH3VOut,CH3IOut]
    return returnlist

def GetCH4():
    global CH4VIn
    global CH4IIn
    global CH4VOut
    global CH4IOut
    returnlist = [CH4VIn,CH4IIn,CH4VOut,CH4IOut]
    return returnlist

def SetChType(ch,val):
    global CH1Type
    global CH2Type
    global CH3Type
    global CH4Type
    if(ch == 1):
        CH1Type = val
    if(ch == 2):
        CH2Type = val
    if(ch == 3):
        CH3Type = val
    if(ch == 4):
        CH4Type = val

def GetChType(ch):
    global CH1Type
    global CH2Type
    global CH3Type
    global CH4Type
    if(ch == 1):
        return(CH1Type)
    if(ch == 2):
        return(CH2Type)
    if(ch == 3):
        return(CH3Type)
    if(ch == 4):
        return(CH4Type)

def SetCHUpdate(x):
    global CHUpdate
    CHUpdate = x

def GetCHUpdate():
    global CHUpdate
    return(CHUpdate)

def SetCHCount(x):
    global CHCount
    CHCount = x

def GetCHCount():
    global CHCount
    return(CHCount)

def SetTestSetup(x):
    global TestSetup
    TestSetup = x

def GetTestSetup():
    global TestSetup
    return(TestSetup)

def SetTestTime(x):
    global TestTime
    TestTime = x

def GetTestTime():
    global TestTime
    return(TestTime)

def GetCH1Status():
    global CH1Status
    return(CH1Status)

def SetCH1Status(x):
    global CH1Status
    CH1Status = x

def GetCH2Status():
    global CH2Status
    return(CH2Status)

def SetCH2Status(x):
    global CH2Status
    CH2Status = x

def GetCH3Status():
    global CH3Status
    return(CH3Status)

def SetCH3Status(x):
    global CH3Status
    CH3Status = x

def GetCH4Status():
    global CH4Status
    return(CH4Status)

def SetCH4Status(x):
    global CH4Status
    CH4Status = x