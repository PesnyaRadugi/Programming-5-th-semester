class Encoder:
    def __init__(self, alphabet, encrypt_alphabet):
        self.alphabet = alphabet
        self.encrypt_alphabet = encrypt_alphabet
        self.encrypt_keys = dict(zip(list(alphabet), list(encrypt_alphabet)))
        self.decrypt_keys = dict(zip(list(encrypt_alphabet), list(alphabet)))

    def Encrypt(self, text):
        lst_of_words = text.split(' ')
        result = ''
        for word in lst_of_words:
            for i in word:
                result += self.encrypt_keys[i]
            result += ' '
        return result.strip()
    
    def Decrypt(self, text):
        lst_of_words = text.split(' ')
        result = ''
        for word in lst_of_words:
            for i in word:
                result += self.decrypt_keys[i]
            result += ' '
        return result.strip()


def Initialize():
    while True:
        usr_input = input('> Would you like to use your own encryption alphabet ? y/n \n')
        if usr_input.lower() == 'y':
            custom_alphabet = input('Enter your own encryption alphabet: \n')
            if len(custom_alphabet) < 26:
                print('> Length of your alphabet is less than actual alphabet (26 symbols), try again')
            else:
                return Encoder('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', custom_alphabet + custom_alphabet.upper())
        elif usr_input.lower() == 'n':
            return Encoder('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA')
        else:
            print('Try again.')
            continue

def Navigate_menu(encoder : Encoder):
    print('''>>> Your next move ?
            encode = Encode a message with current alphabet
            decode = Decode a message with current alphabet
            alphabet = See alphabet and encryption alphabet
            quit = Shut down
            help = Show list of commands
        ''')
    while True:
        usr_input = input('>')
        if usr_input.lower() == 'encode':
            print(encoder.Encrypt(input('> Enter text to encode\n')))
        elif usr_input.lower() == 'decode':
            print(encoder.Decrypt(input('> Enter text to decrypt\n')))
        elif usr_input.lower() == 'alphabet':
            print('Current alphabet:\n',
                    encoder.alphabet, encoder.encrypt_alphabet
            )
        elif usr_input.lower() == 'quit':
            print('Shutting down....')
            break
        elif usr_input.lower() == 'help':
            print(
                '''
                encode = Encode a message with current alphabet
                decode = Decode a message with current alphabet
                alphabet = See alphabet and encryption alphabet
                quit = Shut down
                help = Show list of commands'''
            )
        else:
            print('>>> Invalid command, try again')
            continue
        
           
def Main():
    print('>>> Welcome to super-secret encryption programm <<<')
    test = Initialize()
    print('Alphabet succesfully created\n',
            'Current alphabet:\n',
            test.alphabet, test.encrypt_alphabet
    )
    Navigate_menu(test)

if __name__ == '__main__':
    Main()