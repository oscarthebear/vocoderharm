from pyo import *

s = Server()

# To Find what number to put in the Input and Output
# print("Audio host APIs:")'

# pa_list_host_apis()
# pa_list_host_devices()

# print("Default input device: " % pa_get_default_input())
# print("Default output device: " % pa_get_default_output())


# Set Input & Output to Universal Audio

s.setInputDevice(2)
s.setOutputDevice(2)

s.boot()

mic = Input().play().out()

harm_3 = Harmonizer(mic, transpo=4).out()
harm_5 = Harmonizer(mic, transpo=7).out()
harm_7 = Harmonizer(mic, transpo=11).out()


s.start
s.gui(locals=())
