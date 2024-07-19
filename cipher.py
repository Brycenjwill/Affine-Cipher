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
        return [(ord(char) - ord('a')) for char in text if char.isalpha()]

    def numbers_to_text(self, numbers):
        return ''.join([chr(num + ord('a')) for num in numbers])
    
    def create_char_map(self):
        char_set = string.ascii_letters + string.digits + string.punctuation + " "
        char_map = {char: idx for idx, char in enumerate(char_set)}
        print(char_map)
        return char_map

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "https://www.geeksforgeeks.org/implementation-affine-cipher/ \nhttps://uregina.ca/~kozdron/Teaching/Cornell/135Summer06/Handouts/affine.pdf \n"

    def generate_affine_key(self, password, char_map, m):
        numeric_values = [char_map[char] for char in password] #Map password to numeric values
        
        a = sum(numeric_values) % m
        b = char_map[password[0]] % m


        
        # Ensure a is coprime with m
        while math.gcd(a, m) != 1:
            a = (a + 1) % m
        
        return a, b


    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):

        # The encrypt pseudocode
        pc = "\nEncryption: \nFirst, we map the password to numeric values. Then, we generate a by finding the modulus of this numeric value and 26. We do this by creating a character map, which maps all utf characters from 1 to 93 to their numeric values. We find b by doing the first letter of the password modulus 26. If a is not coprime with 26, then we will find the next highest number that is coprime with 26. We will then convert the plaintext into corresponding numeric values.  Then, to encrypt each character in the numeric version of the plaintext, we will use the equation E(x) = (ax + b)*mod(26) where x is the numeric value of the character. Once all characters in the plaintext are encrypted as numbers, we convert them back to letters. \n"

        # The decrypt pseudocode
        pc += "\nDecryption: \nFirst, we map the password to numeric values. We do this by using the same character map as before, which maps all utf characters from 1 to 93 to their numeric values. Then, we generate a by finding the modulus of this numeric value and 26. We find b by doing the first letter of the password modulus 26. If a is not coprime with 26, then we will find the next highest number that is coprime with 26. Then, we we set a_inverse to a^-1 modulus 26. We will then convert the ciphertext into corresponding numeric values. Then, to decrypt each character in the numeric version of the ciphertext, we will use the equation D(x) = a^-1*(x-b)*mod(26) where x is the numeric value of the character, and a^-1 is represented by a_inverse. Once all characters in the plaintext are decrypted as numbers, we convert them back to letters. \n"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        char_map  = self.create_char_map()
        a, b = self.generate_affine_key(password, char_map, 26)
        num_a, num_b = self.generate_affine_key(password, char_map, 10)
        
        ciphertext = []
        for char in plaintext:
            if char.isalpha(): #Make sure char to be encoded is a letter and not a symbol.
                num = (a * (ord(char.lower()) - ord('a')) + b) % 26
                ciphertext.append(chr(num + ord('a')))
            else:
                if char.isnumeric():
                    num = (num_a * ((ord(char)) - ord('0')) + num_b) % 10
                    ciphertext.append(chr(num + ord('0')))
        
        return ''.join(ciphertext)

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        char_map = self.create_char_map()
        a, b = self.generate_affine_key(password, char_map, 26)
        num_a, num_b = self.generate_affine_key(password, char_map, 10)
        
        plaintext = []
        a_inv = pow(a, -1, 26)
        num_a_inv = pow(num_a, -1, 10)

        for char in ciphertext:
            if char.isalpha():
                num = (a_inv * ((ord(char) - ord('a')) - b)) % 26
                plaintext.append(chr(num + ord('a')))
            else:
                if char.isnumeric():
                    num = (num_a_inv * ((ord(char)) - ord('0') - num_b)) % 10
                    plaintext.append((str(num)))

        return ''.join(plaintext)