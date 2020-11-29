# CS377-Project

Firebase Account info
Link: https://cs377-project-fall-20.firebaseio.com/
----------------------------------
Email: cs377projecttest@gmail.com
PW: Test1234!
----------------------------------

How it works:
To setup the attack scenario, please make sure a copy of the cs377-project-creds.json is in the /Files/ directory.  After this is done, to run the attack, just run the program attack.sh by typing into the command line './attack.sh'.  This should run the attack on the current directory and recursively encrypt the files.  Also, it will store the key for decryption in the firebase account above.  The attack program should also delete the cs377-project-creds.json to replicate the deletion of auth and force the user to email the atatckers for the key in an imaginary scenario.  However, of course, for testing purposes we have a backup of the creds that we can just copy back in the root directory.  To decrypt the files, you must get the key from the the firebase database that correlates to the victim id.  After you have this key, you can run the decrypt file by typing 'python3 decrypt.py {key}'.  This should revert the txt files back to normal.  