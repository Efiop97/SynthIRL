
import mido

instrument = mido.get_input_names()
print(instrument)
inport = mido.open_input(instrument[2])
events = []
while True:
    msg = inport.receive()
    events.append(msg)
    print(events)
    events = []
