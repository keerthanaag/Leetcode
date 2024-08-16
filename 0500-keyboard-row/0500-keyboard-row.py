class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        lst1=["q","w","e","r","t","y","u","i","o","p"]
        lst2=["a","s","d","f","g","h","j","k","l"]
        lst3=["z","x","c","v","b","n","m"]
        for i in range(0,len(words)):
            temp=words[i].lower()
            flag=0
            wor=len(temp)
            if temp[0] in lst1:
                for j in range(1,wor):
                    if temp[j] not in lst1:
                        flag=1
                        break
                if flag ==0:
                    ans.append(words[i])
            if temp[0] in lst2:
                for j in range(1,wor):
                    if temp[j] not in lst2:
                        flag=1
                        break
                if flag ==0:
                    ans.append(words[i])
            else:
                for j in range(1,wor):
                    if temp[j] not in lst3:
                        flag=1
                        break
                if flag ==0:
                    ans.append(words[i])
        return ans
                


        