class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int difference = arr[1] - arr[0];
        for (int i = 1; i < arr.length - 1; i++) {
            int currentDifference = arr[i + 1] - arr[i];
            if (currentDifference != difference) {
                return false; 
            }
        }
        return true;     
    }
}