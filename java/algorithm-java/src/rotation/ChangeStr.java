package rotation;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class ChangeStr {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        final String input = scanner.nextLine();
        final String target = scanner.nextLine();
        final String changeStr = scanner.nextLine();

        change(input, target, changeStr);
    }

    private static void change(String input,String target, String changeStr) {
        Queue<String> queue = new ArrayDeque<>();
        StringBuilder stringBuilder = new StringBuilder();

        for (String token : input.split("")) {
            if (queue.size() == 3) {

            }
            queue.add(token);
        }
    }
}
