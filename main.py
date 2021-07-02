import winsound # for accessing windows system sounds
from time import sleep

# Create list of characters a-z and 0-9
chars = [chr(i) for i in range(ord('a'), ord('z')+1)]
nums = [i for i in range(1, 10)]
for num in nums:
    chars.append(str(num))
chars.append('0')

# Morse Code list:
m_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
          '....', '..', '.---', '-.-', '.-..', '--', '-.',
          '---', '.--.', '--.-', '.-.', '...', '-', '..-',
          '...-', '.--', '-..-', '-.--', '--..', '.----', '..---',
          '...--', '....-', '.....', '-....', '--...', '---..',
          '----.', '-----']

# Use chars list to generate morse code dictionary:
morse_dict = {chars[i]:m_code[i] for i in range(len(chars))}

print('************ -- MORSE CODE CONVERTER -- ************')

while True:
# Get user input
    string_to_convert = input('Enter your text to convert:\n')

    # Convert string to morse code
    result = ''
    try:
        for letter in string_to_convert:
            if letter == ' ':
                result += ' / '
            else:
                result += f'{morse_dict[letter.lower()]} '
        print(result)
        # convert result to windows sounds
        for character in result:
            if character == ' ':
                sleep(0.4)
            if character == '-':
                winsound.Beep(2000, 250)
            if character == '.':
                winsound.Beep(2000, 80)
            sleep(0.05)
    except KeyError:
        print('Please only use characters a-z and number 0-9 (no special characters)')

