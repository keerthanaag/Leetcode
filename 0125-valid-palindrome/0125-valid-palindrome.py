class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=''
        for x in s:
            if x.isalnum() == True:
                temp+=x
        check=temp[::-1]
        if check == temp:
            return True
        else:
            False
        
        