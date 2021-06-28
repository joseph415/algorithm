package practice;

import java.util.Arrays;

public class BinarySearch {
    public static void main(String[] args) {
        int[] bucket = new int[] {4, 12, 14, 23, 45, 53, 74};
        System.out.println(bn(bucket, 24));
    }

    public static int bn(int[] bucket, int n) {
        Arrays.sort(bucket);

        int start = 0;
        int end = bucket.length - 1;
        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (bucket[mid] < n) {
                start = mid + 1;
                continue;
            } else if (bucket[mid] > n) {
                end = mid - 1;
                continue;
            }
            break;
        }
        return bucket[mid];
    }
}
