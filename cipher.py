##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, Brycen Williams
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
import string
import math
class Cipher:


    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Brycen Williams"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Affine Cipher"

    def text_to_numbers(self, text):
        return [(ord(char) - ord('a')) for char in text.upper() if char.isalpha()]

    def numbers_to_text(self, numbers):
        return ''.join([chr(num + ord('a')) for num in numbers])
    
    def create_char_map(self):
        char_set = string.ascii_letters + string.digits + string.punctuation
        char_map = {char: idx for idx, char in enumerate(char_set)}
        return char_map

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "https://www.geeksforgeeks.org/implementation-affine-cipher/ \nhttps://uregina.ca/~kozdron/Teaching/Cornell/135Summer06/Handouts/affine.pdf \n"

    def generate_affine_key(self, password, char_map):
        numeric_values = [char_map[char] for char in password] #Map password to numeric values
        
        a = sum(numeric_values) % 26
        b = 24
        
        # Ensure a is coprime with 26
        while math.gcd(a, 26) != 1:
            a = (a + 1) % 26
        
        return a, b


    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):

        # The encrypt pseudocode
        pc = "insert the encryption pseudocode\n"

        # The decrypt pseudocode
        pc += "insert the decryption pseudocode\n"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        char_map  = self.create_char_map()
        a, b = self.generate_affine_key(password, char_map)
        
        ciphertext = []
        for char in plaintext:
            if char.isalpha(): #Make sure char to be encoded is a letter and not a symbol.
                num = (a * (ord(char.lower()) - ord('a')) + b) % 26
                ciphertext.append(chr(num + ord('a')))
        
        return ''.join(ciphertext)

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        char_map = self.create_char_map()
        a, b = self.generate_affine_key(password, char_map)

        plaintext = []
        a_inv = pow(a, -1, 26)
        for char in ciphertext:
            num = (a_inv * ((ord(char) - ord('a')) - b)) % 26
            plaintext.append(chr(num + ord('a')))

        return ''.join(plaintext)