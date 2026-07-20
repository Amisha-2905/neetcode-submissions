class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        stack = [0, 1]
        idx = 2
        curr_p = 0
        len_s = 2

        while idx <= n:
            if curr_p == len_s:
                len_s <<= 1
                curr_p = 0

            stack.append(stack[curr_p] + 1)
            curr_p += 1
            idx += 1

        return stack