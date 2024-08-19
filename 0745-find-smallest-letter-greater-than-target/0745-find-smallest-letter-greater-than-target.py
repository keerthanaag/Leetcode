class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i,x in enumerate(letters):
            if x > target:
                return x
        return letters[0]