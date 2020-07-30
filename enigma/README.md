# enigma

enigma is a script that aims to simulate the historic machine used in World War II called Enigma.

## 💡 About Enigma

The machine (in its simplest form) consisted of a keyboard, lamps
(one for each letter), a plugboard, an entry drum, three rotors, and
a reflector.
The cipher clerk presses a key, advancing the right-most rotor by
one step and closing an electrical circuit. Current flows from the
battery through the plugboard to the entry drum, from the entry
drum to the rotors, through the rotors to the reflector, and then
back through the rotors, entry drum, and plugboard, and lit up an
appropriate lamp.
The entry drum, rotors, reflector, and plugboard are what
scrambled the message

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/EnigmaMachineLabeled.jpg/800px-EnigmaMachineLabeled.jpg" width="400" height="500">

## 💧 Usage 

```python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import enigma
>>> import rotor
>>> print(rotor.ROTOR_V)
Name: V
Model: M3 Army
Date: December 1938
Wiring: VZBRGITYUPSDNHLXAWMJQOFECK

>>> engine = enigma.Enigma(
...     rotors=[rotor.ROTOR_V, rotor.ROTOR_IV, rotor.ROTOR_III],
...     reflector=rotor.ROTOR_Reflector_A,
...     plugboard=rotor.Plugboard("AV BS CG DL FU HZ IN KM OW RX"))

>>> print(engine)
Rotor 1
Name: V
Model: M3 Army
Date: December 1938
Wiring: VZBRGITYUPSDNHLXAWMJQOFECK

Rotor 2
Name: IV
Model: M3 Army
Date: December 1938
Wiring: ESOVPZJAYQUIRHXLNFTGKDCMWB

Rotor 3
Name: III
Model: Enigma 1
Date: 1930
Wiring: BDFHJLCPRTXVZNYEIWGAKMUSQO

Reflector
Name: Reflector A
Model: None
Date: None
Wiring: EJMZALYXVBWFCRQUONTSPIKHGD

Plugboard
AV BS CG DL FU HZ IN KM OW RX

>>> message = engine.encrypt("Hello World")
>>> print(message)

Encoded Message: UNQVQ LGLWX
Rotors initial positions: [26, 25, 10]
Plugs: AV BS CG DL FU HZ IN KM OW RX

>>> engine.decrypt(
...     encoded_message="UNQVQ LGLWX",
...     rotors=[rotor.ROTOR_V, rotor.ROTOR_IV, rotor.ROTOR_III],
...     reflector=rotor.ROTOR_Reflector_A,
...     rotors_positions=[26, 25, 10],
...     plugboard=rotor.Plugboard("AV BS CG DL FU HZ IN KM OW RX")
... )
'Decoded Message: HELLO WORLD'
```

## 📚 Resources
### Stanford Paper
[Stanford](https://web.archive.org/web/20171211191938/http://math.stanford.edu/~rmbellov/writings/enigma.pdf)
### Wikipedia
 
[Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine )

[Enigma rotor details](https://en.wikipedia.org/wiki/Enigma_rotor_details)
### Github
[pyEnigma](https://github.com/cedricbonhomme/pyEnigma)

### Others
[Enigma machine, how does the famous encryption device work?](https://dev.to/maxime1992/enigma-machine-how-does-the-famous-encryption-device-work-5aon)

[Brilliant](https://brilliant.org/wiki/enigma-machine/)