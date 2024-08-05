class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # lst=[]
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         lst.append(i)
        # return lst
        num=set(nums)
        temp=set()
        for i in range(1,len(nums)+1):
            temp.add(i)#adds an element to the set
        return list(temp-num)# subracts the elements present in nums from temp to get the disaapearing elements

        