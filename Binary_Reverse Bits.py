# class Solution:
#     def reverseBits(self, n: int) -> int:
#         binary= str(bin(n))[2::].zfill(32)
#         return int(binary[::-1],2)

#반칙인듯


class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for i in range(32):
            bit =  (n>>i)&1
            ans |= (bit << (31-i))
        return ans
