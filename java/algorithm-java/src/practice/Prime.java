package practice;

public class Prime {
    public static void main(String[] args) {
        System.out.println(isPrime(17));
        System.out.println(countPrimeRange(10));
    }

    public static int countPrimeRange(int n) {
        boolean[] check = new boolean[n + 1];

        final int sqrt = (int)Math.sqrt(n);
        for (int i = 2; i <= sqrt; i++) {
            if (check[i]) {
                continue;
            }
            check[i] = true;

            for (int j = i + i; j < n+1; j += i) {
                check[j] = true;
            }
        }

        int count = 0;
        for (int i = 0; i < n + 1; i++) {
            if (!check[i]) {
                count++;
            }
        }
        return count;
    }

    public static boolean isPrime(int n) {
        if (n == 0 || n == 1) {
            return false;
        }

        final int sqrt = (int)Math.sqrt(n);
        for (int i = 2; i < sqrt; i++) {
            if (n / i == 0) {
                return false;
            }
        }
        return true;
    }
}
