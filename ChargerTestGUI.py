import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.constants, tkinter.filedialog
import Define as DF
import datetime
import Main

import random
import datetime as dt

font1="Arial 16 bold"

TestConfigArrayGUI = []
ChannelCountGUI = 0
GlobalRoot = 0
EpromType = ["USB hub","PD","MFB","Drawer"]
ChannelType = ["Mobius","LFP"]

def DataSetter(TestArrayIN, TestChannelCount):
    global TestConfigArrayGUI
    global ChannelCountGUI
    TestConfigArrayGUI = TestArrayIN
    ChannelCountGUI = int(TestChannelCount)
    print(TestConfigArrayGUI)
    print(ChannelCountGUI)

class PythonGUI():
    def __init__(self):
        root = tk.Tk()
        global GlobalRoot
        GlobalRoot = root
        ##root.attributes('-fullscreen', True)
        ##root.configure(background='SteelBlue4')
        #scrW = root.winfo_screenwidth()
        #scrH = root.winfo_screenheight()
        #workwindow = str(1024) + "x" + str(768) + "+" + str(int((scrW - 1024) / 2)) + "+" + str(int((scrH - 768) / 2))
        #top1 = tk.Toplevel(root, bg="light blue")
        #top1.geometry(workwindow)
        root.geometry('500x500')
        root.title("  Enovate eeprom programer")
        root.attributes("-topmost", 1)  # make sure top1 is on top to start
        root.update()  # but don't leave it locked in place
        root.attributes("-topmost", 0)  # in case you use lower or lift
        # exit button - note: uses grid
        ##b3 = tk.Button(root, text="Exit", command= self.GUIShutdown)
        ##b3.grid(row=0, column=0, ipadx=10, ipady=10, pady=5, padx=5, sticky=tk.W + tk.N)

        self.MainLayer = ttk.Notebook(root)
        ##self.MainLayer.pack()
        ##self.StartLayer = ttk.Frame(self.MainLayer)
        ##self.TestSettings = ttk.Frame(self.MainLayer)
        ##self.ChannelConfig = ttk.Frame(self.MainLayer)

        ##self.MainLayer.add(self.StartLayer, text =' EEPROM Program    ')
        ##self.MainLayer.add(self.TestSettings, text =' EEPROM read ')
        ##self.MainLayer.add(self.ChannelConfig, text =' Channel Configure ')
        self.MainLayer.pack(expand = 1, fill ="both")

        self.VarSetup()
        self.MainWindowStart()
        ##self.ChannelConfigStart()
        ##self.TestSettingsStart()

    def VarSetup(self):
        t = datetime.datetime.now()
        self.ProgramTime = tk.StringVar()
        self.USBHubFile=tk.StringVar()
        self.USBHubFilePath=tk.StringVar()
        self.USBHubFile.set("*.bin")

        self.MFB_Type=tk.StringVar()
        self.MFB_SN=tk.StringVar()
        self.MFB_Day=tk.StringVar()
        self.MFB_Month=tk.StringVar()
        self.MFB_Year=tk.StringVar()
        self.MFB_Issue=tk.StringVar()
        self.MFB_Day.set(t.strftime("%d"))
        self.MFB_Month.set(t.strftime("%m"))
        self.MFB_Year.set(t.strftime("%y"))

        self.PD_Type=tk.StringVar()
        self.PD_SN=tk.StringVar()
        self.PD_Day=tk.StringVar()
        self.PD_Month=tk.StringVar()
        self.PD_Year=tk.StringVar()
        self.PD_Issue=tk.StringVar()
        self.PD_Day.set(t.strftime("%d"))
        self.PD_Month.set(t.strftime("%m"))
        self.PD_Year.set(t.strftime("%y"))

    def GetUSBBin(self):
        global GlobalRoot
        GlobalRoot.filename =  tk.filedialog.askopenfilename(initialdir = "C:/Users/",title = "Select file",filetypes = [("bin files","*.bin")])
        self.USBHubFilePath = GlobalRoot.filename

    def USBProgram(self):
        print("Program Hub")

    def MFBProgram(self):
        print("Program Hub")

    def PDProgram(self):
        print("Program Hub")

    def DCProgram(self):
        print("Program Hub")

    def MainWindowStart(self):

        self.StartPannelHome = tk.PanedWindow(self.MainLayer, height=400, width=200)
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)  # use a simple pack geometry to install this widget, use it all

        # fill the left side with a big LabelFrame
        self.TestControl = tk.LabelFrame(self.StartPannelHome, text="  EEPROM Config  ", relief=tk.GROOVE, width=100, height=500)  # do NOT pack it yet!
        self.Programlbl = tk.Label(self.TestControl, text="Program Option ")
        self.SelectProgram = ttk.Combobox(self.TestControl, values = EpromType)
        self.SelectProgram.current(0)       
        self.TestStatuslbl = tk.Label(self.TestControl, text="Status: ")
        self.TestProgress = ttk.Progressbar(self.TestControl, orient='vertical', length=300, mode='determinate')
        self.Programlbl.grid(padx=5, pady=5, row=0,column=0,sticky='n')
        self.SelectProgram.grid(padx=5, pady=5, row=1,column=0,sticky='n')
        self.TestStatuslbl.grid(padx=5, pady=5, row=2,column=0,sticky='n')
        self.TestProgress.grid(padx=5, pady=5, row=3,column=0)
        self.TestControl.pack()
        self.TestControl.pack_propagate(False)
        self.StartPannelHome.add(self.TestControl)
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)
        ##Test Output GUI
        self.TestOutput = tk.LabelFrame(self.StartPannelHome, text="  Program / Read  ", relief=tk.GROOVE)  # do NOT pack it yet!
        self.TestOutput.pack()
        self.TestOutput.pack_propagate(False)
        self.StartPannelHome.add(self.TestOutput)  # pw has its own "geometry" for arranging things internally
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)

        ##CH output List
        ####USB Hub
        self.USBLF = tk.LabelFrame(self.TestOutput, text="  Program USB Hub ", relief=tk.GROOVE)
        self.USBLF.grid(padx=5, pady=5, row=1,column=0,columnspan = 2)
        self.USBFile_entry = tk.Entry(self.USBLF,textvariable = self.USBHubFile)
        self.GetButton = tk.Button(self.USBLF,anchor=tk.W,command=self.GetUSBBin,padx=5,pady=5,text="Open")
        self.ProgramButton = tk.Button(self.USBLF,anchor=tk.W,command=self.USBProgram,padx=5,pady=5,text="Program")
        
        self.USBFile_entry.grid(padx=5, pady=5, row=1,column=1)
        self.GetButton.grid(padx=5, pady=5, row=2,column=0)
        self.ProgramButton.grid(padx=5, pady=5, row=2,column=1)
        ####MFB
        self.MFBLF = tk.LabelFrame(self.TestOutput, text="  Program MFB EEPROM ", relief=tk.GROOVE)
        self.MFBLF.grid(padx=5, pady=5, row=2,column=0,columnspan = 2)
        self.MFB_Day_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Day, width = 3)
        self.MFB_Month_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Month, width = 3)
        self.MFB_Year_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Year, width = 3)
        self.MFBProgramButton = tk.Button(self.MFBLF,anchor=tk.W,command=self.MFBProgram,padx=5,pady=5,text="MFB Program")
        
        self.MFB_Day_entry.grid(padx=5, pady=5, row=1,column=1)
        self.MFB_Month_entry.grid(padx=5, pady=5, row=2,column=0)
        self.MFB_Year_entry.grid(padx=5, pady=5, row=2,column=1)
        #self.MFB_Year_entry.grid(padx=5, pady=5, row=2,column=1)
        self.MFBProgramButton.grid(padx=5, pady=5, row=3,column=1)
        ####PD
        self.PDLF = tk.LabelFrame(self.TestOutput, text="  Program PD EEPROM ", relief=tk.GROOVE)
        self.PDLF.grid(padx=5, pady=5, row=3,column=0,columnspan = 2)
        self.PD_Day_entry = tk.Entry(self.PDLF,textvariable = self.PD_Day, width = 3)
        self.PD_Month_entry = tk.Entry(self.PDLF,textvariable = self.PD_Month, width = 3)
        self.PD_Year_entry = tk.Entry(self.PDLF,textvariable = self.PD_Year, width = 3)
        self.PDProgramButton = tk.Button(self.PDLF,anchor=tk.W,command=self.USBProgram,padx=5,pady=5,text=" PD Program")

        self.PD_Day_entry.grid(padx=5, pady=5, row=0,column=1)
        self.PD_Month_entry.grid(padx=5, pady=5, row=1,column=1)
        self.PD_Year_entry.grid(padx=5, pady=5, row=2,column=1)
        self.PDProgramButton.grid(padx=5, pady=5, row=3,column=1)

    def GUIShutdown(self):
        DF.SetAppRun(0)

    def GUIErrorMsgBox(self, msg):
        tk.messagebox.showerror("Title", msg,parent=self.MainLayer)
