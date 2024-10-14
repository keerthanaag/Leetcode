class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos=0
        for x in commands:
            if x == 'RIGHT':
                pos+=1
            elif x == 'LEFT':
                pos-=1
            elif x == 'UP':
                pos-=n
            else:
                pos+=n
        return pos
        