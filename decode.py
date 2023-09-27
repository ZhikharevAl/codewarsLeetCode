import re;

message = input().strip()

# -- ваш код начинается тут
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', ' ': ' '
}

def decode(message):
    words = message.strip().split('   ')
    result = []

    for word in words:
        letters = word.split()  
        decoded_word = ''.join([MORSE_CODE[letter] for letter in letters])
        result.append(decoded_word)

    return ' '.join(result)

result = decode(message)                   
# -- ваш код заканчивается тут

print(result)
