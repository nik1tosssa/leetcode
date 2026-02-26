class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        step = 1
        while True:
            digits[len(digits) - step] += 1
            if digits[len(digits) - step] == 10:
                digits[len(digits) - step] = 0
                if len(digits) < 2:
                    digits.insert(0,0)

                step += 1
            else:
                break
        return digits

s = Solution()
print(s.plusOne([9]))
