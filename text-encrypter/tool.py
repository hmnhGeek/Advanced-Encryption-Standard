from txtencrypter import *

def main():

    choice = input("\n\nWhat do you want to perform?\n1. Encrypt\n2. Decrypt\n3. Read plaintext\n4. Read ciphertext\n5. Exit\n> ")

    if choice == 1:
        text = raw_input("> Enter text: ")
        key = raw_input("> Enter a key: ")

        encr = encrypt(text, key)

        save = raw_input('\n> Save? ').upper()

        if save == 'Y':
            destination = raw_input("\n> Saving location: ")
            filename = raw_input("> Filename: ")

            if destination[-1] != '/':
                destination += '/'

            with open(destination+filename, 'w') as outfile:
                outfile.write(encr)

            print encr

        else:
            print encr

    elif choice == 2:
        text = raw_input("> Enter ciphertext: ")
        key = raw_input("> Enter key: ")

        decr = decrypt(text, key)

        save = raw_input('\n> Save? ').upper()

        if save == 'Y':
            destination = raw_input("\n> Saving location: ")
            filename = raw_input("> Filename: ")

            if destination[-1] != '/':
                destination += '/'

            with open(destination+filename, 'w') as outfile:
                outfile.write(decr)

            print decr

        else:
            print decr

    elif choice == 3:
        fi = raw_input("> Enter file address: ")
        key = raw_input("> Enter key: ")

        with open(fi, 'r') as inputfile:
            data = inputfile.read()

        encr = encrypt(data, key)

        save = raw_input('\n> Save? ').upper()

        if save == 'Y':
            destination = raw_input("\n> Saving location: ")
            filename = raw_input("> Filename: ")

            if destination[-1] != '/':
                destination += '/'

            with open(destination+filename, 'w') as outfile:
                outfile.write(encr)

            print encr

        else:
            print encr

    elif choice == 4:
        fi = raw_input("> Enter file address: ")
        key = raw_input("> Enter key: ")

        with open(fi, 'r') as inputfile:
            data = inputfile.read()

        decr = decrypt(data, key)

        save = raw_input('\n> Save? ').upper()

        if save == 'Y':
            destination = raw_input("\n> Saving location: ")
            filename = raw_input("> Filename: ")

            if destination[-1] != '/':
                destination += '/'

            with open(destination+filename, 'w') as outfile:
                outfile.write(decr)

            print decr

        else:
            print decr

    elif choice == 5:
        exec 'exit()'

    else:
        print "Invalid Choice!!"

    main()

main()
