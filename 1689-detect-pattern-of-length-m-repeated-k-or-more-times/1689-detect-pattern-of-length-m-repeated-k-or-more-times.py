class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for j in range(0,len(arr)-m):
            word = arr[j:j+m]
            count = 0
            for i in range(j,len(arr),m):
                print(arr[i:i+m])
                if arr[i:i+m] == word:
                    count += 1
                else:
                    word = arr[i:i+m]
                    count = 1
                if count == k:
                    print("true",word,count)
                    return True
        return False
        