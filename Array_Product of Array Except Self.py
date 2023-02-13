# O(N)에 동작하면서 나눗셈을 사용하지 않도록 풀어야됨
# 길이 10^5이고 각각의 숫자가 -30~30, 곱은 32bit integer 범위내
# O(1) extra space complexity로 풀수도 있다고함 >> 어케함???
# i까지의 정방향, 역방향 곱을 미리 구해놓고 i-1까지는 정방향 곱 * i+1부터는 역방향 곱의 리스트에서 값 가져와서 곱해서 냄

class Solution:

    def productExceptSelf(self, nums):
        forward = 1
        forlist = []
        backward = 1
        backlist = []
        outlist = []
        n = len(nums)
        for i in nums:
            forward = forward * i
            forlist.append(forward)
        for i in reversed(nums):
            backward = backward * i
            backlist.append(backward)
        for i in range(n):
            if i==0:
                outlist.append(backlist[n-i-2])
            elif i==n-1:
                outlist.append(forlist[i-1])
            else:
                outlist.append(forlist[i-1] * backlist[n-i-2])
        return outlist

        

# s=Solution()
# print(s.productExceptSelf([1,2,3,4]))
# print(s.productExceptSelf([-1,1,0,-3,3]))
