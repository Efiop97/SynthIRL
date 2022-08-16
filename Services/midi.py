import mido

names = mido.get_input_names()
print(names)
out_port = mido.open_output()

inport = mido.open_input(names[1])
msg = inport.receive()

print(msg)