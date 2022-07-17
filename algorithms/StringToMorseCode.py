alpha = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
         'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

print("Select option (1 or 2): ")
print("1. Convert text to morse code")
print("2. Convert morse code to text")
option = int(input())
if option == 1:
	# text to morse code
    text = input('Enter a text: ')
    morse = ""
    for c in text:
        morse += alpha[c] + " "
    print(morse)
elif option == 2:
    # morse code to text.
    morse_txt = input("Enter morse code: ")
    codes = morse_txt.split()
    new_text = ""
    for code in codes:
        for k, v in alpha.items():
            if v == code:
                new_text += k
    print(new_text)
else:
    print("You have selected wrong option.")
