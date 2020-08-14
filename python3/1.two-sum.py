class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in dic:
                return [i, dic[b]]
            dic[nums[i]] = i
        return None

if __name__=='__main__':
    solu = Solution()
    print(solu.twoSum([2, 11, 7, 15], 9))
