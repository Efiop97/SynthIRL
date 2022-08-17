import mido
import re


def midiConnect(portnum):
    instrument  = mido.get_input_names()
    inport = mido.open_input(instrument[portnum])
    return inport

def getMidinote(msg):
    note = re.search('note=(...)', str(msg)).group(1)
    return int(note)

def getVolocity(msg):
    velo = re.search('velocity=(..)', str(msg)).group(1)
    return int(velo)

def noteOn(msg):
    note_on = False
    press = re.search("note_on", str(msg))
    if press:
        note_on = True
    else:
        note_on = False
    return note_on

def noteOff(msg):
    note_off = True
    press = re.search("note_off", str(msg))
    if press:
        note_off = True
    return note_off

def noteToFreq(note):
    a = 440 #frequency of A4 (common value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

def midiListener(inport):
    msg = inport.receive()
    return msg

def cc_number_value(msg):
    control = re.search("control=(..)", str(msg)).group(1)
    val = re.search('value=(..)', str(msg)).group(1)
    cc = (control, val)
    return cc

def cc_change(msg):
    control_change = False
    chnage = re.search("control_change", str(msg))
    if chnage:
        control_change = True
    return control_change


# port = midiConnect(2)
# while True:
#     event = midiListener(port)
#     # print(event)
#     if noteOn(event):
#         note = getMidinote(event)
#         print(event)
#     elif cc_change(event):
#         cc = cc_number_value(event)
#         print(cc)



    

#control_change channel=0 control=32 value=12 time=0

