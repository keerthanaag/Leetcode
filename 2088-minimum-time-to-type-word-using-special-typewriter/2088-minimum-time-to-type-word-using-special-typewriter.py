class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        ans = 0
        for i,x in enumerate(word):
            #print(x)
            if i != 0:
                prev = word[i-1]
            if ord(prev) <= ord(x):
                nav_clock = ord(x) - ord(prev)
            else:
                nav_clock = ord('z') - ord(prev)+ord(x) - ord('a')+1
            if ord(x) > ord(prev):
                nav_anticlock = ord(x) - ord(prev)
                nav_anticlock = 26 - nav_anticlock
            else:
                nav_anticlock = abs(ord(x) - ord(prev))
            print(x,nav_clock,nav_anticlock)
            ans += min(nav_clock,nav_anticlock)
        print(ans+len(word))
        return ans+len(word)

        