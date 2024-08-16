class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 ways to solve this sum
        #method 1: count the ones and store the max of the count in a diff variable at last check the max again bcz the end of the list might be 1
        #method 2:create a list of the count of conseecutive ones then use max function to get the max value
        count=0
        #count_1_list=[]
        ans=0
        for x in nums:
            if x==1:
                count+=1
            else:
                #count_1_list.append(count)
                ans=max(ans,count)
                count=0
        #count_1_list.append(count)
        ans=max(ans,count)
        return ans #max(count_1_list)

        