package rotation;

import java.util.Scanner;

public class Permutation {
    static int[] check = new int[4];
    static int[] res = new int[4];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final int n = scanner.nextInt();
        final int targetLevel = scanner.nextInt();
        final int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = i + 1;
        }
        dfs(0, targetLevel, a);
    }

    public static void dfs(int level, int targetLevel, int[] a) {
        if (level == targetLevel) {
            for (int i = 0; i < targetLevel; i++) {
                System.out.print(res[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < a.length; i++) {
            if (check[i] == 0) {
                check[i] = 1;
                res[level] = a[i];
                dfs(level + 1, targetLevel, a);
                check[i] = 0;
            }
        }
    }
}
