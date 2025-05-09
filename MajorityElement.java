package org.example;

import java.util.Arrays;

public class MajorityElement {

    public static int majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int candidate = findCandidate(nums, 0, nums.length - 1);
        int count = 0;

        for (int num : nums) {
            if (num == candidate) {
                count++;
            }
        }

        return (count > nums.length / 2) ? candidate : -1;
    }

    private static int findCandidate(int[] nums, int left, int right) {
        if (left == right) return nums[left];

        int mid = (left + right) / 2;
        int leftCandidate = findCandidate(nums, left, mid);
        int rightCandidate = findCandidate(nums, mid + 1, right);

        if (leftCandidate == rightCandidate) return leftCandidate;

        int leftCount = countInRange(nums, leftCandidate, left, right);
        int rightCount = countInRange(nums, rightCandidate, left, right);

        return (leftCount > rightCount) ? leftCandidate : rightCandidate;
    }

    private static int countInRange(int[] nums, int val, int left, int right) {
        int count = 0;
        for (int i = left; i <= right; i++) {
            if (nums[i] == val) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int[] ejemplo1 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println(Arrays.toString(ejemplo1));
        System.out.println("Mayoría: " + majorityElement(ejemplo1));

        int[] ejemplo2 = {1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(ejemplo2));
        System.out.println("Mayoría: " + majorityElement(ejemplo2));
    }
}
