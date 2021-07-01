import mido
import time

#midiの絶対パスを書いてください
midipath = ""


ports = mido.get_output_names()
with mido.open_output(ports[0]) as outport:
    for msg in mido.MidiFile('midipath'):
        time.sleep(msg.time)
        if not msg.is_meta:
            outport.send(msg) 