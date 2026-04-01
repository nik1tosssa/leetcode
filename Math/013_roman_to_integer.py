class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        roman_number = s[::-1]
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        #"XIV" - > "VIX" - 14

        while len(roman_number) > 0:
            if len(roman_number) > 1:
                if roman_dict.get(roman_number[0]) <= roman_dict.get(roman_number[1]):
                    n += roman_dict.get(roman_number[0])
                    roman_number = roman_number[1:]
                else:
                    n += roman_dict.get(roman_number[0]) - roman_dict.get(roman_number[1])
                    roman_number = roman_number[2:]
            else:
                n += roman_dict.get(roman_number[0])
                roman_number = roman_number[1:]
        return n

sol = Solution()

print(sol.romanToInt('XIV'))
