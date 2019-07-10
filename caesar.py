#pylint: disable=W0603,C0200
"""Caesar's encryptie algoritme toepassen"""
import getopt
import sys

FILE = "caesar.txt"

def main():
    """main functie"""
    initialize()
    ciphertext = read_file()
    decrypt(ciphertext)

def initialize():
    """opties inlezen en alles instellen"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError:
        print_help()

    if args:    # er zijn extra (onnodige argumenten) toegevoegd
        print_help()
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-f", "--file"):
            global FILE
            FILE = arg

def print_help():
    """help voor de functie uitprinten"""
    print("python caesar.py [-h|--help] [-f|--file filename]")

def read_file():
    """Bestand met cipher tekst inlezen"""
    with open(FILE) as cipher:
        return cipher.read().lower()

def decrypt(ciphertext):
    """Functie waarin telkens een poging wordt gedaan om de tekst de decrypteren"""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    decryptions = {}

    for shift in range(26):
        dic = {}
        for i in range(0, len(alphabet)):
            dic[alphabet[i]] = alphabet[(i + shift)%len(alphabet)]
        decrypted_text = ""
        for letter in ciphertext:
            if letter in dic:
                letter = dic[letter]
            decrypted_text += letter
        decryptions[str(shift)] = decrypted_text
    print_decryptions(decryptions)

def print_decryptions(decryptions):
    """Mogelijke ontcijferingen printen"""
    with open("decryptions.txt", "w") as decryptions_file:
        for shift, decryption in decryptions.items():
            line = "Shift: {shift}\nDecryption:\n{decryption}\n\n".format(shift=shift,
                                                                          decryption=decryption)
            decryptions_file.write(line)
if __name__ == "__main__":
    main()
