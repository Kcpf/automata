# -*- coding: utf-8 -*-

"""Enigma Machine

This script aims to simulate the old machine used in World War II called Enigma.

Enigma was an electromechanical encryption machine with rotors,
used both to encrypt and to decrypt war codes, used in various forms in Europe since the 1920s.

Its fame comes from having been adapted by most German military forces since around 1930.
The ease of use and the supposed undecipherability of the code were the main reasons for its popularity.
The code was, however, deciphered, and the information contained in the messages he did not protect
is held responsible for the end of World War II at least a year earlier than expected.

Todo:
    * Code extension for Arduino and physical implementation

@author: Fernando
"""

import string
from random import randint
from rotor import *

class Enigma(object):
    """Simulates the mechanical reflector from Enigma Machine
    """
    def __init__(self, rotors, reflector, plugboard):
        """Initialize Enigma Machine object

        Args:
            rotors (list): list of rotors in sequence
            reflector (Reflector): reflector object
            plugboard (Plugboard): plugboard object
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def __str__(self):
        """Fancy print
        """
        return f"Rotor 1\n{self.rotors[0]}\n\nRotor 2\n{self.rotors[1]}\n\nRotor 3\n{self.rotors[2]}\n\nReflector\n{self.reflector}\n\nPlugboard\n{self.plugboard}\n"

    def reset_rotors(self):
        """Reset enigma rotors to initial configurations
        """
        for rotor in self.rotors:
            rotor.reset()

    def encrypt(self, message):
        """Given a message, encrypt it and give the configurations to decrypt.

        Args:
            message (String): Message to encrypt

        Returns:
            String: Text with encrypted message and rotors inital configurations
        """
        self.reset_rotors()
        encoded_message = ""

        for rotor in self.rotors:
            rotor.rotate(randint(0, 26))

        spins = [rotor.spins for rotor in self.rotors]

        for letter in message.upper():

            if not letter.isalpha():
                encoded_message += letter
                continue

            next_letter = letter

            next_letter = self.plugboard.return_letter(next_letter)

            self.rotors[0].rotate()

            if self.rotors[0].spins % 26 == 0:
                self.rotors[1].rotate()

            if self.rotors[1].spins % 26 == 0 and self.rotors[1].spins != 0:
                self.rotors[2].rotate()

            for rotor in self.rotors:
                next_letter = rotor.return_letter(next_letter)

            next_letter = self.reflector.return_letter(next_letter)

            for rotor in self.rotors[::-1]:
                next_letter = rotor.return_reverse_letter(next_letter)

            next_letter = self.plugboard.return_letter(next_letter)

            encoded_message += next_letter

        self.reset_rotors()

        return f"Encoded Message: {encoded_message} \nRotors initial positions: {spins} \nPlugs: {self.plugboard}\n"

    @staticmethod
    def decrypt(encoded_message, rotors, reflector, plugboard, rotors_positions):
        """Given a message and enigma's configurations, decrypt the message

        Args:
            encoded_message (String): Message to decrypt
            rotors (list): List of rotors objects
            reflector (Reflector): Reflector object
            plugboard (Plugboard): Plugboard object
            rotors_positions (List): List of rotors positions

        Returns:
            String: Decoded message
        """
        decoded_message = ""

        for i, rotor in enumerate(rotors):
            rotor.rotate(rotors_positions[i]%26)

        for letter in encoded_message:

            if not letter.isalpha():
                decoded_message += letter
                continue

            next_letter = letter

            next_letter = plugboard.return_letter(next_letter)

            rotors[0].rotate()

            if rotors[0].spins % 26 == 0:
                rotors[1].rotate()

            if rotors[1].spins % 26 == 0 and rotors[1].spins != 0:
                rotors[2].rotate()

            for rotor in rotors:
                next_letter = rotor.return_letter(next_letter)

            next_letter = reflector.return_reverse_letter(next_letter)

            for rotor in rotors[::-1]:
                next_letter = rotor.return_reverse_letter(next_letter)

            next_letter = plugboard.return_letter(next_letter)

            decoded_message += next_letter

        return f"Decoded Message: {decoded_message}"
