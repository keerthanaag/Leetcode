class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        occupied_days = 0
        prev_end = 0

        for start, end in meetings:
            if start > prev_end + 1:
                occupied_days += end - start + 1
            else:
                occupied_days += max(0, end - prev_end)
            
            prev_end = max(prev_end, end)
            
            if occupied_days >= days:
                return 0

        return days - occupied_days
        s = set({})
        for x in meetings:
            print(x)
            s.update(range(x[0], x[1]+1))
            if len(s) == days:
                break
        return days - len(s)

        