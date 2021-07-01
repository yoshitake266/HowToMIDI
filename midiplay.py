import mido
import time

ports = mido.get_output_names()
with mido.open_output(ports[0]) as outport:
    for msg in mido.MidiFile('desktop/HowToMIDI/megalovania.mid'):
        time.sleep(msg.time)
        if not msg.is_meta:
            outport.send(msg) 