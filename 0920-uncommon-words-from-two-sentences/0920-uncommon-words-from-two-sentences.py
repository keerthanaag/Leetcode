class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        sample = s1+" "+s2
        sample=sample.split(" ")
        print("sample ",sample)
        dic_count = {}
        for word in sample:
            if word not in dic_count:
                dic_count.update({word:1})
            else:
                val=dic_count[word]+1
                dic_count.update({word:val})
        print(dic_count)
        ans = []
        for x in dic_count:
            if dic_count[x]==1:
                ans.append(x)
        return ans
        