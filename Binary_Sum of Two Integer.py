#+랑 -없이 두수 더하기

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         return sum([a,b])


# s=Solution()
# print(s.getSum(1,2))

#반칙인듯
#해설보니 실제 문제는 비트 연산 푸는거임
# ~ not, & and, | or, ^ xor
# >> << 비트를 좌측/우측으로 이동
# 그냥 블로그 글 << GOAT
# https://skillist.tistory.com/247
#       숫자
#  +    숫자
#  = --------
#      AND
#  +    XOR
#  = --------
#
#      ...
# 
#      AND
#  +     0
#  = -------- 
# 되면 AND가 답임(또는 반대로 AND가 0되면 XOR가 답)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        tempB = (a&b)<<1
        tempA = a^b

        if tempB == 0: return tempA
        elif tempA == 0: return tempB
        else: return self.getSum(tempA,tempB)

s=Solution()
print(s.getSum(5,7))

