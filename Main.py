import sys
import time
import Define as DF
from array import array


import ChargerTestGUI as GUI

TestConfigArray = []
AppRunning = 1


CHDelay = 0.5


##This function is a "all Clear" helpper that defults the loads and power supplys to defults / off.
def onExit():
    sys.exit()


##This is the map function to get test time to 0-100% for the GUI task bar. 
def mapval(x,in_min,in_max):
  return (x - in_min) * (100) / (in_max - in_min)
        
if __name__ == "__main__":
    DF.initialize()  ##Set up Data Dictonary, (DF) 
    GUIHandel = GUI.PythonGUI()  ##Start GUI 
    while 1:
        if(DF.GetTestSetup()):
            print("Get New Com Port fcn")
            SetUpTestFixture()
            DF.SetTestSetup(0)
        if(DF.GetCHUpdate()):  ##If CH Has updated, Set combo Box 
            ChannelTest()
            DF.SetCHUpdate(0) ##Clear flag
        if(DF.GetTestStart()): ##If GUI set Start test flag 
            ##print("Running")
            RunTests() #start tests
            DF.SetTestStart(0) ##Clear flag
            GUIHandel.LockTestTypes(0) #Unlock combobox and start test buttons
        if(DF.GetAppRun()): ##If  app is still running
            GUI.GlobalRoot.update() #keep updating GUI, if this isn't clled regularly, app will "hang" 
        else:
            GUI.GlobalRoot.destroy()  ##If app has closed ( Exit button pushed )
            break
    onExit() ##Play "clean up"
