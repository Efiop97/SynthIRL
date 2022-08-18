import mido
import re

from sqlalchemy import null



def midiConnect(portnum):
    instrument  = mido.get_input_names()
    inport = mido.open_input(instrument[portnum])
    return inport

def checkMidiConnection(inport):
    if str(inport) is not null:
        connected = True
    else:
        connected = False
    return connected

def getMidinote(msg):
    try:
        note = re.search('.note=(...)', str(msg)).group(1)
        return int(note)
    except AttributeError as err:
        return 0
  



def getVolocity(msg):
    try:
        velo = re.search('.velocity=(..)', str(msg)).group(1)
        return int(velo)
    except AttributeError as err:
        return 0

def noteOn(msg):
    press = re.search(".note_on", str(msg))
    if press:
        note_on = True
    else:
        note_on = False
    return note_on

def noteOff(msg):
    note_off = True
    press = re.search(".note_off", str(msg))
    vel = press = re.search(".velocity=0", str(msg))
    if press or vel:
        note_off = True
    else:
        note_off = False
    return note_off

def noteToFreq(note):
    a = 440 #frequency of A4 (common value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

def midiListener(inport):
    msg = inport.receive()
    return [str(msg)]

def cc_number_value(msg):
    try:
        control = re.search(".control=(..)", str(msg)).group(1)
        val = re.search('.value=(..)', str(msg)).group(1)
        cc = (control, val)
        return cc
    except AttributeError as err:
        return 0

def cc_change(msg):
    control_change = False
    chnage = re.search(".control_change", str(msg))
    if chnage:
        control_change = True
    return control_change


# port = midiConnect(0)
# while True:
#     event = midiListener(port)
#     note = getMidinote(event)
#     if noteOn(event):
#         freq = noteToFreq(note)
#         print(note, freq)
#     if noteOff(event):
#         print(event)
#     elif cc_change(event):
#         cc = cc_number_value(event)
#         print(cc)



    

#control_change channel=0 control=32 value=12 time=0

