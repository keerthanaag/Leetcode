class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        st=set({})
        lst=[]
        for x in nums:
            if x not in st:
                st.add(x)
            else:
                lst.append(x)
        return lst
        
        
        