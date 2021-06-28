package practice;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.stream.Stream;

public class StringPractice {
    public static void main(String[] args) {
        final String a = "qwe";
        final String asd = "asd";

        Random random = new Random();
        System.out.println(random.nextInt(45));

        System.out.println(Math.random());
        final List<String> asList = Arrays.asList(a, asd);
        // asList.stream()
        //         .filter(s -> {
        //             System.out.println(s+"1");
        //             return true;
        //         })
        //         .sorted()
        //         .filter(s -> {
        //             System.out.println(s+"2");
        //             return s.equals("a");
        //         })
        //         .collect(Collectors.toList());
        // Stream.of("qwe","asd")
        //         .filter(s -> {
        //             System.out.println(s+"1");
        //             return true;
        //         })
        //         .distinct()
        //         .filter(s -> {
        //             System.out.println(s+"2");
        //             return s.equals("a");
        //         })
        //         .collect(Collectors.toList());
        Stream.iterate(0, i -> (i + 1) % 2)
                .limit(10)
                .distinct()
                .forEach(System.out::println);
        System.out.println("코드 실행 종료");
    }

    static void dangerous(List<String>... stringLists) {
        List<Integer> intList = Collections.singletonList(42);
        Object[] objects = stringLists;
        objects[0] = intList; // Heap pollution
        String s = stringLists[0].get(0); // ClassCastException
    }
}
