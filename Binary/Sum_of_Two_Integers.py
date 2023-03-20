# Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        kMax = 2000

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a < kMax else ~(a ^ mask)