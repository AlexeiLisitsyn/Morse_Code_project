#  A text-based Python program to convert Strings into Morse Code.
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---','K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---','3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '/': '-..-.','.': '.-.-.-', '-': '-....-', '+': '.-.-.', '=': '-...-', ':': '---...', '$': '...-..-',
    '?': '..--..', '@': '.--.-.', '&': '.-...', '"': '.-..-.', "'": ".----.", '!': '--...-', '(': '-.--.-',
    ')': '-.--.-'}

morse_code_reverse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-..-.': '/', '.-.-.-': '.', '-....-': '-', '.-.-.': '+', '-...-': '=', '---...': ':', '...-..-': '$',
    '..--..': '?', '.--.-.': '@', '.-...': '&', '.-..-.': '"', ".----.": "'", '--...-': '!', '-.--.-': ')', '': ' '}

app_on = True

# Translate text into Morse Code.
def intoCode(user_text):
    for char in user_text:
        if char in morse_code:
            user_output.append(morse_code[char] + ' ')
        elif char == ' ':
            user_output.append('/')
        else:
            print(f'Error in input. Cannot translate the highlighted character: {char}')


# Translate text from Morse Code.
def fromCode(user_code):
    user_list_code = []
    for item in user_code.split():
        user_list_code.extend(item.split('/'))
    for code in user_list_code:
        if code in morse_code_reverse:
            user_output.append(morse_code_reverse[code])
        else:
            print(f'Error in input. Cannot translate the highlighted character: {code}')


while app_on:
    user_output = []
    user_input = input("In order to translate text into Morse Code type '1'."
                       "\nIn order to translate Morse Code into text type '2'."
                       "\nTo quit from app type any other key.\n")
    if user_input == '1':
        user_text = input('In order to encrypt your message type it below: \n').upper()
        intoCode(user_text)
        print(''.join(user_output))
    elif user_input == '2':
        user_code = input('Type your Morse Code below separating letters by spaces and words by "/": \n')
        fromCode(user_code)
        print(''.join(user_output))
    else:
        app_on = False

"""
Write down how you approached the project. What was hard, what was easy?

'The most challenging part was about "fromCode() func" with separating two delimiters: forward slash and whitespace. 
It was a little confusing because method 'split()' has only one parameter. So I had to find a way to solve the problem.'
"""