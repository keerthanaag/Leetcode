class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums2)
        lst=[]
        for i in nums1:
            position=nums2.index(i)
            if max(nums2)==i or (n-1)==position:
                lst.append(-1)
            else:
                if nums2[position+1]>i:
                    lst.append(nums2[position+1])
                else:
                    flag=0
                    for j in range(position+1,n):
                        if nums2[j]>i:
                            lst.append(nums2[j])
                            flag=1
                            break
                    if flag==0:
                        lst.append(-1)
        return lst


        