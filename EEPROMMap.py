import Define as DF

eepromMap = 0
eepromType = 0
MFB = 1
PD = 2
MEDBIN = 3

class MFB_EEPROM:
  Type = 'M'
  Rev = '1'
  ProductionPartNumber = ""
  ProductionPartRev = ""
  DayOfManufacture = 0
  MonthOfManufacture = 0
  YearOfManufacture = 0
  First_CRC = 0
  Error = 0
  Error_CRC = 0
  DeviceSerialNumberLenth = 0
  DeviceSerialNumber = ""
  DeviceSerialNumberCRC = 0
  output_array_len = 0
  output_array = None

class PD_EEPROM:
  Type = 'P'
  Rev = '1'
  ProductionPartNumber = ""
  ProductionPartRev = ""
  DayOfManufacture = 0
  MonthOfManufacture = 0
  YearOfManufacture = 0
  First_CRC = 0
  Error = 0
  Error_CRC = 0
  DeviceSerialNumberLenth = 0
  DeviceSerialNumber = ""
  DeviceSerialNumberCRC = 0
  output_array_len = 0
  output_array = None

class MEDBIN_EEPROM:
  Type = 'B'
  Rev = '1'
  ProductionPartNumber = ""
  ProductionPartRev = ""
  DayOfManufacture = 0
  MonthOfManufacture = 0
  YearOfManufacture = 0
  First_CRC = 0
  Error = 0
  Error_CRC = 0
  DeviceSerialNumberLenth = 0
  DeviceSerialNumber = ""
  DeviceSerialNumberCRC = 0
  output_array_len = 0
  output_array = None

def SetEEPROM(Type):
    global eepromType
    eepromType = Type

def StartEEPROMMap():
    global eepromMap
    global eepromType
    if(eepromType == MFB):
        eepromMap = MFB_EEPROM()
    if(eepromType == PD):
        eepromMap = PD_EEPROM()
    if(eepromType == MEDBIN):
        eepromMap = MEDBIN_EEPROM()

def PackatizeEEPROMDF():
    global eepromMap
    global eepromType
    print("hi")
    eepromMap.output_array = bytearray(str.encode(eepromMap.Type))
    eepromMap.output_array.extend(eepromMap.Rev.encode('utf-8')) ##Rev of Data Format
    CleanedString = DF.GetPart()[0].rstrip()
    Lenth = len(CleanedString)
    for x in range(Lenth): ##Add P#
        eepromMap.output_array.extend(CleanedString[x].encode('utf-8'))
    eepromMap.output_array.extend(DF.GetPart()[1].encode('utf-8'))
    eepromMap.output_array.extend(DF.GetDayMonthYear()[0].encode('utf-8')) ##Day
    eepromMap.output_array.extend(DF.GetDayMonthYear()[1].encode('utf-8')) ##Month
    eepromMap.output_array.extend(DF.GetDayMonthYear()[2].encode('utf-8')) ##Year 20XX
    CRC = crc_poly(eepromMap.output_array,8,0x07)
    print("CRC 1 = ", CRC)
    eepromMap.output_array += bytearray(CRC.to_bytes(1, 'little')) ##CRC
    eepromMap.output_array.append(0) ##ERROR
    CRC = 0##crc_poly(0,8,0x07)
    print("CRC 2 = ", CRC)
    eepromMap.output_array += bytearray(CRC.to_bytes(1, 'little')) ##ERROR CRC
    CleanedString = DF.GetSN().rstrip()
    Lenth = len(CleanedString)
    eepromMap.output_array += bytearray(Lenth.to_bytes(1, 'little')) ##SN Lenth
    for x in range(Lenth): ##Add P#
        Data  = CleanedString[x]
        ##Checksum = Data ^ Checksum
        eepromMap.output_array.extend(Data.encode('utf-8'))
    CRCInput = bytearray(CleanedString.encode('utf-8'))
    CRC = crc_poly(CRCInput,8,0x07)
    print("CRC 3 = ", CRC)
    eepromMap.output_array += bytearray(CRC.to_bytes(1, 'little')) ##SN CRC
    eepromMap.output_array_len = len(eepromMap.output_array)

def ReturnEEPROMMap():
    global eepromMap
    return eepromMap.output_array

def ReturnEEPROMMapSize():
    global eepromMap
    return eepromMap.output_array_len

def SetEEPROMFile(Array):
    global eepromMap
    eepromMap.output_array = Array

def crc_poly(data, n, poly, crc=0, ref_in=False, ref_out=False, xor_out=0):
    g = 1 << n | poly  # Generator polynomial

    # Loop over the data
    for d in data:

        # XOR the top byte in the CRC with the input byte
        crc ^= d << (n - 8)
        # Loop over all the bits in the byte
        for _ in range(8):
            # Start by shifting the CRC, so we can check for the top bit
            crc <<= 1

            # XOR the CRC if the top bit is 1
            if crc & (1 << n):
                crc ^= g

    # Return the CRC value
    return crc ^ xor_out
