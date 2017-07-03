from imageencrypt import *

def main():
    choice = raw_input("Select One of the following\n> 1. Encrypt \n> 2. Decrypt\n>>> ")
    if choice == "1":
        filename = raw_input("Enter the name of file to be encrypted >> ")
        password = raw_input("Enter the password")
        encrypt(getKey(password), filename)
        print "Done!\n%s ==> %s"%(filename, filename+".enc")
    elif choice == "2":
        filename = raw_input("File to be decrypted > ")
        password = raw_input("Password: ")
        decrypt(getKey(password), filename)
        print "Done\n%s ==> %s"%(filename, filename[:-4])
    else:
        print "No option Selected"
 
if __name__ == "__main__":
    main()
