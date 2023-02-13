#O(1) extra space, O(n) time complexity
class Solution:
    def missingNumber(self, nums) -> int:
        length =  len(nums) #O(1) time
        sum = (length * (length+1)) //2 #O(1) space
        for i in nums: #O(N) time
            sum -= i
        return sum