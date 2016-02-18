import collections

class Roman:
    mapping = \
        {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
    keys = [key for key in sorted(mapping.keys())]

    def convert(self, number):
        result = self.checkIfSimpleRomanNumeral(number)
        if result:
            return result

        return self.translateToRomanNumberal(number, "")

    def translateToRomanNumberal(self, number, romanNumberalSoFar):
        if number == 0:
            return romanNumberalSoFar
        elif number < 0:
            return "invalid input"
        else:
            key = self.maxSymbolLessThanNumber(number)
            return self.translateToRomanNumberal(number - key, romanNumberalSoFar + self.mapping[key])

    def maxSymbolLessThanNumber(self, number):
        return [key for key in self.keys if key <= number][-1]

    def checkIfSimpleRomanNumeral(self, number):
        return self.mapping.get(number, False)
