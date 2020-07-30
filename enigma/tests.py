from rotor import *
from enigma import *

"""Testing Functionalites
"""

list_rotors = [ROTOR_I, ROTOR_II, ROTOR_III]
reflector = ROTOR_Reflector_A
plugboard = Plugboard("AV BS CG DL FU HZ IN KM OW RX")

engine = Enigma(list_rotors, reflector, plugboard)
print(engine)

print(engine.encrypt('Hello World'))

print(engine.decrypt(
    encoded_message='EAKYQ ZWPOB',
    rotors=list_rotors,
    reflector=reflector,
    plugboard=plugboard,
    rotors_positions= [17, 4, 15]
))