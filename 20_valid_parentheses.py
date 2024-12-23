class Solution:
    def isValid(self, s: str) -> bool:
        while (len(s) > 0):
            if ("()" in s):
                s = s.replace("()","")
            elif ("{}" in s):
                s = s.replace("{}","")
            elif ("[]" in s):
                s = s.replace("[]","")
            elif (len(s) > 0): return False
        return True
    
parentheses = ""
parentheses = input()
solution = Solution()
print(solution.isValid(parentheses))