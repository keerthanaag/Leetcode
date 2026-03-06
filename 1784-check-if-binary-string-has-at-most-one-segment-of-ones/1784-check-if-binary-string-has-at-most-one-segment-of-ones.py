class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        x = re.sub("0+", " ", s)
        return len(x.strip().split(" ")) < 2
            
        