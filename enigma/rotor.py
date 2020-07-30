# -*- coding: utf-8 -*-
"""
Complementary code for enigma.py
"""
import string

class Rotor(object):
    """Simulates a real mechanical rotor from Enigma Machine
    """
    def __init__(self, wiring=None, name=None, model=None, date=None):
        """Initializing Rotor object

        Args:
            wiring (string): Rotor's dictionary
            name (string): Rotor's name
            model (string): Rotor's model
            date (string): Date when Rotor was created
        """
        self.wiring = wiring
        self.name = name
        self.model = model
        self.date = date
        self.dictionary = dict(zip(string.ascii_uppercase, self.wiring.upper()))
        self.original_dictionary = self.dictionary.copy()
        self.spins = 0

    def __str__(self):
        """Fancy print
        """
        return f"Name: {self.name}\nModel: {self.model}\nDate: {self.date}\nWiring: {self.wiring}"

    def return_letter(self, letter):
        """Return encoded letter from rotor dictionary

        Args:
            letter (String): Letter to encode

        Returns:
            String: Encoded Letter
        """
        return self.dictionary[letter]

    def return_reverse_letter(self, letter):
        """Return encoded letter from inverse rotor dictionary

        Args:
            letter (String): Letter to encode

        Returns:
            String: Encoded Letter
        """
        new_dict = dict([(value, key) for key, value in self.dictionary.items()])
        return new_dict[letter]

    def rotate(self, n=1):
        """Rotate n letter from dictionary

        Args:
            n (int, optional): Number of letters to rotate. Defaults to 1.
        """
        dic_keys = list(self.dictionary.keys())
        dic_values = list(self.dictionary.values())

        dic_values = dic_values[-n:] + dic_values[:-n]

        for i, each in enumerate(dic_keys):
            self.dictionary[each] = dic_values[i]

        self.spins += n

    def reset(self):
        """Reset initial rotor configurations
        """
        self.dictionary = self.original_dictionary.copy()
        self.spins = 0

class Reflector(object):
    """Simulates the mechanical reflector from Enigma Machine
    """
    def __init__(self, wiring=None, name=None, model=None, date=None):
        """Initialize Reflector object

        Args:
            wiring (string): Reflector's dictionary
            name (string): Reflector's name
            model (string): Reflector's model
            date (string): Date when Reflector was created
        """
        self.wiring = wiring
        self.name = name
        self.model = model
        self.date = date
        self.dictionary = dict(zip(string.ascii_uppercase, self.wiring.upper()))

    def __str__(self):
        """Fancy print
        """
        return f"Name: {self.name}\nModel: {self.model}\nDate: {self.date}\nWiring: {self.wiring}"

    def return_letter(self, letter):
        """Return encoded letter from rotor dictionary

        Args:
            letter (String): Letter to encode

        Returns:
            String: Encoded Letter
        """
        return self.dictionary[letter]

    def return_reverse_letter(self, letter):
        """Return encoded letter from inverse rotor dictionary

        Args:
            letter (String): Letter to encode

        Returns:
            String: Encoded Letter
        """
        new_dict = dict([(value, key) for key, value in self.dictionary.items()])
        return new_dict[letter]

class Plugboard(object):
    """Simulates the mechanical plugboard from Enigma Machine
    """
    def __init__(self, plugs=""):
        """Initialize Plugboard object

        Args:
            plugs (string): Plugs connected
        """
        self.plugs = dict(zip(string.ascii_uppercase, string.ascii_uppercase))
        self.string_plugs = plugs

        alpha_plugs = {k:i for k, i in plugs.split()}
        alpha_plugs_inverse = {v: k for k, v in alpha_plugs.items()}

        for each in alpha_plugs:
            self.plugs[each] = alpha_plugs[each]
        for each in alpha_plugs_inverse:
            self.plugs[each] = alpha_plugs_inverse[each]

    def __str__(self):
        """Fancy print
        """
        return self.string_plugs

    def return_letter(self, letter):
        """Return encoded letter from rotor dictionary

        Args:
            letter (String): Letter to encode

        Returns:
            String: Encoded Letter
        """
        return self.plugs[letter]


# Types of Rotors
# Fonts: Wikipedia and @cedricbonhomme

# 1924 Rotors
ROTOR_IC = Rotor(wiring="DMTWSILRUYQNKFEJCAZBPGXOHV", name="IC", model="Commercial Enigma A, B", date="1924")
ROTOR_IIC = Rotor(wiring="HQZGPJTMOBLNCIFDYAWVEUSRKX", name="IIC", model="Commercial Enigma A, B", date="1924")
ROTOR_IIIC = Rotor(wiring="UQNTLSZFMREHDPXKIBVYGJCWOA", name="IIIC", model="Commercial Enigma A, B", date="1924")

# German Railway Rotors
ROTOR_GR_I = Rotor(wiring="JGDQOXUSCAMIFRVTPNEWKBLZYH", name="I", model="German Railway (Rocket)", date="7 February 1941")
ROTOR_GR_II = Rotor(wiring="NTZPSFBOKMWRCJDIVLAEYUXHGQ", name="II", model="German Railway (Rocket)", date="7 February 1941")
ROTOR_GR_III = Rotor(wiring="JVIUBHTCDYAKEQZPOSGXNRMWFL", name="III", model="German Railway (Rocket)", date="7 February 1941")
ROTOR_GR_UKW = Reflector(wiring="QYHOGNECVPUZTFDJAXWMKISRBL", name="UTKW", model="German Railway (Rocket)", date="7 February 1941")
ROTOR_GR_ETW = Rotor(wiring="QWERTZUIOASDFGHJKPYXCVBNML", name="ETW", model="German Railway (Rocket)", date="7 February 1941")

# Swiss K Rotors
ROTOR_I_K = Rotor(wiring="PEZUOHXSCVFMTBGLRINQJWAYDK", name="I-K", model="Swiss K", date="February 1939")
ROTOR_II_K = Rotor(wiring="ZOUESYDKFWPCIQXHMVBLGNJRAT", name="II-K", model="Swiss K", date="February 1939")
ROTOR_III_K = Rotor(wiring="EHRVXGAOBQUSIMZFLYNWKTPDJC", name="III-K", model="Swiss K", date="February 1939")
ROTOR_UKW_K = Reflector(wiring="IMETCGFRAYSQBZXWLHKDVUPOJN", name="UKW-K", model="Swiss K", date="February 1939")
ROTOR_ETW_K = Rotor(wiring="QWERTZUIOASDFGHJKPYXCVBNML", name="ETW-K", model="Swiss K", date="February 1939")

# Enigma
ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", name="I", model="Enigma 1", date="1930")
ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", name="II", model="Enigma 1", date="1930")
ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", name="III", model="Enigma 1", date="1930")
ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", name="IV", model="M3 Army", date="December 1938")
ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", name="V", model="M3 Army", date="December 1938")
ROTOR_VI = Rotor(wiring="JPGVOUMFYQBENHZRDKASXLICTW", name="VI", model="M3 & M4 Naval(February 1942)", date="1939")
ROTOR_VII = Rotor(wiring="NZJHGRCXMYSWBOUFAIVLPEKQDT", name="VII", model="M3 & M4 Naval(February 1942)", date="1939")
ROTOR_VIII = Rotor(wiring="FKQHTLXOCBJSPDZRAMEWNIUYGV", name="VIII", model="M3 & M4 Naval(February 1942)", date="1939")

# misc & reflectors
ROTOR_Beta = Rotor(wiring="LEYJVCNIXWPBQMDRTAKZGFUHOS", name="Beta", model="M4 R2", date="Spring 1941")
ROTOR_Gamma = Rotor(wiring="FSOKANUERHMBTIYCWLQPZXVGJD", name="Gamma", model="M4 R2", date="Spring 1941")
ROTOR_Reflector_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD", name="Reflector A")
ROTOR_Reflector_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT", name="Reflector B")
ROTOR_Reflector_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL", name="Reflector C")
ROTOR_Reflector_B_Thin = Reflector(wiring="ENKQAUYWJICOPBLMDXZVFTHRGS", name="Reflector_B_Thin", model="M4 R1 (M3 + Thin)", date="1940")
ROTOR_Reflector_C_Thin = Reflector(wiring="RDOBJNTKVEHMLFCWZAXGYIPSUQ", name="Reflector_C_Thin", model="M4 R1 (M3 + Thin)", date="1940")
ROTOR_ETW = Rotor(wiring="ABCDEFGHIJKLMNOPQRSTUVWXYZ", name="ETW", model="Enigma 1")
