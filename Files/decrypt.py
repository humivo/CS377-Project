#!/usr/bin/env python3

#CS377 Homework
#
#To run file in linux "python3 decrypt.py"
#This program will look for all text file within the current directory and all sub-directories and decrypt it

import sys
import os
import re

#Function to encrypt data within text file
def decrypt(text, key):
    #How many shifts in the alphabet
    encryptData = ""

    #Open file and read the data in the file char by char
    #and encrypt the char one at a time and append it to string encryptData
    #Once we are finish encrypting we will write the encrypted data to the files
    #And replace the previous text
    file = open(text, "r")

    for line in file:
        for character in line:
            #Check if char is upper
            if(character.isupper()):
                encryptData += chr((ord(character) - key - 65) % 26 + 65)
            #Check if char is upper
            elif(character.islower()):
                encryptData += chr((ord(character) - key - 97) % 26 + 97)
            #Check if char is space
            elif(character == " "):
                encryptData += chr((ord(character)))
            #Check if char is newline
            elif(character == "\n"):
                encryptData += chr((ord(character)))
            #Check if char is tab
            elif(character == "\t"):
                encryptData += chr((ord(character)))
            #ASCII 33-64 (Symbols)
            elif((ord(character) >= 33 and ord(character) <= 64)):
                encryptData += chr((ord(character) - key - 33) % 32 + 33)
            #ASCII 91-96 (Symbols)
            elif((ord(character) >= 91 and ord(character) <= 96)):
                encryptData += chr((ord(character) - key - 91) % 6 + 91)
            #ASCII 123-126 (Symbols)
            elif((ord(character) >= 123 and ord(character) <= 126)):
                encryptData += chr((ord(character) - key - 123) % 4 + 123)



    file.close()

    #Write the decrypted data into the textfile
    encryptFile = open(text, "w")
    encryptFile.write(encryptData)
    encryptFile.close()

#main() Function
#Given a path and a key, look for all text files within the directory and sub-directory
#and preform decrypt() on the text files
def main(path, key):
    file = os.listdir(path)
    if len(file) > 0:
        for item in file:
            if item.endswith('.txt'):
                decrypt(path + "/" + item, key)
            elif os.path.isdir(path + "/" + item):
                main(path + "/" + item, key)



if __name__ == "__main__":
    main(os.getcwd(), int(sys.argv[1]))
