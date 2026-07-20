class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            res |= (curr_bit << i)
        if res >= (1 << 31):
            res -= (1 << 32)
        return res