class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d ={}
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                if nums[i] in d:
                    val = d[nums[i]]
                    val+=1
                    d.update({nums[i]:val})
                else:
                    d.update({nums[i]:1})
        ans = []
        if len(d) == 0:
            return -1
        cnt = max(d.values())
        for x in d:
            if d[x] == cnt:
                ans.append(x)
        return min(ans)
        