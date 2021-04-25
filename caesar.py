from alphabets import alphabetrus, alphabeteng

class Caesar:
    def encrypt(self, text, num):
        newtext = ''
        for symbol in text:
            if symbol.lower() not in alphabetrus:
                newtext += symbol
                continue
            isupper = symbol.isupper()
            if isupper:
                symbol = symbol.lower()
            symbol = alphabetrus[(alphabetrus.index(symbol) + int(num)) % 33]
            if isupper:
                symbol = symbol.upper()
            newtext += symbol
        return newtext
    
    def decrypt(self, code, num):
        newtext = ''
        for symbol in code:
            if symbol.lower() not in alphabetrus:
                newtext += symbol
                continue
            isupper = symbol.isupper()
            if isupper:
                symbol = symbol.lower()
            symbol = alphabetrus[(alphabetrus.index(symbol) - int(num)) % 33]
            if isupper:
                symbol = symbol.upper()
            newtext += symbol
        return newtext