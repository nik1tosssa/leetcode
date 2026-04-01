class Solution:
    """
    Input: a = "1010", b = "1011"
    Output: "10101"
    """
    def equalize_lens(self,n,x):
        for _ in range(abs(len(n) - len(x))):
            if len(n) > len(x):
                x.append("0")
            else:
                n.append("0")


    def addBinary(self, a: str, b: str) -> str:
        list_a = list(a)[::-1]
        list_b = list(b)[::-1]
        result = []
        self.equalize_lens(list_a,list_b)
        extra = 0
        for i in range(max(len(list_a),len(list_b))):
            digit = int(list_a[i]) + int(list_b[i]) + extra

            if digit == 2:
                result.append("0")
                extra = 1
            elif digit == 3:
                result.append("1")
                extra = 1
            else:
                result.append(str(digit))
                extra = 0
        result.append(str(extra))
        result = result[::-1]
        if int(result[0]) == 0:
            del result[0]

        return "".join(result)




sol = Solution()
print(sol.addBinary("11","1"))