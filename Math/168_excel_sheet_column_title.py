class Solution:
    def convertToTitle(self, column_number: int) -> str:
        alphabet = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
            8:"I",
            9:"J",
            10:"K",
            11:"L",
            12:"M",
            13:"N",
            14:"O",
            15:"P",
            16:"Q",
            17:"R",
            18:"S",
            19:"T",
            20:"U",
            21:"V",
            22:"W",
            23:"X",
            24:"Y",
            25:"Z",
        }
        title = ''
        while column_number > 0:
            column_number -= 1
            i = column_number % 26
            c = alphabet.get(i)
            title += c
            column_number = column_number // 26

        return title[::-1]

sol = Solution()
print(sol.convertToTitle(24))