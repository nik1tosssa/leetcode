class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


a = int(input())
s = Solution()
print(s.isPalindrome(a))