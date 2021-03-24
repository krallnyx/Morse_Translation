class MorseEncoder:
    """Main class of the program, you should call run() on the object"""
    def __init__(self):
        """Simply creating an empty text and the morse dictionary"""
        self.dict = {'a': '. _', 'b': '_ . . .', 'c': '_ . . .', 'd': '_ . .', 'e': '.', 'f': '. . _ .', 'g': '- - .',
                     'h': '. . . .', 'i': '. .', 'j': '. _ _ _', 'k': '_ . _', 'l': '. _ . .', 'm': '_ _', 'n': '_ .',
                     'o': '_ _ _', 'p': '. _ _ .', 'q': '_ _ . _', 'r': '. _ .', 's': '. . .', 't': '_', 'u': '. . _',
                     'v': '. . . _', 'w': '. _ _', 'x': '_ . . _', 'y': '_ . _ _', 'z': '_ _ . .', '0': '_ _ _ _ _',
                     '1': '. _ _ _ _', '2': '. . _ _ _', '3': '. . . _ _', '4': '. . . . _', '5': '. . . . .',
                     '6': '_ . . . .', '7': '_ _ . . .', '8': '_ _ _ . .', '9': '_ _ _ _ .'}
        self.text = ''

    def run(self):
        """Main method, should be called on the class' children. Detects if the input is text to encode or
         morse to decode"""
        loop = True
        while loop:
            # We loop until there is actually an entry
            self.text = input("Please enter your text to translate or your morse code to decode.")
            try:
                first = self.text[0]
            except IndexError:
                # no text was given, we pass so we loop
                pass
            else:
                loop = False
        if first == '_' or first == '.':
            # entry is morse
            self.decode()
        else:
            # entry is not morse, assuming it's text to encode
            self.encode()

    def encode(self):
        """Takes self.text as an input and returns it's corresponding morse code"""
        result = ''
        for char in self.text:
            if char in self.dict:
                result += self.dict[char] + '   '
            elif char == ' ':
                result += '       '
        print("Your text in morse will be:")
        print(result)

    def decode(self):
        """Takes a morse code as self.text as an input and return its text translation"""
        result = ''
        list_of_words = self.text.split('       ')
        for words in list_of_words:
            list_of_chars = words.split('   ')
            for char in list_of_chars:
                if char in self.dict.values():
                    result += list(self.dict.keys())[list(self.dict.values()).index(char)]
            result += ' '
        print("Your decoded text is:")
        print(result[:-1])


if __name__ == '__main__':
    """Entry point of the app"""
    morse_encoder = MorseEncoder()
    morse_encoder.run()
