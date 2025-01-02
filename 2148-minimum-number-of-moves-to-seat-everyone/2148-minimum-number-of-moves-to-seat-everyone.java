class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        Arrays.sort(seats);
        Arrays.sort(students);
        int pos = 0;
        for(int i=0;i<seats.length;i++){
            pos += Math.abs(seats[i]-students[i]);
        }
        return pos; 
    }
}