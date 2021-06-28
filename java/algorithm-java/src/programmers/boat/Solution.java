package programmers.boat;

import java.util.ArrayDeque;
import java.util.stream.Collectors;

public class Solution {
    public static int solution(int[] people, int limit) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        for (int person : people) {
            deque.add(person);
        }

        deque = deque.stream()
                .sorted((o1, o2) -> Long.compare(o2, o1))
                .collect(Collectors.toCollection(ArrayDeque::new));

        int answer = 0;

        while (!deque.isEmpty()) {
            if (deque.size() == 1) {
                answer++;
                break;
            }

            Integer first = deque.pollFirst();
            Integer last = deque.pollLast();

            if (first + last > limit) {
                deque.addLast(last);
            }
            answer++;
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[] {70, 50, 80, 50}, 100));
    }
}
