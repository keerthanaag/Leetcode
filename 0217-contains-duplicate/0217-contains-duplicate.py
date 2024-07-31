class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #in the 1st code I counted the no of duplicates which resulted in exceeded time limit
        #for i in nums:
        #    if(nums.count(i)>1):
        #        return True
        #return False
        #in the second code I converted the list to set cz set doesn't contain duplicates.when their length aren't equal thn it contained duplicates
        len_list=len(nums)
        convert_set=set(nums)
        len_set=len(convert_set)
        if(len_set==len_list):
            return False
        else:
            return True

        