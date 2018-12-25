import re


class RomanNumerals:

    @staticmethod
    def int_to_roman_string(integer):
        rn = RomanNumerals(integer=integer)
        return rn.to_roman_string()

    @staticmethod
    def roman_string_to_int(roman_string):
        rn = RomanNumerals(roman_string=roman_string)
        return rn.to_int()

    def __init__(self, integer=None, roman_string=None):
        self.integer = -1
        self.roman_string = ""
        self.is_valid = False

        if integer is not None:
            self.parse_from_int(integer)
        elif roman_string is not None:
            self.parse_from_roman_string(roman_string)

    def parse_from_int(self, integer):
        self.is_valid = False

        if integer < 1 or integer > 3999:
            raise ValueError("Invalid integer value: {}".format(integer))

        self.integer = integer
        self.roman_string = self.to_roman_string()
        self.is_valid = True

    def parse_from_roman_string(self, roman_string):
        self.is_valid = False

        if roman_string == "":
            raise ValueError("Empty string value")

        match = self._roman_string_regex_match(roman_string)

        if not match:
            raise ValueError("Invalid roman_string value: {}".format(roman_string))

        self.integer = self.to_int(match)
        self.roman_string = roman_string
        self.is_valid = True

    def to_roman_string(self):
        if not self.is_valid:
            # Break up the places using integer division and modulo
            ones = self.integer % 10
            tens = self.integer // 10 % 10
            hundreds = self.integer // 100 % 10
            thousands = self.integer // 1000 % 10
            self.roman_string = self._digit_to_roman(thousands, "M", "", "")
            self.roman_string += self._digit_to_roman(hundreds, "C", "D", "M")
            self.roman_string += self._digit_to_roman(tens, "X", "L", "C")
            self.roman_string += self._digit_to_roman(ones)

        return self.roman_string

    def to_int(self, match=None):
        if not self.is_valid:
            if match is None:
                match = self._roman_string_regex_match(self.roman_string)

            ones = match.group(4)
            tens = match.group(3)
            hundreds = match.group(2)
            thousands = match.group(1)

            self.integer = self._roman_to_digit(ones)
            self.integer += 10 * self._roman_to_digit(tens, "X", "L", "C")
            self.integer += 100 * self._roman_to_digit(hundreds, "C", "D", "M")
            self.integer += 1000 * self._roman_to_digit(thousands, "M", "", "")

        return self.integer

    def _digit_to_roman(self, digit, one="I", five="V", ten="X"):
        if digit < 0 or digit > 9:
            raise ValueError("Invalid digit value: {}".format(integer))

        switcher = {
            0: "",
            1: one,
            2: one + one,
            3: one + one + one,
            4: one + five,
            5: five,
            6: five + one,
            7: five + one + one,
            8: five + one + one + one,
            9: one + ten,
        }

        return switcher.get(digit)

    def _roman_to_digit(self, roman_digit, one="I", five="V", ten="X"):
        if roman_digit in ("", "M", "MM", "MMM"):
            return len(roman_digit)

        switcher = {
            "": 0,
            one: 1,
            one + one: 2,
            one + one + one: 3,
            one + five: 4,
            five: 5,
            five + one: 6,
            five + one + one: 7,
            five + one + one + one: 8,
            one + ten: 9,
        }

        return switcher.get(roman_digit)

    def _roman_string_regex_match(self, roman_string):
        # Break up the places using regex
        regex = re.compile(
            "(M{0,3})" +
            "(C{0,3}|CD|DC{0,3}|CM)" +
            "(X{0,3}|XL|LX{0,3}|XC)" +
            "(I{0,3}|IV|VI{0,3}|IX)"
        )

        return regex.fullmatch(roman_string)
