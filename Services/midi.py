import mido
import re

instrument = mido.get_input_names()
inport = mido.open_input(instrument[2])
events = []


def getMidinote(msg):
    note = ""
    if 'clock' not in str(msg):
        note = re.search('note=(..)', str(msg)).group(1)
    return note

def noteOn(msg):
    note_on = False
    if 'clock' not in str(msg):
        press = re.search("note_on", str(msg))
        if press:
            note_on = True
        return note_on


def noteOff(msg):
    note_off = False
    if 'clock' not in str(msg):
        press = re.search("note_off", str(msg))
        if press:
            note_off = True
        return note_off


while True:
    msg = inport.receive()
    if 'clock' not in str(msg): 
        if noteOn:
            print(getMidinote(msg))
        if noteOff:
            print(getMidinote(msg))



