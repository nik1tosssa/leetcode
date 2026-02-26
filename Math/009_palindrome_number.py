class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False


a = int(input())
s = Solution()
print(s.isPalindrome(a))