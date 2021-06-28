package practice;

import java.util.ArrayDeque;
import java.util.Deque;

public class Queue {
    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.push(3);
        stack.push(4);
        stack.push(5);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }

    static class Stack {
        private Deque<Integer> push = new ArrayDeque<>();
        private Deque<Integer> pop = new ArrayDeque<>();

        public void push(Integer integer) {
            push.addLast(integer);
        }

        public Integer pop() {
            if (!pop.isEmpty()) {
                return pop.pollLast();
            }

            final int size = push.size();

            for (int i = 0; i < size; i++) {
                pop.addLast(push.pollLast());
            }
            return pop.pollLast();
        }
    }
}
