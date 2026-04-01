class Solution:
    """
    #fast solution with lists
    def plusOne(self, digits: list[int]) -> list[int]:
        step = 1
        while True:
            digits[len(digits) - step] += 1
            if digits[len(digits) - step] == 10:
                digits[len(digits) - step] = 0
                if len(digits) - step == 0:
                    digits.insert(0,0)
                step += 1
            else:
                break
        if digits[0] == 0:
            del digits[0]
        return digits
    """

    def plusOne(self, digits: list[int]) -> list[int]:
        str_number = ""
        for i in digits:
            str_number += str(i)
        number = int(str_number) + 1
        str_number = str(number)
        digits = []
        for s in str_number:
            digits.append(int(s))
        return digits

s = Solution()
print(s.plusOne([9,9,9]))
