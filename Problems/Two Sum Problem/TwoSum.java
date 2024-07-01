import java.util.HashMap;

public class TwoSum {

    /**
     * Finds two numbers in the array 'nums' that add up to 'target'.
     *
     * @param nums   The array of integers to search.
     * @param target The target sum of two numbers in 'nums'.
     * @return An array containing the indices of the two numbers that add up to 'target',
     * or null if no such pair exists.
     */
    public static int[] twoSum(int[] nums, int target) {
        // HashMap to store seen numbers and their indices
        HashMap<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complement = target - num; // Calculate the complement needed to reach 'target'

            // Search the complement in numMap
            if (numMap.containsKey(complement)) {
                // If complement exists in numMap, return the indices of the current number and complement
                return new int[]{numMap.get(complement), i};
            }

            // Store the current number and its index in numMap
            numMap.put(num, i);
        }

        // Return null if no such pair is found
        return null;
    }

    public static void main(String[] args) {
        // Example usage:
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        if (result != null) {
            System.out.println("[" + result[0] + ", " + result[1] + "]"); // Output: [0, 1] (indices of numbers 2 and 7)
        }
    }
}
