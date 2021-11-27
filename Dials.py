# May well form foundation of Bas program

####################################

import smbus
B = smbus.SMBus(1)
a = 0x20
B.write_byte_data(a,0x00,0xff) #inputs
B.write_byte_data(a,0x01,0xff) #inputs
B.write_byte_data(a,0x0C,0xff) #pullups
B.write_byte_data(a,0x0D,0xff) #pullups

def ReadBank(bank,adr=0x20):
	Banks = {"A": 0x12, "B": 0x13}
	Result = map(int,list(bin(B.read_byte_data(adr,Banks[bank])).split("0b")[1].zfill(8)))
	return Result[:4], Result[4:]

####################################
Izero = lambda x: x.index(0)

def ShowDials():
        i, ii = ReadBank("A")
        iii, iv = ReadBank("B")
        Dials = [i, ii, iii, iv]
        return map(Izero, Dials)


