from fastapi import FastAPI


app = FastAPI()


def encode_message(message: str):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        ' ': ' '
    }
    message_list = list(message.upper())
    encoded_list = []
    for char in message_list:
        if char in morse_code_dict:
            encoded_list.append(morse_code_dict[char])
        else:
            pass
    encoded_message = ' '.join(encoded_list)
    return encoded_message


def decode_message(morse_code: str):
    other_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', ' ': ' '
    }
    morse_code_list = morse_code.split(' ')
    decoded_list = []
    for x in morse_code_list:
        if x in other_dict:
            decoded_list.append(other_dict[x])
        else:
            pass
    decoded_message = ' '.join(decoded_list)
    return decoded_message


@app.get("/")
async def home():
    return {"welcome": "to encode a message in morse code visit 'this_url/encode/your message', to decode type yuour "
                       "morse code with spaces in between each grouping of dots and dashes representing one alphabet "
                       "character"}


@app.get("/encode/{message}")
async def root(message: str):
    encoded_message = encode_message(message=message)
    return {"message": encoded_message}


@app.get("/decode/{morse_code}")
async def decode_morse(morse_code: str):
    decoded_message = decode_message(morse_code=morse_code)
    return {"message": decoded_message}