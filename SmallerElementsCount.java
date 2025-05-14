package org.example;

import java.util.Arrays;

public class SmallerElementsCount {

    public static int[] countSmallerElementsToRight(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int[] indexes = new int[n];

        for (int i = 0; i < n; i++) {
            indexes[i] = i;
        }

        mergeSort(nums, indexes, result, 0, n - 1);
        return result;
    }

    private static void mergeSort(int[] nums, int[] indexes, int[] result, int left, int right) {
        if (left >= right) return;

        int mid = (left + right) / 2;

        mergeSort(nums, indexes, result, left, mid);
        mergeSort(nums, indexes, result, mid + 1, right);
        merge(nums, indexes, result, left, mid, right);
    }

    private static void merge(int[] nums, int[] indexes, int[] result, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int[] tempIndexes = new int[right - left + 1];

        int i = left;
        int j = mid + 1;
        int k = 0;
        int rightCount = 0;

        while (i <= mid && j <= right) {
            if (nums[indexes[j]] < nums[indexes[i]]) {
                rightCount++;
                tempIndexes[k] = indexes[j];
                k++; j++;
            } else {
                result[indexes[i]] += rightCount;
                tempIndexes[k] = indexes[i];
                k++; i++;
            }
        }

        while (i <= mid) {
            result[indexes[i]] += rightCount;
            tempIndexes[k++] = indexes[i++];
        }

        while (j <= right) {
            tempIndexes[k++] = indexes[j++];
        }

        // Copiamos de vuelta los índices ordenados
        for (int p = 0; p < tempIndexes.length; p++) {
            indexes[left + p] = tempIndexes[p];
        }
    }

    public static void main(String[] args) {
        int[] nums = {5, 2, 6, 1, 3};
        int[] counts = countSmallerElementsToRight(nums);

        System.out.println("Arreglo original: " + Arrays.toString(nums));
        System.out.println("Conteo de elementos menores a la derecha: " + Arrays.toString(counts));
    }
}
