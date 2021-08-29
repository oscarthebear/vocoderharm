from pyo import *

# Chord Voicings

# CHORD = {
#     "major7": [4, 7, 11],
#     "minor7": [3, 7, 10],
#     "dom7": [4, 7, 10],
#     "halfDim7": [4, 6, 10]
# }

s = Server()

# To Find what number to put in the Input and Output - When running make sure this the only code that is being run

# print("Audio host APIs:")
# pa_list_host_apis()
# pa_list_devices()

# print("Default input device: %i" % pa_get_default_input())
# print("Default output device: %i" % pa_get_default_output())


s.setInputDevice(2)
s.setOutputDevice(2)
s.boot()

mic = Input().play().out()

# Octaves
octave_high = Harmonizer(mic, transpo=12).out()
octave_low = Harmonizer(mic, transpo=-12).out()

# List of Harmonies
harm_3 = Harmonizer(mic, transpo=4).out()
# harm_3.ctrl(title="Harmony 3") - Visual GUI - If neeeded

harm_5 = Harmonizer(mic, transpo=7).out()
harm_7 = Harmonizer(mic, transpo=11).out()

s.start
s.gui(locals())
