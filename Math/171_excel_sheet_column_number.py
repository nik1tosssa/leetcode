class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 1
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        column_title = columnTitle[::-1]
        for i in range(len(column_title)):
            c = column_title[i]
            ind = alphabet.find(c) + 1
            addable = ind * (26 ** i)
            number += addable
        return number - 1

sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))
