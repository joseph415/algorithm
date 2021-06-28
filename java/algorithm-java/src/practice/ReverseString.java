package practice;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ReverseString {
    public static void main(String[] args) {
        String test = "asdf";

        List<String> temp = Arrays.asList(test.split(""));

        Collections.reverse(temp);
        temp.forEach(System.out::print);
        System.out.println();

        char[] res = new char[test.length()];
        final char[] chars = test.toCharArray();

        for (int i = 0; i < test.length(); i++) {
            res[i] = chars[test.length() - 1 - i];
        }
        System.out.println(res);
    }
}
