# https://leetcode.com/problems/two-sum

nums = [2,7,11,15]
target = 9


for i in range(0, nums.len()):
            for j in range(0,nums.len()):
                if nums[i] + nums[j]:
                    return [i,j]