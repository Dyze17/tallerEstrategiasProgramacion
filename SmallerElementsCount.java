package org.example;

import java.util.Arrays;

public class SmallerElementsCount {

    public static int[] countSmallerElementsToRight(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        result[n-1] = 0;

        for (int i = n - 2; i >= 0; i--) {
            int count = 0;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[i]) {
                    count++;
                }
            }
            result[i] = count;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] nums = {5, 2, 6, 1, 3};
        int[] counts = countSmallerElementsToRight(nums);

        System.out.println("Arreglo original: " + Arrays.toString(nums));
        System.out.println("Conteo de elementos menores a la derecha: " + Arrays.toString(counts));
    }
}