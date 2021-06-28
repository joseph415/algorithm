package practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class Sort {
    public static void main(String[] args) {
        int[] data = new int[5];
        for (int i = 0; i < 5; i++) {
            data[i] = (int)(Math.random() * 100);
        }
        heapSort(data);
        // mergeSort(0, data.length - 1, data);
        quickSort(data, 0, data.length - 1);
    }

    public static void heapSort(int[] input) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        priorityQueue.addAll(Arrays.stream(input).boxed().collect(Collectors.toList()));
        List<Integer> res = new ArrayList<>();

        while (!priorityQueue.isEmpty()) {
            res.add(priorityQueue.poll());
        }
        res.forEach(integer -> System.out.print(integer + " "));
    }

    public static void mergeSort(int start, int end, int[] input) {
        if (start < end) {
            final int mid = (start + end) / 2;
            mergeSort(start, mid, input);
            mergeSort(mid + 1, end, input);

            merge(start, mid, end, input);
        }
        System.out.println(Arrays.toString(input));
    }

    private static void merge(int start, int mid, int end, int[] input) {
        int[] res = new int[input.length];
        int left = start;
        int right = mid + 1;
        int resIdx = start;

        while (left <= mid && right <= end) {
            if (input[left] <= input[right]) {
                res[resIdx] = input[left];
                left += 1;
                resIdx++;
            } else {
                res[resIdx] = input[right];
                right += 1;
                resIdx++;
            }
        }

        if (left > mid) {
            for (int i = right; i <= end; i++) {
                res[resIdx] = input[i];
                resIdx++;
            }
        } else {
            for (int i = left; i <= mid; i++) {
                res[resIdx] = input[i];
                resIdx++;
            }
        }
        for (int i = left; i <= end; i++)
            input[i] = res[i];
    }

    public static void quickSort(int[] input, int x, int y) {
        if (x >= y) {
            return;
        }

        int pivot = x;
        int left = pivot + 1;
        int right = y;
        int temp;
        while (left < right) {
            while (left <= y && input[left] < input[pivot]) {
                left++;
            }
            while (right >= pivot && input[pivot] < input[right]) {
                right--;
            }
            if (left < right) {
                temp = input[left];
                input[left] = input[right];
                input[right] = temp;
            } else {
                temp = input[pivot];
                input[pivot] = input[right];
                input[right] = temp;
            }

            quickSort(input, x, right - 1);
            quickSort(input, right + 1, y);
        }
        System.out.println(Arrays.toString(input));
    }
}
